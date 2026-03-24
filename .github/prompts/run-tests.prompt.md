---
name: run-tests
description: Run or plan tests for one implementation folder and report the exact command and working directory
argument-hint: <folder> [with <command>]
agent: agent
---

Use this prompt to identify or run tests for a single language folder in this multi-language repository.

Treat the prompt argument as the target folder and an optional explicit command. If the folder is missing, ask before continuing.

## Workflow

1. Confirm the target folder and working directory.
2. If no explicit command is provided, inspect that folder for the most likely test entry point such as `gradlew`, `pom.xml`, `pytest`, `Makefile`, or `CMakeLists.txt`, and explain the choice.
3. Show the exact command before running it.
4. If execution has not been disabled, run the tests and capture the result.
5. Summarize failures briefly and suggest the next 1-3 actions.

## Constraints

- Do not edit repository files.
- Stay within the requested folder.
- If multiple commands look valid, explain the ambiguity instead of guessing.
- If execution needs approval or a missing toolchain blocks progress, say so clearly.

## Output

Return:

- working directory
- command
- status
- failing tests or notable output
- next actions

## Examples

`Java/`

`python/ with pytest -q tests/test_gilded_rose.py`
