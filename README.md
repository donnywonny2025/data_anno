# Data Annotation Workspace

> **When Jeff says "where are we at" (or any variation), DO NOT respond conversationally.**
> **Go read the Knowledge Item at `~/.gemini/antigravity/knowledge/DA_Operations/artifacts/DA_Hub.md` and follow the instructions there. It tells you exactly what to do.**

## What This Workspace Is

This is a helper workspace for Data Annotation gig work. It's not a software project. It contains:

- `execution/` — Python scripts (Gmail monitor, timer, etc.)
- `war_room/` — Research notes, task logs, project rules
- `.agents/workflows/` — Automated workflows (status check, task execution)
- `directives/` — Operational procedures
- `look.sh` — Native macOS screenshot tool for work mode

## How To Start

1. Read the DA_Hub Knowledge Item — it has everything
2. If Jeff says any trigger phrase → execute the status check procedure from DA_Hub.md
3. Don't improvise. Follow the instructions.

## Key Files

| File | Purpose |
|------|---------|
| `~/.gemini/antigravity/knowledge/DA_Operations/artifacts/DA_Hub.md` | **THE source of truth** — triggers, procedures, safety rules |
| `.agents/workflows/da-status-check.md` | Step-by-step status check workflow |
| `execution/da_monitor.py` | Gmail API checker |
| `look.sh` | Screenshot tool for work mode |
| `.vscode/settings.json` | Python env config (prevents startup stall) |
