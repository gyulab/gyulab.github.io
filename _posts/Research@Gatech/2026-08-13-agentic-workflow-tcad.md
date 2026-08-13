---
layout: post
title: "Building an Agentic Workflow for TCAD"
date: "2026-08-13T09:00:00-04:00"
description: "A practical guide for semiconductor researchers who want to use coding agents for repetitive TCAD setup, input checking, parameter sweeps, and reproducible reporting."
tags: [1_Georgia_Tech]
---

<iframe src="https://drive.google.com/file/d/1Y6OE-IeEOqfVEkdmI3WGMKyysW7EPz3c/preview" style="width:100%; height:600px;" frameborder="0"></iframe>

> This independent educational article is not affiliated with or endorsed by Synopsys, Inc. No Synopsys software, documentation, license, or proprietary examples are distributed. Users must obtain their own licenses and follow their applicable agreements.

<br>

# Motivation: Why TCAD Workflows Are Repetitive

&nbsp;&nbsp;&nbsp;&nbsp;TCAD tools are powerful because they expose detailed control over structure generation, physical models, meshing, bias conditions, solver settings, and post-processing. That same flexibility also creates repetitive research work. A typical study may require copying a baseline case, changing a small set of parameters, checking that placeholders were resolved, launching jobs in the correct environment, parsing logs, extracting metrics, and writing a short report.

&nbsp;&nbsp;&nbsp;&nbsp;For semiconductor researchers who are new to coding agents, the key point is not to let an agent "do TCAD." The researcher still owns the device physics, calibration assumptions, convergence criteria, and final interpretation. The agent is useful for the surrounding workflow: file navigation, script execution, manual search, input-deck checks, sweep generation, log summarization, and reproducible bookkeeping.

<br>

# System View: Desktop to Simulator

&nbsp;&nbsp;&nbsp;&nbsp;A practical setup has four layers:

1. **Codex desktop**: the researcher writes the request, reviews proposed changes, and approves any expensive run.
2. **SSH server**: the agent connects to a controlled compute environment where the project files and scripts live.
3. **Project files**: `AGENTS.md`, reusable skills, baseline input decks, generated cases, logs, and reports are stored in versioned folders.
4. **TCAD execution**: simulator commands run only after the agent has checked the input deck and the researcher has confirmed the exact case count.

<br>

# Master Rules: `AGENTS.md`

&nbsp;&nbsp;&nbsp;&nbsp;`AGENTS.md` is the master rulebook for the project. It should describe what the agent may read, what it must not modify, which commands are allowed, and what evidence is required before a run. The most important rule is to protect the baseline.

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

&nbsp;&nbsp;&nbsp;&nbsp;This keeps the researcher from repeating the same cautionary instructions in every prompt. A short task request can then focus on the physics objective: "debug this placeholder and prepare a three-point drain-bias sweep."

<br>

# Task-specific Procedure: `SKILL.md`

&nbsp;&nbsp;&nbsp;&nbsp;A `SKILL.md` file is narrower than `AGENTS.md`. It describes a reusable operating procedure for one kind of task, such as debugging an input-deck parsing failure or preparing a bias sweep. The skill should trigger only when the task matches that procedure.

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

&nbsp;&nbsp;&nbsp;&nbsp;The practical difference is simple: `AGENTS.md` tells the agent the standing safety rules; `SKILL.md` tells it the ordered procedure for a repeatable task.

<br>

# Local Manual-Search Architecture

&nbsp;&nbsp;&nbsp;&nbsp;TCAD syntax depends on the installed release and the licensed tools available in the lab. An agent should not guess syntax from memory or internet snippets. A safer architecture is local manual search:

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

# Safe Input-Deck Checking

&nbsp;&nbsp;&nbsp;&nbsp;Before launching a job, the agent can run cheap checks that do not consume a simulator license:

```bash
./tools/check_host.sh
./tools/check_tcad_case.sh runs/<run_id>/input
python tools/render_case_matrix.py experiments/<sweep>.yaml
git diff -- runs/<run_id>/input
```

&nbsp;&nbsp;&nbsp;&nbsp;The goal is to fail early. If a placeholder remains unresolved, if an include file is missing, or if a generated sweep contains more cases than requested, the agent should block the run and ask for review.

<br>

# Example: Unresolved `@Vd@`

&nbsp;&nbsp;&nbsp;&nbsp;A common source of failure is moving an input deck from a Workbench-style preprocessing flow into a standalone run without resolving placeholders. A generic fragment might look like this:

```text
Electrode {
  { Name="drain" Voltage=@Vd@ }
}
```

&nbsp;&nbsp;&nbsp;&nbsp;For a standalone three-point drain-bias sweep, the agent should generate explicit cases rather than editing the baseline:

```yaml
baseline: cases/baseline
placeholder: "@Vd@"
parameter: drain_voltage
values_V: [0.05, 0.50, 1.00]
locked_paths:
  - geometry.tdr
  - physics.inc
```

&nbsp;&nbsp;&nbsp;&nbsp;The proposed diff for one generated case should be minimal:

```diff
- { Name="drain" Voltage=@Vd@ }
+ { Name="drain" Voltage=0.50 }
```

&nbsp;&nbsp;&nbsp;&nbsp;The agent should then report:

```text
Ready to execute 3 cases:
1. runs/<run_id>/cases/Vd_0.05V
2. runs/<run_id>/cases/Vd_0.50V
3. runs/<run_id>/cases/Vd_1.00V

Please confirm before simulator execution.
```

<br>

# Researcher Confirmation Before License-Consuming Jobs

&nbsp;&nbsp;&nbsp;&nbsp;The confirmation gate is not bureaucracy. It protects shared licenses, queue resources, and research time. Before execution, the agent should show the exact command pattern, the generated input paths, the case count, and the stop condition. A good confirmation is explicit:

```text
Run exactly these 3 cases.
Stop after the first non-zero exit code.
Do not add cases, retry failed cases, or change solver settings without asking.
```

&nbsp;&nbsp;&nbsp;&nbsp;This keeps automation bounded. It also makes later debugging easier because every run has a clear human-approved scope.

<br>

# Reproducible Run Records

&nbsp;&nbsp;&nbsp;&nbsp;A useful agentic workflow ends with a run record, not just a terminal log. Each report should include:

- Run ID and Git commit
- Installed tool release placeholder
- Confirmed case count
- Input diff and generated sweep matrix
- Hashes for locked files
- Commands executed
- Start time, end time, stdout, stderr, and exit code
- Convergence checks and extracted metrics
- Known limitations and next actions

<br>
