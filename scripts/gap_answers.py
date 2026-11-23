#!/usr/bin/env python3
"""A page's practice must not print its own answer.

A learner who reads "You want *ik heb het koud*" and then meets
"Ik ___ het koud" one line down copies, they don't recall. This check finds
each game on a page whose answer the rest of the page already shows:

- a `:::cloze` gap (and each line of a page's `extras.cloze`, which the
  session's Reading card shows) whose filled words, the answer plus up to two
  words either side, appear as a run anywhere else on the page;
- a `:::predict` whose subject and answer appear side by side;
- a `:::parse` or `:::order` sentence that another sentence on the page
  mostly repeats (seven words in ten or more), since the page then shows its
  parts, or its word order, before the game asks for them.

"The rest of the page" is the body with every game block taken out, plus the
sentences other games show and the page's `extras.examples`.

    python3 scripts/gap_answers.py PACK.json...   # lint pack files, custom ones too
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

GAME_BLOCK = re.compile(
    r"^:::(cloze|order|parse|predict)\{([^}\n]*)\}[ \t]*\n(.*?)^:::[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
ATTR = re.compile(r'(\w+)="([^"]*)"')
TOKEN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*'?")
# A run never crosses a sentence end, and a table row is one run of its cells.
BREAK = re.compile(r"[.!?;:\n]")
GAP = "___"
WINDOW = 2
REPEAT_SHARE = 0.7
REPEAT_MIN = 4


def tokens(text: str) -> list[str]:
    return [m.group(0).lower().rstrip("'") or m.group(0).lower() for m in TOKEN.finditer(text)]


def chunks(text: str) -> list[list[str]]:
    """Each line of `text` as runs of words: a table row whole, prose by sentence."""
    out: list[list[str]] = []
    for line in text.split("\n"):
        parts = [line] if line.lstrip().startswith("|") else BREAK.split(line)
        out += [t for t in (tokens(p) for p in parts) if t]
    return out


def has_run(haystack: list[list[str]], run: list[str]) -> bool:
    n = len(run)
    return any(c[i : i + n] == run for c in haystack for i in range(len(c) - n + 1))


def gap_window(sentence: str, blank: str) -> list[str] | None:
    """The answer and up to WINDOW words either side, read off the filled sentence."""
    if sentence.count(GAP) != 1 or not blank.strip():
        return None
    before, after = sentence.split(GAP)
    filled = before + blank + after
    start, end = len(before), len(before) + len(blank)
    spans = list(TOKEN.finditer(filled))
    hit = [i for i, m in enumerate(spans) if m.start() < end and m.end() > start]
    if not hit:
        return None
    words = [m.group(0).lower().rstrip("'") for m in spans]
    return words[max(0, hit[0] - WINDOW) : hit[-1] + WINDOW + 1]


def repeated_by(sentence: str, haystack: list[list[str]]) -> bool:
    words = set(tokens(sentence))
    if len(words) < REPEAT_MIN:
        return False
    return any(
        len(words & set(c)) >= max(REPEAT_MIN, REPEAT_SHARE * len(words)) for c in haystack
    )


def _short(text: str, limit: int = 48) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "…"


def check_page(page: dict) -> list[str]:
    body = page.get("body_md") or ""
    extras = page.get("extras") or {}
    games = [
        (m.group(1), dict(ATTR.findall(m.group(2))), m.span()) for m in GAME_BLOCK.finditer(body)
    ]
    shown = [
        attrs.get("sentence", "").replace(GAP, " ")
        for name, attrs, _ in games
        if name in ("cloze", "parse")
    ] + [str(e) for e in extras.get("examples", []) if isinstance(e, str)]
    bare = GAME_BLOCK.sub("", body)
    label = page.get("id", "?")
    errors: list[str] = []

    def rest_without(own: str) -> list[list[str]]:
        others = list(shown)
        if own in others:
            others.remove(own)
        return chunks(bare) + [t for t in (tokens(s) for s in others) if t]

    clozes = [(a.get("sentence", ""), a.get("blank", ""), "") for n, a, _ in games if n == "cloze"]
    clozes += [
        (c.get("sentence", ""), c.get("blank", ""), " on the Reading card")
        for c in extras.get("cloze", [])
        if isinstance(c, dict)
    ]
    for sentence, blank, where in clozes:
        run = gap_window(sentence, blank)
        if run and has_run(rest_without(sentence.replace(GAP, " ")), run):
            errors.append(
                f"page {label}: the gap{where} \"{_short(sentence)}\" is answered elsewhere on the page "
                f"(\"{' '.join(run)}\")"
            )

    for name, attrs, _ in games:
        if name == "predict":
            prompt, answer = attrs.get("prompt", ""), attrs.get("answer", "")
            subject = tokens(prompt.split("(")[0])
            run = subject + tokens(answer)
            if subject and tokens(answer) and has_run(rest_without(""), run):
                errors.append(
                    f"page {label}: the prediction \"{prompt}\" is answered elsewhere on the page "
                    f"(\"{' '.join(run)}\")"
                )
        elif name in ("parse", "order"):
            sentence = attrs.get("sentence", "")
            if repeated_by(sentence, rest_without(sentence.replace(GAP, " "))):
                errors.append(
                    f"page {label}: the {name} sentence \"{_short(sentence)}\" is printed, near enough, "
                    "elsewhere on the page"
                )
    return errors


def check_gap_answers(pack: dict) -> list[str]:
    """Every game on the pack's pages whose answer its page already prints."""
    errors: list[str] = []
    for item in pack.get("items", []):
        if item.get("kind") == "misc" and item.get("body_md") is not None:
            errors += check_page(item)
    return errors


def main(paths: list[str]) -> int:
    failed = False
    for p in paths:
        errs = check_gap_answers(json.loads(Path(p).read_text()))
        print(f"{Path(p).name}: {'ok' if not errs else f'{len(errs)} answered gaps'}")
        for e in errs:
            print(f"  {e}")
        failed |= bool(errs)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
