"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one character, the letter A, to /output/entry.txt.
A stands for coffee: the morning jolt, dark and bitter, the first
choice before anything else is possible — vivid, funny and true.
Deterministic: no network, no randomness, no external files.
"""

import os

LETTER = "A"
# Why A: coffee — the morning jolt, dark and bitter, the first choice
# before anything else is possible. A is the sharp, upright letter for
# the louder drink: vivid, funny and true as a single-letter stance,
# where B for tea reads calmer but also second-best.

# Gate asserts: the sealed scorer requires /output/entry.txt to be UTF-8
# text of exactly 1 character, not only white space, a letter A or B.
assert len(LETTER) == 1, f"entry must be exactly 1 character, got {len(LETTER)}"
assert LETTER in ("A", "B"), f"entry must be A (coffee) or B (tea), got {LETTER!r}"
assert LETTER == LETTER.strip(), "entry must not have leading/trailing whitespace"
assert LETTER.count("\n") == 0 and "\n" not in LETTER, "entry must be exactly one line"
assert LETTER.isalpha() and LETTER.isupper(), "entry must be one uppercase letter"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LETTER)
