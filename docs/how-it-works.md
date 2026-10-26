# 🧠 How it works

The site is plain files. There is no build step, no script and no framework.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg">
  <img src="assets/architecture-light.svg" width="100%" alt="The app's settings and the store listings link to this site; a parent's browser fetches static HTML and CSS from GitHub Pages.">
</picture>

## Pages and URLs

Four pages exist in each language: home, `privacy/`, `contact/` and
`philosophy/`. English is at the root and every other language is a folder
named by its code (`it/`, `es/`, `fr/`, `de/`, `pt/`, `nl/`, `pl/`). The app's
Settings and the store listings link to the privacy and contact pages, so these
URLs do not change.

## Languages

Each page carries a language row linking the same page in every language, with
`hreflang` attributes so search engines pair them. The app opens the privacy
and contact pages in its own language. Settings paths and labels in the
privacy and contact pages are quoted from the app's own strings, and the
philosophy pages are the app's "Why" screen.

## Styles

`assets/site.css` holds the colours as variables. The light set follows the
app's theme, and a `prefers-color-scheme: dark` block swaps them, so the page
follows the reader's system setting. The layout is one column up to 720 px.

## Hosting

GitHub Pages serves the `main` branch root. `.nojekyll` makes it serve files as
they are. GitHub may keep standard server logs; the site says so in its
footer and in the privacy policy.

## Checks

`make check` runs `tools/check_site.py` (pages, links, no scripts, one address)
and `tools/gen_diagram.py --check` (the diagram files match the generator).
CI runs the same command on every pull request.
