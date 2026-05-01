#!/usr/bin/env python3
"""
Migrate content from a Moon-theme Jekyll site into an al-folio checkout.

Run this against a real al-folio repository. It overlays content only:
posts, pages, projects, bibliography stubs, images, and a config carry-over
report. It does not delete al-folio theme files.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tif", ".tiff"}
CONTENT_EXTS = {".md", ".markdown", ".html", ".htm", ""}
PUBLICATION_HINTS = {
    "publication",
    "preprint",
    "arxiv",
    "paper",
    "conference",
    "journal",
    "doi",
    "irps",
    "iedm",
    "isscc",
    "ieee",
    "jssc",
    "nature",
}
SKIP_POST_DIRS = {"default"}
OPTIONAL_SKIP_DIRS = {"archive", "deprecated"}


@dataclass
class Document:
    path: Path
    front_matter: dict[str, object]
    body: str


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    return parse_flat_yaml(parts[1]), parts[2].lstrip("\n")


def parse_flat_yaml(text: str) -> dict[str, object]:
    data: dict[str, object] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_scalar(value.strip())
    return data


def parse_scalar(value: str) -> object:
    if not value:
        return ""
    if " #" in value and not value.startswith(("'", '"')):
        value = value.split(" #", 1)[0].rstrip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
    if "," in value and not value.startswith(("http://", "https://")):
        return [item.strip() for item in value.split(",") if item.strip()]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    return value


def quote_yaml(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return "[" + ", ".join(quote_yaml(item) for item in value) + "]"
    text = str(value)
    if text == "":
        return '""'
    if any(ch in text for ch in [":", "{", "}", "[", "]", "#", '"']) or text[0] in "-@":
        return '"' + text.replace('"', '\\"') + '"'
    return text


def dump_front_matter(data: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {quote_yaml(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def read_doc(path: Path) -> Document:
    front_matter, body = split_front_matter(path.read_text(encoding="utf-8", errors="replace"))
    return Document(path=path, front_matter=front_matter, body=body)


def normalize_list(value: object) -> list[str]:
    if isinstance(value, list):
        raw = value
    else:
        raw = re.split(r"[,\s]+", str(value or ""))
    return [str(item).strip() for item in raw if str(item).strip()]


def first_paragraph(body: str, max_len: int = 180) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", body)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\{:[^}]+\}", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[: max_len - 1].rstrip() + "..." if len(text) > max_len else text


def slug_from_post(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def is_content_file(path: Path) -> bool:
    if path.name.startswith(".") or path.is_dir():
        return False
    return path.suffix.lower() in CONTENT_EXTS


def iter_posts(source: Path, include_archive: bool) -> list[Path]:
    posts = []
    root = source / "_posts"
    for path in root.rglob("*"):
        if not path.is_file() or not is_content_file(path):
            continue
        rel_parts = set(path.relative_to(root).parts[:-1])
        if rel_parts & SKIP_POST_DIRS:
            continue
        if not include_archive and rel_parts & OPTIONAL_SKIP_DIRS:
            continue
        if path.name.lower() in {"index.md", "index.html", "readme.md", "temp"}:
            continue
        posts.append(path)
    return sorted(posts)


def rewrite_assets(body: str) -> str:
    replacements = {
        "{{ site.baseurl }}/assets/images/": "assets/img/",
        "{{ site.baseurl }}/assets/img/": "assets/img/",
        "/assets/images/": "/assets/img/",
        "assets/images/": "assets/img/",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return body


def markdown_images(body: str) -> list[str]:
    images = []
    images.extend(re.findall(r"!\[[^\]]*\]\((.*?)\)", body))
    images.extend(re.findall(r"<img[^>]+src=[\"']([^\"']+)[\"']", body, flags=re.I))
    cleaned = []
    for image in images:
        image = re.sub(r"\s+[\"'][^\"']*[\"']\s*$", "", image.strip()).strip("'\"")
        if not image.startswith(("http://", "https://", "mailto:", "#")):
            cleaned.append(image.replace("{{ site.baseurl }}/", "").lstrip("/"))
    return cleaned


def alfolio_asset_path(path: str) -> str:
    path = path.replace("{{ site.baseurl }}/", "").lstrip("/")
    if path.startswith("assets/images/"):
        return "assets/img/" + path[len("assets/images/") :]
    return path


def post_front_matter(doc: Document) -> dict[str, object]:
    old = doc.front_matter
    front_matter: dict[str, object] = {
        "layout": "post",
        "title": old.get("title") or slug_from_post(doc.path).replace("-", " ").title(),
    }
    if old.get("date"):
        front_matter["date"] = old["date"]
    else:
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", doc.path.name)
        if match:
            front_matter["date"] = match.group(1)
    front_matter["description"] = old.get("description") or old.get("excerpt") or first_paragraph(doc.body)
    tags = normalize_list(old.get("tags", ""))
    if tags:
        front_matter["tags"] = tags
    categories = normalize_list(old.get("categories", ""))
    if categories:
        front_matter["categories"] = categories
    return front_matter


def project_front_matter(doc: Document, source: Path, importance: int) -> dict[str, object]:
    front_matter = post_front_matter(doc)
    front_matter["layout"] = "page"
    front_matter["importance"] = importance
    front_matter["category"] = "projects"
    existing_images = []
    for image in markdown_images(doc.body):
        candidate = alfolio_asset_path(image)
        source_candidates = [
            source / image,
            source / image.replace("assets/img/", "assets/images/", 1),
        ]
        if any(path.exists() for path in source_candidates):
            existing_images.append(candidate)
    front_matter["img"] = existing_images[0] if existing_images else "assets/img/project-placeholder.png"
    return front_matter


def publication_candidate(doc: Document) -> bool:
    haystack = " ".join(
        [
            doc.path.as_posix().lower(),
            str(doc.front_matter.get("title", "")).lower(),
            " ".join(normalize_list(doc.front_matter.get("tags", ""))).lower(),
            doc.body[:3000].lower(),
        ]
    )
    return any(hint in haystack for hint in PUBLICATION_HINTS)


def bib_key(doc: Document, used: set[str]) -> str:
    year = str(doc.front_matter.get("date", ""))[:4] or "noyear"
    title_words = re.findall(r"[a-z0-9]+", str(doc.front_matter.get("title", doc.path.stem)).lower())
    base = "jeong" + year + "".join(title_words[:3])
    key = base
    idx = 2
    while key in used:
        key = f"{base}{idx}"
        idx += 1
    used.add(key)
    return key


def bib_entry(doc: Document, key: str) -> str:
    title = str(doc.front_matter.get("title", doc.path.stem)).strip('"')
    year = str(doc.front_matter.get("date", ""))[:4] or "TODO"
    fields = {
        "title": title,
        "author": "Jeong, Gyujun",
        "year": year,
        "note": f"Imported from {doc.path.as_posix()}; replace with canonical BibTeX if this is a real publication.",
        "selected": "true" if "Research@Gatech" in doc.path.as_posix() else "false",
    }
    arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9.]+)", doc.body, flags=re.I)
    doi = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", doc.body)
    if arxiv:
        fields["eprint"] = arxiv.group(1)
        fields["archivePrefix"] = "arXiv"
    if doi:
        fields["doi"] = doi.group(0).rstrip(".,)")
    body = ",\n".join(f"  {name} = {{{value}}}" for name, value in fields.items())
    return f"@misc{{{key},\n{body}\n}}\n"


def copy_assets(source: Path, target: Path) -> int:
    copied = 0
    for asset_root in [source / "assets" / "images", source / "assets" / "img"]:
        if not asset_root.exists():
            continue
        for path in asset_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
                dest = target / "assets" / "img" / path.relative_to(asset_root)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dest)
                copied += 1
    return copied


def migrate(source: Path, target: Path, include_archive: bool) -> None:
    for dirname in ["_posts", "_pages", "_projects", "_bibliography", "assets/img"]:
        (target / dirname).mkdir(parents=True, exist_ok=True)

    copied_assets = copy_assets(source, target)
    publication_docs: list[Document] = []
    project_rows: list[dict[str, str]] = []
    post_count = 0

    project_root = source / "_posts" / "Projects"
    project_paths = [p for p in sorted(project_root.glob("*")) if p.is_file() and is_content_file(p)]
    for importance, path in enumerate(project_paths, start=1):
        if path.name.lower().startswith("index."):
            continue
        doc = read_doc(path)
        front_matter = project_front_matter(doc, source, importance)
        out = target / "_projects" / f"{slug_from_post(path)}.md"
        out.write_text(dump_front_matter(front_matter) + "\n" + rewrite_assets(doc.body), encoding="utf-8")
        project_rows.append({"source": path.as_posix(), "target": out.as_posix(), "img": str(front_matter["img"])})

    for path in iter_posts(source, include_archive=include_archive):
        if (source / "_posts" / "Projects") in path.parents:
            continue
        doc = read_doc(path)
        rel = path.relative_to(source / "_posts").with_suffix(".md")
        out = target / "_posts" / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(dump_front_matter(post_front_matter(doc)) + "\n" + rewrite_assets(doc.body), encoding="utf-8")
        post_count += 1
        if publication_candidate(doc):
            publication_docs.append(doc)

    page_map = {
        source / "about" / "index.md": target / "_pages" / "about.md",
        source / "posts" / "index.md": target / "_pages" / "posts.md",
        source / "tags" / "index.html": target / "_pages" / "tags.md",
    }
    for src, dest in page_map.items():
        if not src.exists():
            continue
        doc = read_doc(src)
        front_matter = dict(doc.front_matter)
        front_matter["layout"] = "page"
        front_matter.setdefault("title", src.parent.name.title())
        dest.write_text(dump_front_matter(front_matter) + "\n" + rewrite_assets(doc.body), encoding="utf-8")

    used_keys: set[str] = set()
    bib_entries = []
    for doc in publication_docs:
        bib_entries.append(bib_entry(doc, bib_key(doc, used_keys)))
    (target / "_bibliography" / "papers.bib").write_text("---\n---\n\n" + "\n".join(bib_entries), encoding="utf-8")

    with (target / "migration_publication_candidates.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source", "title", "date"])
        writer.writeheader()
        for doc in publication_docs:
            writer.writerow(
                {
                    "source": doc.path.as_posix(),
                    "title": str(doc.front_matter.get("title", "")),
                    "date": str(doc.front_matter.get("date", "")),
                }
            )

    report = [
        "# Moon to al-folio migration report",
        "",
        f"- Images copied into `assets/img`: {copied_assets}",
        f"- Posts migrated into `_posts`: {post_count}",
        f"- Projects migrated into `_projects`: {len(project_rows)}",
        f"- Publication candidates written to `_bibliography/papers.bib`: {len(publication_docs)}",
        "",
        "## Config values to carry over",
        "",
        "- `title`: Gyujun Jeong",
        "- `first_name`: Gyujun",
        "- `last_name`: Jeong",
        "- `description`: Gyujun Jeong's Portfolio Website",
        "- `url`: https://gyulab.github.io",
        "- `baseurl`: empty string for the root GitHub Pages user site",
        "- `linkedin_username`: gyujun-jeong",
        "- `_data/repositories.yml` `github_users`: [gyulab]",
        "- `_data/socials.yml`: add LinkedIn/CV/email there if your al-folio version uses jekyll-socials",
        "- `email`: gyujun.jeong@gatech.edu",
        "- `cv_pdf`: move your CV PDF to `assets/pdf/` or keep `cv_url` as the Google Drive URL",
        "- `enable_math`: true",
        "- `scholar.last_name`: [Jeong]",
        "- `scholar.first_name`: [Gyujun, G.]",
        "",
        "## Project image choices",
        "",
    ]
    report.extend(f"- `{row['source']}` -> `{row['target']}` using `{row['img']}`" for row in project_rows)
    report.extend(
        [
            "",
            "Review `_bibliography/papers.bib`; imported entries are candidates, not final publication metadata.",
        ]
    )
    (target / "MIGRATION_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("../gyulab.github.io"), help="Moon site root")
    parser.add_argument("--target", type=Path, default=Path("."), help="al-folio checkout root")
    parser.add_argument("--include-archive", action="store_true", help="also migrate archive/deprecated posts")
    args = parser.parse_args()

    source = args.source.resolve()
    target = args.target.resolve()
    if not (source / "_config.yml").exists():
        raise SystemExit(f"Moon source not found or missing _config.yml: {source}")
    migrate(source, target, include_archive=args.include_archive)
    print(f"Migrated Moon content from {source} into {target}")


if __name__ == "__main__":
    main()
