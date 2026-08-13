# exatrines.github.io

Portfolio site for [mirage](https://github.com/exatrines).

- Home: https://exatrines.github.io/
- Plugins: https://exatrines.github.io/dalamud-plugins/
- Splatoon: https://exatrines.github.io/splatoon/
- Support: https://exatrines.github.io/support/

## Layout

| Path | Role |
| --- | --- |
| `content/` | Markdown sources (including home `content/index.md`) |
| `static/` | Source CSS / JS (`styles.css`, `script.js`) |
| `assets/` | Source images |
| `.github/scripts/build.py` | Site generator (CI + local build) |

Optional: if a top-level `files/` directory exists, the build copies it for publishing.

## Editing content

Edit Markdown under `content/` (TOML frontmatter between `+++`).

| Edit | Builds to |
| --- | --- |
| `content/index.md` | site home |
| `content/dalamud-plugins/index.md` | `/dalamud-plugins/` |
| `content/dalamud-plugins/oracle/index.md` | `/dalamud-plugins/oracle/` |
| `content/splatoon/.../index.md` | `/splatoon/.../` |

Useful frontmatter keys: `title`, `description`, `nav` (`dalamud` \| `splatoon` \| `support`), `page_title`, `eyebrow`, `lede`, `breadcrumbs`, `[[changelog]]` (`date`, `title`, `body`), `[[sections]]`, `redirect`, `layout = "home"` (top page).

Home page: `layout = "home"`, plus `brand`, `lede`, `[[links]]`, `[[socials]]`.

Images: `![](/assets/...)`. Fenced code blocks become copyable install boxes.

Edit styles: `static/styles.css`.

## Build

Requires Python 3.11+ (`tomllib`).

```bash
python .github/scripts/build.py
```

GitHub Actions runs the same script and deploys to Pages (repo Settings → Pages → source **GitHub Actions**).
