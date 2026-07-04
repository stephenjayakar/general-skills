# Article to Annotated PDF

`article-to-annotated-pdf` is a Codex skill for turning a source document into a polished LaTeX PDF with annotations.

You can hand it a website, PDF, text file, transcript, Markdown document, or pasted article. The skill guides Codex through extracting the source text, formatting it as an academic-style LaTeX document, identifying concepts worth explaining, and producing annotation outputs.

## What It Produces

- A justified LaTeX PDF, usually in a two-column academic-paper style.
- An annotated PDF with real embedded PDF highlights and sticky-note annotations.
- A companion dual-column PDF where the left column is the source text and the right column is annotation prose.
- Optional Obsidian-ready files: a PDF copied into the vault plus a Markdown note with page-linked annotations.
- A `CACHE.md` file of reusable `idea -> summary` entries so repeated concepts do not need to be researched again.

## Annotation Workflow

The skill is designed for dense explanatory annotation, especially for legal or technical text. It prioritizes:

- Proper nouns.
- Case names.
- Statutes and constitutional provisions.
- Agencies and institutions.
- Doctrines, Latin terms, historical references, and named authorities.

For longer documents, it tells Codex to split the work across page ranges and use subagents, typically `gpt-5.3-codex-spark` or `gpt-5.4-mini`, with parallelism of 4 by default.

## Typical Prompt

```text
Use $article-to-annotated-pdf on this PDF. Convert it to a LaTeX academic document, annotate the proper nouns and cases, make an annotated PDF, and also create an Obsidian note next to it.
```

## Included Helper

The skill includes `scripts/pdf_annotate.py`, a PyMuPDF helper that takes JSON annotations and writes real highlight/sticky-note annotations into a PDF.
