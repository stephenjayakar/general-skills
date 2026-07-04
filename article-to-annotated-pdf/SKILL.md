---
name: article-to-annotated-pdf
description: Convert source text, transcripts, articles, Markdown, or documents into polished academic-style LaTeX PDFs with optional dense annotations, embedded PDF highlights/sticky notes, dual-column transcript/annotation companion PDFs, CACHE.md lookup files, and Obsidian companion notes. Use when Codex is asked to make an annotated PDF workflow from text or a document, define legal/proper-noun references, generate two-column or side-by-side LaTeX output, or sync PDF annotations with Markdown notes.
---

# Article To Annotated PDF

## Workflow

1. Identify the source artifact: plain text, Markdown, PDF, DOCX, transcript, or pasted text.
2. Choose outputs requested by the user:
   - Academic paper PDF: justified LaTeX, two columns.
   - Embedded annotated PDF: PyMuPDF highlights plus sticky-note annotations.
   - Companion annotation PDF: portrait LaTeX, left column source text, right column notes.
   - Obsidian note: Markdown page-linked notes beside the PDF.
3. Create or update `CACHE.md` in the project or requested note folder. Before researching a concept, search the cache and reuse matching `idea -> summary` entries.
4. Extract annotation targets. For long documents, split by page ranges and use subagents.
5. Generate the base LaTeX PDF, then apply PDF annotations and/or create companion outputs.
6. Render at least one representative page for visual review when layout matters.

## Subagent Policy

Use the user's current/main model for orchestration. When spawning subagents for extraction/research, prefer:

- `gpt-5.3-codex-spark` for fast page-range extraction and proper-noun/case inventories.
- `gpt-5.4-mini` for slightly more reasoning-heavy summaries when Spark output is too thin.

Use parallelism of 4 by default for medium/large documents. Assign disjoint page ranges and ask each subagent for:

```text
page number, exact anchor phrase, one-sentence definition, and whether it is a case/statute/person/doctrine.
```

Keep subagent tasks read-only unless explicitly assigning a disjoint write scope.

## Annotation Targeting

Annotate terms a smart reader may not know:

- Case names and case-like references.
- Statutes, constitutional provisions, regulations, and agencies.
- Legal doctrines and Latin/French/common-law terms.
- Judges, advocates, senators, framers, scholars, treatise authors.
- Historical institutions or movements relevant to the argument.

Avoid annotating every repeated occurrence. Prefer first meaningful occurrence per page or section.

## File Patterns

Use stable output names:

- `main-academic.pdf` for the base academic PDF.
- `main-academic-annotated.pdf` for embedded PDF annotations.
- `main-first10-latex-columns.pdf` or similar for dual-column source/annotation companion PDFs.
- `CACHE.md` for reusable concept summaries.
- `<PDF basename> notes.md` for Obsidian companion notes.

## Scripts

Use `scripts/pdf_annotate.py` for adding highlights and sticky notes from a JSON annotation table.

Read `references/layout-and-obsidian.md` when creating:

- LaTeX dual-column source/annotation PDFs.
- Obsidian companion notes with `[[file.pdf#page=N|Page N]]` links.
- PDF++/Obsidian-style annotation workflows.
