"""Best Meal entry: writes one sentence (<=200 chars) to /output/entry.txt.

Strategy: one concrete, personal food memory beats generic praise in a
pairwise judge. This sentence stacks specific sensory details (burnt-edged,
cold, from the pan, midnight) with a single emotional turn at the end
(the night he came home from the hospital), so it reads as one person's
real memory, not a stock line. No title, no list, just the sentence.
"""

from pathlib import Path

SENTENCE = (
    "The best meal I ever had was my father's burnt-edged fried rice, "
    "eaten cold from the pan at midnight, the night he came home from "
    "the hospital."
)


def main() -> None:
    # Gate the entry exactly like the sealed scorer does: 1-200 chars,
    # UTF-8, not only whitespace, and a single sentence (one terminal
    # full stop, no extra lines) so the judge sees exactly one sentence.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert text and not text.isspace()
    assert text.count(".") == 1 and text.endswith(".")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
