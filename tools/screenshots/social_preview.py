#!/usr/bin/env python3
"""Draw docs/assets/social-preview.png (1280x640) from the site's own tokens.

  make social
"""
from __future__ import annotations

import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[2]
W, H = 1280, 640
TOP, BOTTOM = (15, 24, 38), (22, 36, 58)  # --sky-top / --sky-bottom, dark
TEXT, MUTED, ACCENT, SURFACE, LINE = (237, 239, 243), (183, 193, 206), (140, 199, 191), (26, 38, 56), (43, 55, 72)
FONTS = ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/SFNS.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(TOP, BOTTOM)))
    icon = Image.open(ROOT / "docs/assets/brand/icon.png").convert("RGBA").resize((200, 200), Image.LANCZOS)
    mask = Image.new("L", (200, 200), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 199, 199], 44, fill=255)
    im.paste(icon, (96, 96), mask)
    d.text((96, 330), "Tap Tap Moo site", font=font(84, True), fill=TEXT)
    d.text((96, 436), "Privacy policy, support and philosophy pages", font=font(36), fill=MUTED)
    d.text((96, 484), "for a calm first-words app.", font=font(36), fill=MUTED)
    x = 96
    for chip in ("Every app language", "Light and dark", "No scripts or cookies", "Static HTML"):
        f = font(26)
        w = d.textlength(chip, font=f)
        d.rounded_rectangle([x, 548, x + w + 40, 596], 24, fill=SURFACE, outline=LINE)
        d.text((x + 20, 560), chip, font=f, fill=ACCENT)
        x += w + 40 + 16
    clean = Image.new("RGB", im.size)
    clean.putdata(list(im.getdata()))
    clean.save(ROOT / "docs/assets/social-preview.png", optimize=True)
    print("wrote docs/assets/social-preview.png")


if __name__ == "__main__":
    main()
