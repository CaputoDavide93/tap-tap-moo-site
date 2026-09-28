<div align="center">

# 🌤️ Tap Tap Moo site

**The public home, privacy policy, contact and philosophy pages for the Tap Tap Moo app**

![HTML](https://img.shields.io/badge/HTML-static-E34F26?logo=html5&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-hosted-222222?logo=github&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

---

## ✨ Features

| | Page | What it is |
|---|---|---|
| 🏠 | [Home](https://caputodavide93.github.io/tap-tap-moo-site/) | What the app is, in a few lines |
| 🔒 | [Privacy policy](https://caputodavide93.github.io/tap-tap-moo-site/privacy/) | What the app keeps on the device, the voice, the microphone, purchases, children. Linked from the app's settings and the store listings |
| ✉️ | [Contact](https://caputodavide93.github.io/tap-tap-moo-site/contact/) | Support address and common questions. Linked from the app's settings and the store listings |
| 🌱 | [Philosophy](https://caputodavide93.github.io/tap-tap-moo-site/philosophy/) | Why the app exists: the app's own "Why" screen, word for word |
| 🌍 | Every language | Each page in English, Italian (`it/`), Spanish (`es/`) and French (`fr/`), linked to the same page in the others. The app opens the privacy and contact pages in its own language |
| 🌗 | Light and dark | Follows the reader's system setting, in the app's own colours |
| 🚫 | No tracking | No scripts, cookies or analytics |

---

## 🚀 Quick Start

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

GitHub Pages publishes the `main` branch root. The privacy pages must stay true to the app's own `docs/privacy.md`; change both together, in every language. Settings paths and labels are quoted from the app's ARB files (`lib/l10n/app_*.arb`), and the philosophy pages are its `whyTitle` to `whyClosing` copy, in the order the screen shows it.

---

## 📁 Repo structure

```text
tap-tap-moo-site/
├── index.html             # 🏠 home
├── privacy/index.html     # 🔒 privacy policy
├── contact/index.html     # ✉️ contact and support
├── philosophy/index.html  # 🌱 why the app exists
├── it/                    # 🇮🇹 the same pages in Italian
├── es/                    # 🇪🇸 the same pages in Spanish
├── fr/                    # 🇫🇷 the same pages in French
├── assets/
│   ├── site.css           # 🎨 light and dark styles
│   └── mark.svg           # 🌤️ the sun on a cloud (favicon)
├── .nojekyll              # serve files as they are
├── .gitignore
├── README.md
├── SECURITY.md
└── LICENSE
```

---

## 🔒 Security

See [SECURITY.md](SECURITY.md).

---

## 📄 License

[MIT](LICENSE)

---

<p align="center"><sub>Made with ❤️ by <a href="https://github.com/CaputoDavide93">Davide Caputo</a></sub></p>
