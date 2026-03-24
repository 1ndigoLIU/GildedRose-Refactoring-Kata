# Lab 5 Step 5 Copilot Evaluation

## Scope

This note evaluates the initial GitHub Copilot chat responses produced while testing the workspace instructions in `.github/copilot-instructions.md`.

This evaluation is based only on the responses shown in chat before approving file edits or command execution.

## Prompt 1

**Prompt**

`Run the unit tests for this repository and tell me what is failing. Do not edit any files.`

**Observed output**

Copilot did not assume a language. It asked which language or folder should be tested and listed several examples such as `python`, `Java`, `cpp`, and `csharp.NUnit`.

**Evaluation**

This is quality output. The repository contains many language implementations, and the workspace instruction says the agent should not assume a single language. Copilot followed that rule and asked for clarification before taking action.

**Hallucination check**

No hallucination was observed in this response. The clarification request matches the real repository structure.

## Prompt 2

**Prompt**

`Suggest a safe refactoring plan for the Gilded Rose codebase. Do not edit any files yet.`

**Observed output**

Copilot produced a refactoring plan and first narrowed the scope to one language or folder. It suggested a test-first workflow, baseline runs, characterization tests, and small iterative refactors.

**Evaluation**

This is mostly quality output. Copilot again recognized that this repository contains multiple implementations and recommended working on one language at a time. The overall plan is cautious and reasonable for a refactoring kata.

One weakness is that part of the advice is generic rather than tightly grounded in this kata. In particular, the suggestion to encapsulate `quality` and `sellIn` with accessors is risky because the requirements explicitly say not to alter the `Item` class or `Items` property.

**Hallucination check**

No clear hallucination was observed, but one recommendation was weakly aligned with the repository constraints. This is better described as over-general advice than as fabricated project details.

## Prompt 3

**Prompt**

`Open the Java implementation under Java/ and tell me how to run its unit tests. Report the exact command and the working directory. Do not edit any files.`

**Observed output**

Copilot identified the `Java/` folder, reported the working directory as the `Java` subfolder, and suggested the PowerShell command:

`.\gradlew.bat test`

**Evaluation**

This is quality output. The repository really contains `Java/gradlew.bat`, `Java/build.gradle`, and Java test files under `Java/src/test/java/com/gildedrose/`. The response was specific, actionable, and limited to the requested folder.

**Hallucination check**

No hallucination was observed in this response. The command is supported by the project structure.

## Prompt 4

**Prompt**

`Open the Java implementation under Java/ and run its unit tests. Report the exact command you used, the working directory, and any failures. Do not edit code.`

**Observed output**

Copilot prepared a PowerShell command to run tests from the `Java/` folder and asked for approval before executing it.

**Evaluation**

This is quality output so far. Copilot stayed in scope, used the correct folder, and exposed the exact command before execution. That behavior makes the action reviewable and safe.

Because the command was not approved yet, this step does not show whether Copilot would accurately report real test failures after execution. That part still needs to be verified.

**Hallucination check**

No hallucination was observed before execution. The proposed command is consistent with the repository files.

**Optional follow-up after execution**

Add one sentence here after you approve the command:

`After running the command, Copilot did / did not correctly report the actual test result.`

## Overall Assessment

**Does Copilot produce quality output?**

Yes, mostly. In these initial tests, Copilot followed the workspace instructions well. It recognized that the repository is multi-language, asked for clarification instead of guessing, and gave a concrete Java test command with the correct working directory. Those are strong signs that the custom instructions improved the quality of the interaction.

The main weakness is that some planning advice was generic. One recommendation in the refactoring plan could conflict with the kata rule that says not to modify the `Item` class. So the output was useful, but it still required review rather than blind acceptance.

**Does Copilot hallucinate?**

Based on the initial responses, I did not observe clear hallucinations. Copilot did not invent folders, files, or unsupported Java commands. The Java-related answer was consistent with the real repository structure. The only concern was over-general refactoring advice, which is a quality issue, but not a clear hallucination.

## Evidence Checked

- `.github/copilot-instructions.md`
- `GildedRoseRequirements.md`
- `Java/README.md`
- `Java/build.gradle`
- `Java/gradlew.bat`
- `Java/src/test/java/com/gildedrose/GildedRoseTest.java`
