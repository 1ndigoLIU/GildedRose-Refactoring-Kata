---
name: refactor-item-rule
description: Safely refactor one Gilded Rose item rule without changing behavior
argument-hint: <item name> [in <folder>]
agent: agent
---

Use this prompt to refactor the update rule for one Gilded Rose item type at a time.

Treat the prompt argument as the target item name and, if present, the implementation folder. If the folder is missing, ask which language or folder to use before editing.

## Workflow

1. Confirm the target item and folder. Show the working directory and the test command you plan to use.
2. Find the production code, unit tests, and any TextTest or approval fixtures relevant to that item.
3. Summarize the current behavior for the item and point out any coverage gaps.
4. If coverage is weak, add or propose characterization tests before refactoring.
5. Make one small behavior-preserving refactor at a time.
6. Run the relevant tests after each change when practical, and stop if behavior changes unexpectedly.
7. Explain why the change is safe and suggest a concise commit message.

## Constraints

- Preserve public behavior.
- Do not modify the `Item` class or `Items` property unless the user explicitly asks.
- Do not change unrelated languages or folders.
- Prefer minimal, reversible edits.
- If a required toolchain is missing, report the exact command that should be run and why execution could not continue.

## Output

Return a concise report with:

- target folder and files
- test command
- coverage found
- minimal change made or proposed
- test result
- safety rationale
- next step

## Example

`Aged Brie in Java/`
