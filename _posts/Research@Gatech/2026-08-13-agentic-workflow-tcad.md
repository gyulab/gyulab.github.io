---
layout: post
title: "Building an Agentic Workflow for TCAD Simulation"
date: "2026-08-13T09:00:00-04:00"
description: "A practical guide for semiconductor researchers who want to use coding agents for repetitive TCAD setup, input checking, parameter sweeps, and reproducible reporting."
tags: [1_Georgia_Tech]
---

<iframe src="https://drive.google.com/file/d/1Y6OE-IeEOqfVEkdmI3WGMKyysW7EPz3c/preview" style="width:100%; height:600px;" frameborder="0"></iframe>

Disclaimer: This educational-purpose post is not affiliated with or endorsed by Synopsys, Inc. No Synopsys software, documentation, license, or proprietary examples are distributed. Users must obtain their own licenses and follow their applicable agreements.

<br>

# Motivation: why TCAD workflows are repetitive

&nbsp;&nbsp;&nbsp;&nbsp;TCAD tools give researchers detailed control over structure generation, physical models, meshing, bias conditions, solver settings, and post-processing. That flexibility also creates repetitive work. A typical study involves copying a baseline case, changing a few parameters, checking for unresolved placeholders, launching jobs in the correct environment, parsing logs, extracting metrics, and writing a report.

&nbsp;&nbsp;&nbsp;&nbsp;A coding agent should not be asked to "do TCAD." The researcher remains responsible for the device physics, calibration assumptions, convergence criteria, and interpretation. The agent can instead handle the surrounding workflow: navigating files, running scripts, searching manuals, checking input decks, generating sweeps, summarizing logs, and keeping reproducible records.

<br>

# System view: desktop to simulator

&nbsp;&nbsp;&nbsp;&nbsp;A practical setup has four parts:

1. **Codex desktop**: The researcher describes the task, reviews proposed changes, and approves expensive runs.
2. **SSH server**: The agent connects to the controlled compute environment that contains the project files and scripts.
3. **Project files**: Versioned folders store `AGENTS.md`, reusable skills, baseline input decks, generated cases, logs, and reports.
4. **TCAD execution**: Simulator commands run only after the agent checks the input deck and the researcher confirms the exact case count.

<br>

# Master rules: `AGENTS.md`

&nbsp;&nbsp;&nbsp;&nbsp;`AGENTS.md` contains the standing rules for the project: what the agent may read, what it must not modify, which commands it may run, and what evidence it must provide before execution. Above all, it should protect the baseline inputs.

```markdown
# AGENTS.md

## Project use

This repository supports generic TCAD input checking and parameter sweeps.

## Baseline inputs

- Never edit `cases/baseline/` directly.
- Copy baseline inputs into `runs/<run_id>/input/` before modification.
- Keep generated cases, logs, and reports under `runs/<run_id>/`.

## Manual handling

- Search only approved local documentation for the installed release.
- Cite document ID, release, and page metadata in internal run reports.
- Do not paste licensed manual text into Git, chat, or public notes.

## Execution gate

- Show the input diff and intended case count before simulator execution.
- Ask the researcher to confirm license-consuming jobs.
- Stop after the first non-zero exit code unless the researcher approves another attempt.
```

&nbsp;&nbsp;&nbsp;&nbsp;With these rules in the repository, the researcher does not need to repeat the same constraints in every prompt. A task request can focus on the immediate objective: "debug this placeholder and prepare a three-point drain-bias sweep."

<br>

# Task-specific procedure: `SKILL.md`

&nbsp;&nbsp;&nbsp;&nbsp;A `SKILL.md` file has a narrower purpose. It defines a reusable procedure for one type of task, such as debugging an input-deck parsing failure or preparing a bias sweep. The skill should run only when the request matches that procedure.

```markdown
---
name: tcad-debug-and-sweep
description: Use for generic TCAD input parsing failures, unresolved placeholders, and small researcher-confirmed voltage sweeps. Do not use for model calibration or unpublished process development decisions.
---

1. Read `AGENTS.md` and the task request.
2. Identify the baseline case and confirm it remains read-only.
3. Run host and environment checks without consuming a simulator license.
4. Search approved local documentation for the installed release.
5. Inspect the input deck and report unresolved placeholders.
6. Propose a minimal diff and generated case list.
7. Ask the researcher to confirm the exact case count before execution.
8. Run cases one at a time, preserving stdout, stderr, exit code, and timestamps.
9. Summarize convergence status, extracted metrics, and limitations.
```

&nbsp;&nbsp;&nbsp;&nbsp;In short, `AGENTS.md` defines the standing project rules, while `SKILL.md` defines the steps for a repeatable task.

<br>

# Local manual-search architecture

&nbsp;&nbsp;&nbsp;&nbsp;TCAD syntax depends on the installed release and the tools licensed by the lab. The agent should not guess from memory or rely on internet snippets. It should search approved local manuals instead:

1. Store approved manual PDFs in a non-public `knowledge/raw/` folder on the SSH host.
2. Register each document with product, release, access class, and hash metadata.
3. Build a local text index with section and page metadata.
4. Search the local index before making syntax-related changes.
5. Return short internal citations in the run report, not manual text in public notes.

```yaml
documents:
  - doc_id: device_user_guide
    product: device-simulator
    release: SITE_RELEASE
    path: knowledge/raw/LICENSED_DOCUMENT.pdf
    access: local_only
```

<br>

# Safe input-deck checking

&nbsp;&nbsp;&nbsp;&nbsp;Before launching a job, the agent can run inexpensive checks that do not consume a simulator license:

```bash
./tools/check_host.sh
./tools/check_tcad_case.sh runs/<run_id>/input
python tools/render_case_matrix.py experiments/<sweep>.yaml
git diff -- runs/<run_id>/input
```

&nbsp;&nbsp;&nbsp;&nbsp;These checks catch simple problems before they consume compute time or a license. The agent should block the run and ask for review if a placeholder is unresolved, an include file is missing, or the generated sweep contains more cases than requested.

<br>

# Example: unresolved `@Vd@`

&nbsp;&nbsp;&nbsp;&nbsp;A common failure occurs when an input deck moves from a Workbench-style preprocessing flow to a standalone run with unresolved placeholders. A generic fragment might look like this:

```text
Electrode {
  { Name="drain" Voltage=@Vd@ }
}
```

&nbsp;&nbsp;&nbsp;&nbsp;For a standalone three-point drain-bias sweep, the agent should generate explicit cases and leave the baseline unchanged:

```yaml
baseline: cases/baseline
placeholder: "@Vd@"
parameter: drain_voltage
values_V: [0.05, 0.50, 1.00]
locked_paths:
  - geometry.tdr
  - physics.inc
```

&nbsp;&nbsp;&nbsp;&nbsp;The diff for each generated case should be minimal:

```diff
- { Name="drain" Voltage=@Vd@ }
+ { Name="drain" Voltage=0.50 }
```

&nbsp;&nbsp;&nbsp;&nbsp;The agent should then report the cases it is ready to run:

```text
Ready to execute 3 cases:
1. runs/<run_id>/cases/Vd_0.05V
2. runs/<run_id>/cases/Vd_0.50V
3. runs/<run_id>/cases/Vd_1.00V

Please confirm before simulator execution.
```

<br>

# Researcher confirmation before license-consuming jobs

&nbsp;&nbsp;&nbsp;&nbsp;Confirmation protects shared licenses, queue resources, and research time. Before execution, the agent should show the command pattern, generated input paths, case count, and stop condition. The approval should be explicit:

```text
Run exactly these 3 cases.
Stop after the first non-zero exit code.
Do not add cases, retry failed cases, or change solver settings without asking.
```

&nbsp;&nbsp;&nbsp;&nbsp;This bounds the automation and gives each run a human-approved scope, which makes later debugging easier.

<br>
