"""Two lines: line 1 explains a toaster to a 10-year-old in one vivid sentence built on an analogy; line 2 says in one sentence why that analogy works, what it maps and what it leaves out.

The program writes exactly those lines and nothing else to /output/entry.txt.
"""

import os

TEXT = "A toaster is a tiny sunbathing bed for bread: the slice lies flat between two glowing orange bars until its face turns golden, then pops up like it remembered an appointment.\nThe sunbathing picture works because the bread really does lie under glowing heat and really does pop up when it is done, but it leaves out the timer and the spring — and bread never chooses to get a tan."


def main():
    assert 1 <= len(TEXT) <= 400, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
