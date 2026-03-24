---
name: copilot-instructions
description: "Workspace instructions for AI assistants: how to run tests, common workflows, and recommended agent behavior for the Gilded Rose refactoring kata repository."
---

Purpose
-------

These workspace instructions give concise, actionable guidance to AI assistants working in this repository. They are intentionally short — prefer asking for clarification rather than guessing.

What the agent may do
- Read project README and language subfolder READMEs to discover test/build commands.
- Run or suggest the appropriate test commands for a target language folder.
- Create, modify, or propose changes to code and tests, and run the relevant tests when asked.

Agent behavior and constraints
- Do not assume a single language; this repo contains many language implementations (see top-level folders such as `python`, `java`, `csharp.NUnit`, `cpp`, etc.). Before modifying code, confirm which language/folder the user wants to target.
- Prefer minimal, focused edits. Keep changes small and well-tested.
- Do not use `applyTo: "**"` global instructions. Use narrow file globs if creating file-scoped instructions.

Developer workflows (quick reference)
- Run TextTest (Unix):

```bash
./start_texttest.sh
```

- Run TextTest (Windows):

```powershell
start_texttest.bat
```

- Create venv and run TextTest (Python helper, Windows):

```powershell
start_texttest_from_python.bat
```

- Common bash helpers (in `bash/`):

```bash
bash/unit_test.sh       # run language-agnostic unit helpers
bash/texttest_fixture.sh [Days]  # prepare TextTest fixtures
bash/verify.sh          # run verification scripts
```

Notes about tests and builds
- Many language subfolders contain their own README with language-specific build/test commands. Check the target folder (for example `python/`, `java/`, `csharp.NUnit/`) for exact steps.
- When asked to run tests, prefer showing the exact command and the working directory to run it from.

Suggested prompts for common tasks
- "Open the Java implementation under `Java/` and run its unit tests; report failures and suggest minimal fixes." 
- "Refactor `GildedRose.c` to improve readability without changing behavior; run C tests and show results."

When to ask the user
- If the user does not specify a target language or folder, ask: "Which language/folder should I work in? (examples: `python/`, `Java/`, `cpp/`)"
- If a change could affect many implementations, ask whether to update all language variants or only one.

Where to add further instructions
- If you want persistent, language-specific agent behavior, add file-scoped instructions under `.github/instructions/` with `applyTo` globs (for example `.github/instructions/python.instructions.md`).

Contact & follow-up
- After making changes, suggest running the precise test command and offer to commit the change if the user approves.
