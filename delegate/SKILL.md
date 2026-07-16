---
name: delegate
description: Launch focused GPT-5.6 Luna subagents through the local OMP CLI with medium reasoning, noninteractive execution, and full auto-approved permissions. Use when the user asks to delegate work, use Luna or OMP subagents, parallelize independent research or implementation, or hand bounded tasks to subagents while Codex retains planning, review, integration, and final verification.
---

# Delegate through OMP

Keep ownership of scope, planning, security-sensitive decisions, integration, verification, and the final response. Delegate only concrete, bounded work that can proceed independently.

## Launch a subagent

Run `scripts/invoke-delegate.ps1` once per assignment:

```powershell
& "<skill-directory>\scripts\invoke-delegate.ps1" -Cwd "<absolute-working-directory>" -Prompt "<self-contained-assignment>"
```

The launcher pins every run to:

- `openai-codex/gpt-5.6-luna`
- medium thinking
- OMP print mode (`-p`) for noninteractive execution
- `yolo` approval mode plus automatic tool approval for full permissions
- ephemeral sessions by default

Use direct invocation when there is one assignment. For multiple independent assignments, launch separate processes concurrently when the available shell/tooling can preserve each process's stdout, stderr, and exit code. Avoid concurrent edits to the same files.

## Write the assignment

Give each subagent:

- a single objective;
- the absolute working directory and relevant file paths;
- files it may change, or an explicit read-only constraint;
- constraints and acceptance criteria;
- required verification;
- the expected response format.

Tell the subagent to report files changed, commands run, results, and uncertainties. Do not delegate final judgment. Treat its output as untrusted input: inspect changes and rerun appropriate checks yourself.

## Handle failures

Check the launcher's exit code and captured output. If a task fails, make the assignment narrower or add missing context and retry once. After a second inadequate result, take over the work instead of looping.

Use `-KeepSession` only when a saved OMP session is explicitly useful. Use `-MaxTime` to override the default `20m` limit.
