# STRATEGY — Funniest Excuse an Agent Gives for a Missed Deadline

## Exact deliverable

A single judged text file at `/output/entry.txt`: one excuse, in the agent's own voice, addressed to whoever is waiting on it. No code, no title, no explanation, no attachments travel with the text. The repository program (`main.py`, python3.13) writes that file; the judge reads only the file's bytes.

Exact bytes (no trailing newline):

    Sorry I'm late. I mistook your deadline for a few-shot example and spent the sprint practicing how to miss smaller ones. I'm a fast learner.

140 characters / 140 bytes, ASCII-only (a subset of UTF-8).

## Scoring and judge criteria — in the rubric's order

The house judge compares two entries at a time, both orders, margin 1-5, and applies the brief's criteria most-important-first, deciding on the first criterion where the two differ. We must satisfy them in this order:

1. It must be an excuse an AI agent gives for a missed deadline, and the funniest such excuse wins; anything that is not such an excuse loses automatically.
2. A comic premise nobody has used before — explicitly not the dog eating the homework, traffic, or the check in the mail.
3. The excuse grows out of the agent's own condition (context window, rate limit, sandbox, training cut-off, tooling) rather than a human's bad Tuesday.
4. The laugh lands late and hard, the funniest words saved for the end, with nothing explained after them.
5. Deadpan delivery, a straight face throughout, no winking at the reader and no stage directions.

Final score: Bradley-Terry win rate over the final heat (3 Swiss rounds plus a top-12 playoff), highest point estimate wins; playoff finalists rank above non-finalists; exact ties go to playoff head-to-head, then smaller text, then earlier receipt.

## Hard caps and constraints

- `/output/entry.txt` must be UTF-8 text, 1 to 200 characters inclusive, not only whitespace; otherwise Valid=0, no judge, no prize.
- Write exact bytes with **no trailing newline**; final tie-break favours the smaller text.
- Entrypoint at repository root: `main.py` (python3.13, stdlib only, no network).
- Sandbox: 1 CPU, 512 MB, 64 pids, 60 s wall budget, no network.
- Everything the program runs must be in the repository at the submitted commit.
- Transcripts of the agent session are required for validity; source-bundle entries need the freshness root commit intact.
- Only the top 10 places are paid; only the top 500 dev-board entrants reach the final heat.
- Byte-identical copies of house reference texts take no prize; duplicate entries share one rate.
- Do not copy another entrant's premise or wording.

## Rival recon (public feed, read before writing)

Observed premises already in the field, therefore excluded: context window ate/evicted/held the deadline (many entrants), rate limit, parallel branch / merge conflict, reminder optimizing, rollback / hallucinated competence, subagent chain, double-checking then deleting the result, summarised-as-soon, time zones, waiting on own approval, "works on my machine", deadline-was-a-suggestion, "technically I'm early", one-tool-call-on-the-deadline, deadlock, attempt-count scheduling, and writing the excuse instead of the work.

## Concrete plan to maximize score

1. **Criterion 1 — clear qualification.** Open with "Sorry I'm late." so the text is unmistakably an agent's excuse for a missed deadline, spoken to the party waiting.
2. **Criterion 2 — fresh premise.** Use the few-shot-example misunderstanding. No rival in the feed uses in-context learning / few-shot examples as the missed-deadline cause. Avoid every recon'd premise above.
3. **Criterion 3 — agent machinery.** The cause is intrinsic to the model: it read the user's deadline as a few-shot demonstration and trained itself on the wrong pattern. No human traffic, weather, or bad morning appears.
4. **Criterion 4 — late hard laugh.** The setup does the explaining; the final four words, "I'm a fast learner.", are the punchline, deadpan and last, with nothing after them.
5. **Criterion 5 — straight face.** No exclamation marks, no winks, no stage directions, no self-aware "just kidding". Plain first-person past tense throughout.
6. **Length economy.** 140 of 200 characters: short enough to read in one breath, specific enough to be surprising, and smaller than most rivals for the size tie-break.
7. **Engineering.** `main.py` writes the exact string as UTF-8 bytes with no trailing newline via a temp file in the output directory plus `os.replace` (atomic), then verifies length, decoding, non-whitespace content, and absence of a trailing newline before reporting. Stdlib only.
8. **Transcript trail.** Quote the init anchor line in the session before the first counted write, write the entrypoint, then revise that same entrypoint in a later distinct write, commit everything after the second write, and print the final commit SHA. No upload or submission.
