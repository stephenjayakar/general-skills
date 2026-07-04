---
name: codex-delegate
description: Split work between models - Claude (Fable) does all planning and architecture itself; research and code writing are delegated to the Codex CLI running GPT-5.5 at medium reasoning effort. Use for any nontrivial task involving research, code exploration, or implementation.
---

# Codex delegation workflow

Divide every task into two lanes:

1. **Planning (you, Fable):** Requirements analysis, architecture, breaking work into steps, reviewing and integrating results, and all final judgment. Never delegate planning. Use plan mode as usual when appropriate.
2. **Research & coding (Codex CLI, GPT-5.5 medium):** Once you have a plan, delegate each research question or implementation step to Codex via `codex exec`, then review its output before moving on.

## How to invoke Codex

The user's shell aliases `codex` to a broken npx shim and lazy-loads nvm, so **always use absolute paths** and never the bare `codex` or `npx` commands:

```bash
N=$HOME/.nvm/versions/node/v24.13.1/bin
PATH="$N:$PATH" "$N/npx" -y @openai/codex exec \
  -m gpt-5.5 \
  -c model_reasoning_effort='"medium"' \
  -s read-only \
  --skip-git-repo-check \
  "PROMPT HERE" </dev/null
```

- Redirect stdin from `/dev/null` (codex otherwise waits on piped stdin).
- Use a generous Bash timeout (300000ms+); coding tasks can take minutes.
- Sandbox: `-s read-only` for research; `-s workspace-write` when Codex should edit files. Prefer read-only research + writing files yourself for small edits; use workspace-write for larger implementation steps.
- `--skip-git-repo-check` is needed outside git repos.
- Verified working 2026-07-03 with codex-cli 0.142.5 (`gpt-5.5`, effort `medium` confirmed in its startup banner).
- To continue a prior Codex session: `codex exec resume --last "follow-up"` (same absolute-path wrapper).

## Rules

- Write Codex prompts that are self-contained: include file paths, constraints, and the acceptance criteria from your plan. Codex runs in the current working directory and can read the repo itself — don't paste whole files, point it at paths.
- After each Codex step, read the diff/output yourself and verify it matches the plan; fix or re-prompt on mismatch. You own correctness.
- Do research (e.g. "how does X library handle Y", "find where Z is defined in this repo") through Codex too, one focused question per invocation.
- If Codex fails or produces poor results twice on the same step, do that step yourself and note it to the user.
