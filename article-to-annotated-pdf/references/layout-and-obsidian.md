# Layout And Obsidian Reference

## Academic LaTeX PDF

Use an `article` document with `geometry`, `lmodern`, `microtype`, and normal LaTeX justification. For a base article:

```latex
\documentclass[10pt,twocolumn]{article}
\usepackage[letterpaper,margin=0.72in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{microtype}
\setlength{\columnsep}{0.24in}
```

For transcript-like text, bold standalone speaker names and preserve paragraphs.

## Source / Annotation Companion PDF

Use portrait by default when the user says "same as original columns." Use equal-width side-by-side columns:

```latex
\begin{minipage}[t][0.86\textheight][t]{0.47\textwidth}
\justifying\fontsize{5.2}{5.9}\selectfont
% source text
\end{minipage}\hfill
\begin{minipage}[t][0.86\textheight][t]{0.47\textwidth}
\justifying\fontsize{5.2}{5.9}\selectfont
% annotations
\end{minipage}
```

Use landscape only when readability is more important than preserving original proportions.

## Annotation JSON Shape

Use this shape for scripts and for merging subagent outputs:

```json
[
  {
    "page": 1,
    "anchor": "Citizenship Clause",
    "note": "First sentence of the Fourteenth Amendment; the core dispute is what 'subject to the jurisdiction thereof' means.",
    "kind": "constitutional provision"
  }
]
```

## Obsidian Companion Notes

Place the PDF and note in the same Obsidian folder when requested. Use wiki links:

```md
#law #pdf [[2026-07-02]]

[[Oral Argument Transcript annotated.pdf]]

### Page 1: framing the issue
[[Oral Argument Transcript annotated.pdf#page=1|Page 1]]
* **Citizenship Clause**: First sentence of the Fourteenth Amendment; the core dispute is what "subject to the jurisdiction thereof" means.
```

Use `#page=N` links unless precise PDF++ `selection=` coordinates are available. Do not invent selection coordinates.

## Cache

Write cache entries as:

```md
- `idea` -> One-sentence summary. Authorities: case/statute/source names.
```

Search `CACHE.md` before adding new lookups.
