#!/usr/bin/env python3
"""Structural checks for the static site. Exit 1 on the first failing group.

  python3 tools/check_site.py

Checks: every page exists in every language, every local link and asset
resolves, no scripts or forms, every page links the same page in every
language, and the only mailto address is the one the policy names.
"""
from __future__ import annotations

import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
LANGS = ["", "it", "es", "fr", "de", "pt", "nl", "pl"]
PAGES = ["", "privacy", "contact", "philosophy"]
ADDRESS = "caputodav@gmail.com"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.tags, self.langs = [], set(), {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.add(tag)
        for key in ("href", "src"):
            if key in a:
                self.links.append(a[key])
        if tag == "a" and "hreflang" in a:
            self.langs[a["hreflang"]] = a["href"]


def page_path(lang: str, page: str) -> pathlib.Path:
    return ROOT.joinpath(*[p for p in (lang, page) if p], "index.html")


def main() -> int:
    errors: list[str] = []
    for lang in LANGS:
        for page in PAGES:
            path = page_path(lang, page)
            if not path.exists():
                errors.append(f"missing page: {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8")
            p = Page()
            p.feed(text)
            rel = path.relative_to(ROOT)
            if p.tags & {"script", "form", "iframe"}:
                errors.append(f"{rel}: script, form or iframe present")
            if len(p.langs) != len(LANGS):
                errors.append(f"{rel}: language row lists {len(p.langs)} languages, expected {len(LANGS)}")
            for link in p.links:
                if re.match(r"^(https?:|mailto:|#)", link):
                    continue
                target = (path.parent / link.split("#")[0]).resolve()
                if target.is_dir():
                    target = target / "index.html"
                if not target.exists():
                    errors.append(f"{rel}: broken link {link}")
            for addr in re.findall(r"mailto:([^?\"']+)", text):
                if addr != ADDRESS:
                    errors.append(f"{rel}: unexpected address {addr}")
    for f in ("assets/site.css", "assets/icon.png", "assets/favicon.png", "assets/apple-touch-icon.png", ".nojekyll"):
        if not (ROOT / f).exists():
            errors.append(f"missing file: {f}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"{len(LANGS) * len(PAGES)} pages OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
