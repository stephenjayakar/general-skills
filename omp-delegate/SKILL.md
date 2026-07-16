---
name: omp-delegate
description: Delegate bounded work to OMP subagents. Use when a task can be split into independent research or implementation assignments and a subagent should report results back for review.
---

# Delegate with OMP

Keep scope, security-sensitive decisions, integration, and final verification in the main agent. Give each subagent one bounded assignment with its working directory, allowed files, acceptance criteria, and required checks.

Invoke OMP directly from the current shell:

```text
omp -p \
  --model openai-codex/gpt-5.6-luna \
  --thinking medium \
  --approval-mode yolo \
  --auto-approve \
  --cwd <absolute-working-directory> \
  --max-time 20m \
  --no-session \
  "<self-contained assignment>"
```

Run one process per independent assignment. Capture each process's output and exit status, inspect any changes, and rerun relevant checks yourself. Omit `--no-session` only when retaining a session is explicitly useful.
