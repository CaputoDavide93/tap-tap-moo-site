<div align="center">

<img src="docs/assets/brand/icon.png" width="96" alt="The Tap Tap Moo app icon: a cow with a bell, chewing a blade of grass, on a soft yellow sparkle background">

# 🐄 Tap Tap Moo site

**Privacy policy, support and philosophy pages for the Tap Tap Moo first-words app, in every language the app speaks**

![HTML](https://img.shields.io/badge/HTML-static-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-light_and_dark-1572B6?logo=css3&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-hosted-222222?logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
[![CI](https://github.com/CaputoDavide93/tap-tap-moo-site/actions/workflows/ci.yml/badge.svg)](https://github.com/CaputoDavide93/tap-tap-moo-site/actions/workflows/ci.yml)

</div>

---

## ✨ Features

This is the website for **Tap Tap Moo**, a calm first-words game for babies and toddlers on iPhone, iPad and Android. The app opens the privacy policy and the support page in its own language from its Settings, and the store listings link to them, so those addresses stay fixed.

The privacy page says what stays on the device, what the microphone is for, that nothing is sold, and how to delete everything. It exists in English, Italian, Spanish, French, German, Brazilian Portuguese, Dutch and Polish, and each page links to its twin in the other languages.

Live at [caputodavide93.github.io/tap-tap-moo-site](https://caputodavide93.github.io/tap-tap-moo-site/).

| | Page | What it is |
|---|---|---|
| 🏠 | [Home](https://caputodavide93.github.io/tap-tap-moo-site/) | What the app is, in a few lines |
| 🔒 | [Privacy policy](https://caputodavide93.github.io/tap-tap-moo-site/privacy/) | What the app keeps on the device, the voice, the microphone, payments (none: nothing is sold), children. Linked from the app's Settings and the store listings |
| ✉️ | [Contact](https://caputodavide93.github.io/tap-tap-moo-site/contact/) | Support address and common questions. Linked from the app's Settings and the store listings |
| 🌱 | [Philosophy](https://caputodavide93.github.io/tap-tap-moo-site/philosophy/) | Why the app exists, in the app's own words |
| 🌍 | Every language | English, Italian (`it/`), Spanish (`es/`), French (`fr/`), German (`de/`), Brazilian Portuguese (`pt/`), Dutch (`nl/`) and Polish (`pl/`). The app opens the privacy and contact pages in its own language |
| 🌗 | Light and dark | Follows the reader's system setting, in the app's own colours |
| 🚫 | No tracking | No scripts, forms, cookies or analytics, and a check that fails if one appears |
| 🧪 | Self-checking | `make check` verifies every page exists in every language, every local link resolves, and the support address is the only one |

The pages are plain HTML and CSS: no scripts, forms, cookies or analytics, and a check fails the build if one appears. Every language is a separate hand-written file, so a change to the policy means editing all of them. GitHub Pages may keep standard server logs for visitors, and the privacy page says so.

---

## 📸 Screenshots

Taken from the served site by `make screenshots` (Chromium, 900 px wide). The
contact page is left out because it shows the support address.

<table>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/home-dark.png">
  <img src="docs/assets/screenshots/home-light.png" alt="The Tap Tap Moo home page: the headline 'Tap the sky, and say it together.' and a card of six short facts about the app">
</picture>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/privacy-dark.png">
  <img src="docs/assets/screenshots/privacy-light.png" alt="The privacy policy page with an 'In short' card: no account, no servers, no analytics, no AI, nothing leaves the device">
</picture>
</td>
</tr>
<tr>
<td>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/philosophy-dark.png">
  <img src="docs/assets/screenshots/philosophy-light.png" alt="The philosophy page: why Tap Tap Moo exists, with four cards on what it offers">
</picture>
</td>
<td>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/home-italian-dark.png">
  <img src="docs/assets/screenshots/home-italian-light.png" alt="The same home page in Italian, with the language row at the top">
</picture>
</td>
</tr>
</table>

---

## 🗺️ Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/architecture-dark.svg">
  <img src="docs/assets/architecture-light.svg" width="100%" alt="The app's settings and the store listings link to this site; a parent's browser fetches static HTML and CSS from GitHub Pages.">
</picture>

How it is built is in [docs/how-it-works.md](docs/how-it-works.md).

---

## 🚀 Quick Start

You need Python 3 and a browser. There is no build step, and `make check` uses only the standard library.

```bash
git clone https://github.com/CaputoDavide93/tap-tap-moo-site.git
cd tap-tap-moo-site
make serve     # preview at http://localhost:8000
make check     # the same checks CI runs
```

Editing a page, retaking the images and what each check covers are in [docs/setup.md](docs/setup.md).

---

## 🧪 Tested on

| Environment | Status |
|---|---|
| Chromium (Playwright 1.64.1) on macOS, light and dark | ✅ Screenshots and layout checked |
| `make check` on Python 3.12 (CI, Ubuntu) | ✅ Runs on every pull request |
| Safari and Firefox | ❔ Unverified: plain HTML and CSS, not tried here |
| Screen readers | ❔ Unverified |

---

## 📁 Repo structure

```text
tap-tap-moo-site/
├── index.html             # 🏠 home
├── privacy/index.html     # 🔒 privacy policy
├── contact/index.html     # ✉️ contact and support
├── philosophy/index.html  # 🌱 why the app exists
├── it/                    # 🌍 the same four pages in Italian
├── es/                    # 🌍 the same four pages in Spanish
├── fr/                    # 🌍 the same four pages in French
├── de/                    # 🌍 the same four pages in German
├── pt/                    # 🌍 the same four pages in Portuguese
├── nl/                    # 🌍 the same four pages in Dutch
├── pl/                    # 🌍 the same four pages in Polish
├── assets/                # 🎨 site.css and the app icon in three sizes
├── docs/                  # 📚 setup, how it works, FAQ, troubleshooting
│   └── assets/            # 🖼️ diagrams, screenshots, brand icon, social preview
├── tools/                 # 🔧 check_site.py, gen_diagram.py, brand/, screenshots/
├── .github/workflows/     # 🤖 ci.yml runs make check
├── Makefile               # ⚙️ check, serve, diagram, screenshots, social
├── llms.txt               # 🤖 the site in one plain-text page for search tools
├── AGENTS.md              # 🧭 contributor and agent notes
├── CONTRIBUTING.md  SECURITY.md  LICENSE
├── .nojekyll              # serve files as they are
└── .gitignore
```

---

## 📦 Deployment

GitHub Pages serves the root of `main`, so a merged pull request is the release.
CI runs `make check` on every pull request and on every push to `main`. The
privacy pages must stay true to the app's own privacy document: change both
together, in every language. Settings paths and labels are quoted from the app's
ARB files (`lib/l10n/app_*.arb`), and the philosophy pages are its `whyTitle` to
`whyClosing` copy, in the order the screen shows it.

---

## 🛠️ Troubleshooting

[docs/troubleshooting.md](docs/troubleshooting.md) lists symptoms and fixes:
a page that 404s on GitHub Pages, a language row that is out of step, a failing
`make check`. Common questions are in [docs/faq.md](docs/faq.md). The full
index is [docs/README.md](docs/README.md).

---

## 🔒 Security

See [SECURITY.md](SECURITY.md).

---

## 🤝 Contributing

Found a wrong sentence, a broken link or a page that reads badly on your
device? [Open an issue](https://github.com/CaputoDavide93/tap-tap-moo-site/issues/new)
with the page address, your browser and operating system with versions, and a
screenshot if it is a layout problem. Reports from browsers and devices not
listed under Tested on are especially useful. Details are in
[CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)

---

<p align="center"><sub>Made with ❤️ by <a href="https://github.com/CaputoDavide93">Davide Caputo</a></sub></p>
