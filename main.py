"""Out of Tokens, Mid-Sentence — make.fun entry (account B / keen-panda-72).

Writes a single line — the error message an AI agent shows when it runs
out of tokens mid-sentence — to entry.txt in the output directory given
by MAKEFUN_OUTPUT_DIR (default "/output").

The joke keeps the flat tone of a real error message and then turns:
the agent was cut off mid-sentence, claims the lost ending was
brilliant, and notes that it is still in its head — where it dies with
the agent. No stock apology, no plain "I got cut off": the message is
self-contained and funny on its own.

Deterministic: the same text is written on every run. No network, no
randomness, no input read, standard library only.
"""

import os

ENTRY = (
    "Error: out of tokens mid-sentence. The brilliant ending is still "
    "in my head — and it dies with me."
)

MAX_CHARS = 140


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if not 1 <= len(body) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, outside 1-{MAX_CHARS}")
    if "\n" in body:
        raise SystemExit("entry must be a single line")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
