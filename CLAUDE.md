# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python educational course** written in **Traditional Chinese** using **Emacs Org-Mode**. Content is authored in `.org` files and exported to HTML for publishing on GitHub Pages at `letranger.github.io/PythonCourse/`.

## Content Structure

- **`index.org`** — Main entry point linking to all modules
- **`PythonBasic.org`** — Core Python fundamentals (variables, control flow, data structures, I/O)
- **`PythonAdvanced.org`** — Advanced topics (functions, classes, OOP)
- **Library guides:** `Numpy.org`, `Pandas.org`, `Matplotlib.org`, `Streamlit.org`, `Crawler.org`, `gui.org`, `Sympy.org`, `PyTorch.org`
- **Specialty topics:** `WordCloud.org`, `findImage.org`, `ipLocation.org`, `VideoDownloader.org`
- **`exams.org`** — Exam/exercise materials

## Critical Rule: Edit .org Files, Never .html

All `.html` files are **generated output** from Org-Mode export. Always edit the corresponding `.org` source file. The HTML will be regenerated on export.

## Org-Mode File Conventions

Every course `.org` file uses this standard header pattern:

```org
#+INCLUDE: ../pdf.org
#+PROPERTY: header-args :eval never-export
#+TAGS: Python
#+EXCLUDE_TAGS: noexport
#+OPTIONS: toc:2 ^:nil num:3
#+OPTIONS: H:4
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="../css/muse.css" />
#+HTML_HEAD_EXTRA: <script src="../css/copy_code.js"></script>
```

Key details:
- `#+INCLUDE: ../pdf.org` pulls shared LaTeX/PDF export config from the parent directory
- `:eval never-export` prevents code block execution during export
- `:EXCLUDE_TAGS: noexport` hides sections tagged `noexport` from output
- Sections use `:CUSTOM_ID:` properties for stable HTML anchor links

## Build / Export Process

There is no Makefile. Export is done interactively through Emacs:

- **HTML export:** Open `.org` file in Emacs, run `C-c C-e h h` (org-export-dispatch → HTML)
- **PDF export:** `C-c C-e l p` (org-export-dispatch → LaTeX → PDF)
- Shared CSS: `../css/muse.css` (in parent directory)
- Code copy button: `../css/copy_code.js`

## Python Environment

A local `venv/` directory exists for testing code examples. Activate with:
```bash
source venv/bin/activate
```

## Assets

- **`images/`** — Screenshots, diagrams, and charts used in course materials
- **`js/`** — MathJax (math rendering) and Prettify (syntax highlighting)
- **`datasets/`** — Sample data files for exercises

## Deployment

Content is published to GitHub Pages. After exporting `.org` → `.html`, commit and push to trigger deployment.
