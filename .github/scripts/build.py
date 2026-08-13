# -*- coding: utf-8 -*-
"""
Build the static site into dist/.

  python .github/scripts/build.py

Maps:
  content/index.md       → dist/index.html
  content/foo/index.md   → dist/foo/index.html
  content/foo/bar.md     → dist/foo/bar/index.html

Also copies static/styles.css, static/script.js, and assets/ into dist/.
"""
from __future__ import annotations

import html
import re
import shutil
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
STATIC = ROOT / "static"
ASSETS = ROOT / "assets"
FILES = ROOT / "files"
SITE_URL = "https://exatrines.github.io"
DISCORD_INVITE = "https://discord.gg/gRfxXNZWMs"

GITHUB_SVG = """<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
              <path
                fill="currentColor"
                d="M12 2C6.48 2 2 6.58 2 12.26c0 4.52 2.87 8.35 6.84 9.7.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.37-3.37-1.37-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.06 1.53 1.06.9 1.57 2.36 1.12 2.94.86.09-.67.35-1.12.63-1.38-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.7 0 0 .84-.27 2.75 1.05A9.3 9.3 0 0 1 12 6.84c.85 0 1.71.12 2.51.34 1.91-1.32 2.75-1.05 2.75-1.05.55 1.4.2 2.44.1 2.7.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.95.68 1.92 0 1.38-.01 2.5-.01 2.84 0 .26.18.59.69.48A10.03 10.03 0 0 0 22 12.26C22 6.58 17.52 2 12 2Z"
              />
            </svg>"""

DISCORD_SVG = """<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
              <path
                fill="currentColor"
                d="M19.27 5.33A16.4 16.4 0 0 0 15.38 4l-.2.35c1.67.46 2.5 1.14 2.5 1.14a11 11 0 0 0-4.55-1.16 11.4 11.4 0 0 0-4.56 1.16s.87-.72 2.64-1.18L10.94 4a16.1 16.1 0 0 0-3.98 1.33C3.65 9.44 2.98 13.45 3.2 17.4a16.6 16.6 0 0 0 5.05 2.56l.65-.99a10.7 10.7 0 0 1-1.62-.78l.4-.3a12 12 0 0 0 10.63 0l.4.3c-.52.32-1.07.57-1.64.78l.65.99a16.5 16.5 0 0 0 5.06-2.56c.35-4.5-.6-8.46-3.51-12.07ZM9.7 14.83c-.9 0-1.63-.84-1.63-1.87 0-1.03.72-1.87 1.63-1.87.9 0 1.64.84 1.63 1.87 0 1.03-.73 1.87-1.63 1.87Zm4.6 0c-.9 0-1.63-.84-1.63-1.87 0-1.03.72-1.87 1.63-1.87.9 0 1.63.84 1.63 1.87 0 1.03-.73 1.87-1.63 1.87Z"
              />
            </svg>"""


# ---------------------------------------------------------------------------
# Markdown → HTML
# ---------------------------------------------------------------------------

def make_heading_id(label: str, used: dict[str, int]) -> str:
    """Stable-ish fragment id for headings (Japanese-friendly)."""
    slug = re.sub(r"\s+", "-", label.strip())
    slug = re.sub(r"[^\w\-一-龥ぁ-んァ-ヶー＋+]", "", slug, flags=re.UNICODE)
    slug = slug.strip("-") or "section"
    n = used.get(slug, 0)
    used[slug] = n + 1
    return slug if n == 0 else f"{slug}-{n + 1}"


def md_to_html(md: str, depth: int) -> tuple[str, list[tuple[str, str]]]:
    """Convert Markdown used on this site into HTML fragments.

    Returns (html, h2_toc) where h2_toc is [(id, plain_title), ...].
    """
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    h2_toc: list[tuple[str, str]] = []
    id_used: dict[str, int] = {}
    i = 0
    in_code = False
    code_buf: list[str] = []
    list_type: str | None = None
    asset_prefix = "../" * depth

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    def flush_code() -> None:
        nonlocal in_code, code_buf
        if not in_code:
            return
        code = "\n".join(code_buf).rstrip("\n")
        out.append(
            '<div class="install-box md-code">'
            f'<div class="repo-scroll"><code class="repo-url">{html.escape(code)}</code></div>'
            '<button type="button" class="copy-btn" data-copy aria-label="コピー">'
            '<i class="fa-regular fa-copy" aria-hidden="true"></i></button></div>'
        )
        code_buf = []
        in_code = False

    def rewrite_asset(src: str) -> str:
        src = src.strip()
        if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
            return src
        if src.startswith("/"):
            return asset_prefix + src.lstrip("/")
        if src.startswith("../") or src.startswith("./"):
            return src
        return asset_prefix + src.lstrip("/")

    def process_inline(raw: str) -> str:
        tokens: list[tuple] = []

        def push_img(m: re.Match) -> str:
            tokens.append(("IMG", m.group(1), m.group(2)))
            return f"\x00T{len(tokens) - 1}\x00"

        def push_link(m: re.Match) -> str:
            tokens.append(("A", m.group(1), m.group(2)))
            return f"\x00T{len(tokens) - 1}\x00"

        raw = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", push_img, raw)
        raw = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", push_link, raw)
        raw = html.escape(raw)
        raw = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", raw)
        raw = re.sub(r"`([^`]+)`", r'<code class="inline-code">\1</code>', raw)

        def restore(m: re.Match) -> str:
            kind, a, b = tokens[int(m.group(1))]
            if kind == "IMG":
                href = rewrite_asset(b)
                return (
                    f'<figure class="md-figure">'
                    f'<img src="{html.escape(href)}" alt="{html.escape(a)}" loading="lazy" />'
                    f"</figure>"
                )
            href = rewrite_asset(b) if not b.startswith(("http", "mailto:", "#")) else b
            text = html.escape(a)
            if href.startswith("http"):
                return (
                    f'<a class="inline-link" href="{html.escape(href)}" '
                    f'target="_blank" rel="noreferrer">{text}</a>'
                )
            return f'<a class="inline-link" href="{html.escape(href)}">{text}</a>'

        return re.sub(r"\x00T(\d+)\x00", restore, raw)

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                flush_code()
            else:
                close_list()
                in_code = True
                code_buf = []
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if not line.strip():
            close_list()
            i += 1
            continue

        if line.startswith("# "):
            close_list()
            i += 1
            continue
        if line.startswith("## "):
            close_list()
            title = line[3:].strip()
            hid = make_heading_id(title, id_used)
            h2_toc.append((hid, title))
            out.append(
                f'<h2 id="{html.escape(hid)}">{process_inline(title)}</h2>'
            )
            i += 1
            continue
        if line.startswith("### "):
            close_list()
            out.append(f"<h3>{process_inline(line[4:].strip())}</h3>")
            i += 1
            continue
        if line.startswith("#### "):
            close_list()
            out.append(f"<h4>{process_inline(line[5:].strip())}</h4>")
            i += 1
            continue
        if line.startswith("##### "):
            close_list()
            out.append(f"<h5>{process_inline(line[6:].strip())}</h5>")
            i += 1
            continue

        m = re.match(r"^(?P<mark>[-*+]|\d+\.)\s+(?P<body>.+)$", line)
        if m:
            kind = "ul" if m.group("mark") in "-*+" else "ol"
            if list_type != kind:
                close_list()
                list_type = kind
                out.append(f"<{kind}>")
            out.append(f"<li>{process_inline(m.group('body'))}</li>")
            i += 1
            continue

        close_list()
        para = [line]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if (
                not nxt.strip()
                or nxt.startswith("#")
                or nxt.startswith("```")
                or re.match(r"^[-*+]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
            ):
                break
            para.append(nxt)
            j += 1
        text = " ".join(p.strip() for p in para)
        out.append(f"<p>{process_inline(text)}</p>")
        i = j
        continue

    if in_code:
        flush_code()
    close_list()
    return "\n".join(out), h2_toc


def script_toc_html(items: list[tuple[str, str]]) -> str:
    """In-page TOC for script titles (## headings)."""
    if len(items) < 2:
        return ""
    lis = "\n".join(
        f'<li><a href="#{html.escape(hid)}">{html.escape(title)}</a></li>'
        for hid, title in items
    )
    return (
        '<nav class="script-toc reveal" aria-label="スクリプトの目次">'
        '<p class="script-toc-label">スクリプト</p>'
        f'<ol class="script-toc-list">\n{lis}\n</ol>'
        "</nav>"
    )


def wants_script_toc(meta: dict, og_path: str) -> bool:
    """Script pages with auto TOC; override with frontmatter toc = true/false."""
    if "toc" in meta:
        return bool(meta.get("toc"))
    path = f"/{og_path}"
    return (
        "/presets/dmad/scripts/" in path
        or "/presets/top/scripts/" in path
    )



# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------

def breadcrumbs_html(items: list[dict] | list[list] | None) -> str:
    if not items:
        return ""
    parts: list[str] = []
    n = len(items)
    for i, item in enumerate(items):
        if isinstance(item, dict):
            label = str(item.get("label", ""))
            href = str(item.get("href", "") or "")
        else:
            label = str(item[0])
            href = str(item[1]) if len(item) > 1 else ""
        esc = html.escape(label)
        if href and i < n - 1:
            parts.append(f'<a href="{html.escape(href)}">{esc}</a>')
        else:
            parts.append(f"<span>{esc}</span>")
    return (
        '<nav class="breadcrumbs reveal" aria-label="breadcrumb">'
        + '<span class="bc-sep"> / </span>'.join(parts)
        + "</nav>"
    )


def support_links_html(items: list[dict]) -> str:
    """Two (or more) support destinations as linked tiles."""
    cards: list[str] = []
    for it in items:
        title = html.escape(str(it.get("title", "")))
        href = html.escape(str(it.get("href", "#")))
        note = it.get("note") or it.get("meta") or ""
        badge = it.get("badge") or ""
        desc = it.get("description") or it.get("body") or ""
        cta = html.escape(str(it.get("cta") or "応援する"))
        variant = str(it.get("variant") or "").strip().lower()
        extra_cls = f" support-card--{html.escape(variant)}" if variant else ""
        badge_html = (
            f'<span class="support-card-badge">{html.escape(str(badge))}</span>' if badge else ""
        )
        note_html = (
            f'<span class="support-card-note">{html.escape(str(note))}</span>' if note else ""
        )
        desc_html = (
            f'<span class="support-card-desc">{html.escape(str(desc))}</span>' if desc else ""
        )
        cards.append(
            f'<a class="support-card{extra_cls} reveal" href="{href}" '
            f'target="_blank" rel="noreferrer">'
            f"{badge_html}"
            f'<span class="support-card-title">{title}</span>'
            f"{desc_html}"
            f"{note_html}"
            f'<span class="support-card-cta">{cta}'
            f'<span class="arrow" aria-hidden="true">↗</span></span>'
            f"</a>"
        )
    return f'<div class="support-links">\n' + "\n".join(cards) + "\n</div>"


def product_list_html(items: list[dict], compact: bool = True) -> str:
    lis: list[str] = []
    for it in items:
        title = html.escape(str(it.get("title", "")))
        meta = it.get("meta")
        href = html.escape(str(it.get("href", "#")))
        desc = it.get("description") or it.get("body")
        icon = it.get("icon")
        fallback = it.get("icon_fallback")
        external = bool(it.get("external")) or href.startswith("http")
        target = ' target="_blank" rel="noreferrer"' if external else ""

        icon_html = ""
        if icon:
            icon_html = (
                f'<img class="product-icon" src="{html.escape(str(icon))}" alt="" width="40" height="40" />'
            )
        elif fallback:
            icon_html = (
                f'<span class="product-icon product-icon-fallback" aria-hidden="true">'
                f"{html.escape(str(fallback))}</span>"
            )

        meta_html = f'<span class="meta">{html.escape(str(meta))}</span>' if meta else ""
        desc_html = f"<p>{html.escape(str(desc))}</p>" if desc else ""
        product_cls = "product product-compact" if compact and not desc and not icon else "product"

        lis.append(
            f'<li class="reveal">'
            f'<a class="{product_cls}" href="{href}"{target}>'
            f"{icon_html}"
            f'<div class="product-body">'
            f'<div class="product-title"><strong>{title}</strong>{meta_html}</div>'
            f"{desc_html}"
            f"</div>"
            f'<span class="arrow" aria-hidden="true">↗</span>'
            f"</a></li>"
        )
    return f'<ul class="product-list">\n' + "\n".join(lis) + "\n</ul>"


def sections_html(sections: list[dict], depth: int) -> str:
    chunks: list[str] = []
    for sec in sections:
        heading = html.escape(str(sec.get("heading", "")))
        sid = sec.get("id")
        id_attr = f' id="{html.escape(str(sid))}"' if sid else ""
        install = sec.get("install")
        items = sec.get("items") or []
        compact = bool(sec.get("compact", True))

        fixed_items = []
        for it in items:
            it2 = dict(it)
            if it2.get("icon") and not str(it2["icon"]).startswith("http"):
                icon = str(it2["icon"]).lstrip("/")
                it2["icon"] = ("../" * depth) + icon
            fixed_items.append(it2)

        chunks.append(f'<section class="list-section"{id_attr}>')
        if heading:
            chunks.append(f'<div class="section-head reveal"><h2>{heading}</h2></div>')
        if install:
            chunks.append(
                f'<div class="install-box reveal">'
                f'<div class="repo-scroll"><code class="repo-url">{html.escape(str(install))}</code></div>'
                f'<button type="button" class="copy-btn" data-copy aria-label="コピー">'
                f'<i class="fa-regular fa-copy" aria-hidden="true"></i></button></div>'
            )
        if fixed_items:
            if str(sec.get("kind", "")) == "support":
                chunks.append(support_links_html(fixed_items))
            else:
                chunks.append(product_list_html(fixed_items, compact=compact))
        chunks.append("</section>")
    return "\n".join(chunks)


def changelog_html(entries: list[dict], depth: int) -> str:
    """Expandable update log: summary shows date + title; body is Markdown.

    When there are more than LIMIT items, only the first ones are shown until
    the user expands via the “さらに表示” control (script.js).
    """
    if not entries:
        return ""
    limit = 3
    items: list[str] = []
    for entry in entries:
        # Date only (drop any trailing time-of-day)
        date_raw = str(entry.get("date", "")).strip()
        date_raw = re.sub(r"\s+\d{1,2}:\d{2}(?::\d{2})?\s*$", "", date_raw).strip()
        title = html.escape(str(entry.get("title", "")))
        body_md = str(entry.get("body") or entry.get("details") or "").strip()
        body_html = md_to_html(body_md, depth)[0] if body_md else ""
        body_block = (
            f'<div class="changelog-body doc-content">\n{body_html}\n</div>' if body_html else ""
        )
        date_html = (
            f'<span class="changelog-date">{html.escape(date_raw)}</span>' if date_raw else ""
        )
        no_date = " changelog-item-nodate" if not date_raw else ""
        items.append(
            f'<details class="changelog-item{no_date} reveal">'
            f"<summary>"
            f"{date_html}"
            f'<span class="changelog-title">{title}</span>'
            f"</summary>"
            f"{body_block}"
            f"</details>"
        )

    more = ""
    if len(items) > limit:
        rest = len(items) - limit
        more = (
            f'<button type="button" class="changelog-more" data-changelog-more>'
            f"さらに表示（残り {rest} 件）"
            f"</button>"
        )

    return (
        '<section class="list-section" id="changelog">'
        '<div class="section-head reveal"><h2>更新履歴</h2></div>'
        f'<div class="changelog" data-changelog-limit="{limit}">\n'
        f'{"".join(items)}\n{more}\n</div>'
        "</section>"
    )


def head_html(
    *,
    title: str,
    description: str,
    og_path: str,
    prefix: str,
    og_image: str | None = None,
    extra_css: bool = True,
) -> str:
    og_url = f"{SITE_URL}/" if not og_path else f"{SITE_URL}/{og_path}"
    og_img = ""
    if og_image:
        og_img = f'\n    <meta property="og:image" content="{html.escape(str(og_image))}" />'
    fa = ""
    if extra_css:
        fa = """
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />"""
    return f"""    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="{html.escape(description)}" />
    <meta name="theme-color" content="#faf9f8" />
    <meta property="og:title" content="{html.escape(title)}" />
    <meta property="og:description" content="{html.escape(description)}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{html.escape(og_url)}" />{og_img}
    <title>{html.escape(title)}</title>
    <link rel="icon" href="{prefix}assets/avatar.jpg" type="image/jpeg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;1,400&family=M+PLUS+Rounded+1c:wght@500;700;800&family=Noto+Sans+JP:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />{fa}
    <link rel="stylesheet" href="{prefix}styles.css" />"""


def atmosphere_html() -> str:
    return """    <div class="atmosphere" aria-hidden="true">
      <div class="glow glow-a"></div>
      <div class="glow glow-b"></div>
      <div class="grain"></div>
    </div>"""


def socials_html(socials: list[dict] | None) -> str:
    if not socials:
        return ""
    parts: list[str] = []
    for s in socials:
        kind = str(s.get("kind", "")).lower()
        if kind == "github":
            href = html.escape(str(s.get("href", "https://github.com/exatrines")))
            aria = html.escape(str(s.get("aria", "GitHub")))
            parts.append(
                f'<a href="{href}" target="_blank" rel="noreferrer" aria-label="{aria}">'
                f"{GITHUB_SVG}</a>"
            )
        elif kind == "discord":
            href = html.escape(str(s.get("href") or DISCORD_INVITE))
            aria = html.escape(str(s.get("aria", "Discord")))
            label = s.get("label")
            label_html = f"<span>{html.escape(str(label))}</span>" if label else ""
            parts.append(
                f'<a class="discord-link" href="{href}" target="_blank" rel="noreferrer" aria-label="{aria}">'
                f"{DISCORD_SVG}{label_html}</a>"
            )
        else:
            href = html.escape(str(s.get("href", "#")))
            label = html.escape(str(s.get("label", s.get("aria", "link"))))
            external = href.startswith("http")
            target = ' target="_blank" rel="noreferrer"' if external else ""
            parts.append(f'<a href="{href}"{target}>{label}</a>')
    return '<div class="socials">\n          ' + "\n          ".join(parts) + "\n        </div>"


def parent_back_link(
    breadcrumbs: list[dict] | list[list] | None,
    prefix: str,
) -> tuple[str, str]:
    """One site level up via last non-empty breadcrumb href; else home."""
    ancestors: list[tuple[str, str]] = []
    for item in breadcrumbs or []:
        if isinstance(item, dict):
            label = str(item.get("label", "") or "")
            href = str(item.get("href", "") or "")
        else:
            label = str(item[0])
            href = str(item[1]) if len(item) > 1 else ""
        if href:
            ancestors.append((label, href))
    if not ancestors:
        return prefix, "← mirage"
    label, href = ancestors[-1]
    return href, f"← {label}"


def default_footer_end_html(
    *,
    footer_href: str | None = None,
    footer_label: str | None = None,
    include_discord: bool = True,
) -> str:
    """Right side of content footers: optional follow link + Discord invite."""
    bits: list[str] = []
    if footer_href:
        bits.append(
            f'<a class="follow" href="{html.escape(str(footer_href))}" target="_blank" rel="noreferrer">'
            f'{html.escape(str(footer_label or "GitHub"))} <span aria-hidden="true">↗</span></a>'
        )
    if include_discord:
        bits.append(
            f'<a class="discord-link" href="{html.escape(DISCORD_INVITE)}" '
            f'target="_blank" rel="noreferrer" aria-label="Discord">'
            f"{DISCORD_SVG}</a>"
        )
    if not bits:
        return ""
    return '<div class="footer-end">\n          ' + "\n          ".join(bits) + "\n        </div>"


def render_home(meta: dict, body_md: str, *, og_path: str) -> str:
    title = str(meta.get("title", "mirage"))
    description = str(meta.get("description", ""))
    brand = str(meta.get("brand") or meta.get("page_title") or "mirage")
    lede = meta.get("lede")
    og_image = meta.get("og_image")
    links = meta.get("links") or []
    socials = meta.get("socials") or []

    ctas: list[str] = []
    for link in links:
        label = html.escape(str(link.get("label", "")))
        href = html.escape(str(link.get("href", "#")))
        ctas.append(
            f'<a class="home-link" href="{href}">'
            f"<span>{label}</span>"
            f'<span class="arrow" aria-hidden="true">↗</span>'
            f"</a>"
        )

    md_html = md_to_html(body_md.strip(), 0)[0] if body_md.strip() else ""
    extra = f"\n          {md_html}" if md_html else ""

    lede_html = (
        f'<p class="lede reveal" style="--d: 100ms">{html.escape(str(lede))}</p>'
        if lede
        else ""
    )
    cta_html = (
        f'<div class="cta-row reveal" style="--d: 160ms">\n            '
        + "\n            ".join(ctas)
        + "\n          </div>"
        if ctas
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
{head_html(title=title, description=description, og_path=og_path, prefix="", og_image=og_image, extra_css=False)}
  </head>
  <body class="page-home">
{atmosphere_html()}

    <div class="page page-home-inner">
      <header class="site-header reveal">
        <a class="brand-mark" href="./" aria-label="mirage home">
          <img src="assets/avatar.jpg" alt="" width="36" height="36" />
        </a>
        <nav class="nav">
          <a href="dalamud-plugins/">Dalamud Plugins</a>
          <a href="splatoon/">Splatoon</a>
          <a href="support/">Support</a>
          <a href="https://github.com/exatrines" target="_blank" rel="noreferrer">GitHub</a>
        </nav>
      </header>

      <main class="home-main">
        <section class="intro intro-home">
          <h1 class="brand reveal" style="--d: 40ms">{html.escape(brand)}</h1>
          {lede_html}
          {cta_html}{extra}
        </section>
      </main>

      <footer class="site-footer site-footer-home reveal" style="--d: 220ms">
        {socials_html(socials)}
      </footer>
    </div>

    <script src="script.js"></script>
  </body>
</html>
"""


def render_page(
    meta: dict,
    body_md: str,
    *,
    depth: int,
    og_path: str,
) -> str:
    layout = str(meta.get("layout", "page"))
    if layout == "home":
        return render_home(meta, body_md, og_path=og_path)

    title = str(meta.get("title", "mirage"))
    description = str(meta.get("description", ""))
    nav = str(meta.get("nav", "splatoon"))
    eyebrow = meta.get("eyebrow")
    page_title = meta.get("page_title") or meta.get("heading")
    lede = meta.get("lede")
    footer_href = meta.get("footer_href")
    footer_label = meta.get("footer_label")
    breadcrumbs = meta.get("breadcrumbs")
    sections = meta.get("sections")
    changelog = meta.get("changelog")
    og_image = meta.get("og_image")

    prefix = "../" * depth

    dalamud_cur = ' aria-current="page"' if nav == "dalamud" else ""
    splatoon_cur = ' aria-current="page"' if nav == "splatoon" else ""
    support_cur = ' aria-current="page"' if nav == "support" else ""

    if footer_href is None and nav == "dalamud":
        footer_href = "https://github.com/exatrines/DalamudPlugins"
        footer_label = footer_label or "Repo on GitHub"
    # Splatoon pages: no extra footer link (this site is the canonical source).

    body_parts: list[str] = []
    bc = breadcrumbs_html(breadcrumbs)
    if bc:
        body_parts.append(bc)

    if page_title or eyebrow or lede:
        body_parts.append('<section class="page-hero">')
        if eyebrow:
            body_parts.append(f'<p class="eyebrow reveal">{html.escape(str(eyebrow))}</p>')
        if page_title:
            body_parts.append(f'<h1 class="page-title reveal">{html.escape(str(page_title))}</h1>')
        if lede:
            body_parts.append(f'<p class="lede reveal">{html.escape(str(lede))}</p>')
        body_parts.append("</section>")

    # Order: optional changelog first, then product sections, then freeform MD
    if changelog:
        body_parts.append(changelog_html(changelog, depth))

    if sections:
        body_parts.append(sections_html(sections, depth))

    md_html = ""
    h2_toc: list[tuple[str, str]] = []
    if body_md.strip():
        md_html, h2_toc = md_to_html(body_md.strip(), depth)
    if md_html:
        parts_inner = ""
        if wants_script_toc(meta, og_path):
            parts_inner += script_toc_html(h2_toc)
        parts_inner += md_html
        body_parts.append(f'<article class="doc-content reveal">\n{parts_inner}\n</article>')

    body = "\n".join(body_parts)

    back_href, back_label = parent_back_link(breadcrumbs, prefix)

    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
{head_html(title=title, description=description, og_path=og_path, prefix=prefix, og_image=og_image)}
  </head>
  <body>
{atmosphere_html()}
    <div class="page">
      <header class="site-header reveal">
        <a class="brand-mark" href="{prefix}" aria-label="mirage home">
          <img src="{prefix}assets/avatar.jpg" alt="" width="36" height="36" />
        </a>
        <nav class="nav">
          <a href="{prefix}dalamud-plugins/"{dalamud_cur}>Dalamud Plugins</a>
          <a href="{prefix}splatoon/"{splatoon_cur}>Splatoon</a>
          <a href="{prefix}support/"{support_cur}>Support</a>
          <a href="https://github.com/exatrines" target="_blank" rel="noreferrer">GitHub</a>
        </nav>
      </header>
      <main>
{body}
      </main>
      <footer class="site-footer reveal">
        <a class="back-link" href="{html.escape(back_href)}">{html.escape(back_label)}</a>
        {default_footer_end_html(footer_href=footer_href, footer_label=footer_label)}
      </footer>
    </div>
    <script src="{prefix}script.js"></script>
  </body>
</html>
"""


# ---------------------------------------------------------------------------
# File resolution
# ---------------------------------------------------------------------------

def parse_content_file(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    text = text.lstrip("\ufeff")
    if text.startswith("+++"):
        end = text.find("\n+++", 3)
        if end == -1:
            raise ValueError(f"Unclosed frontmatter in {path}")
        meta_raw = text[3:end].strip()
        body = text[end + 4 :].lstrip("\n")
        meta = tomllib.loads(meta_raw) if meta_raw else {}
        return meta, body
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end == -1:
            raise ValueError(f"Unclosed YAML frontmatter in {path} (use +++ TOML)")
        raise ValueError(f"{path}: use +++ TOML frontmatter (not YAML)")
    return {}, text


def content_path_to_output(rel: Path) -> Path:
    """content/a/b.md → a/b/index.html ; content/a/index.md → a/index.html"""
    parts = list(rel.parts)
    if not parts:
        raise ValueError(rel)
    if parts[-1] == "index.md":
        return Path(*parts[:-1], "index.html") if len(parts) > 1 else Path("index.html")
    stem = Path(parts[-1]).stem
    return Path(*parts[:-1], stem, "index.html")


def depth_of(out_rel: Path) -> int:
    return len(out_rel.parent.parts)


def og_path_of(out_rel: Path) -> str:
    parent = out_rel.parent.as_posix()
    return "" if parent == "." else parent + "/"


def redirect_page(target: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="refresh" content="0; url={html.escape(target)}" />
    <link rel="canonical" href="{SITE_URL}/{html.escape(target.lstrip('./'))}" />
    <title>Redirecting…</title>
    <script>location.replace({target!r});</script>
  </head>
  <body>
    <p><a href="{html.escape(target)}">移動します</a>。</p>
  </body>
</html>
"""


def build_one(src: Path) -> Path:
    rel = src.relative_to(CONTENT)
    meta, body = parse_content_file(src)
    out_rel = content_path_to_output(rel)

    if meta.get("redirect"):
        out = DIST / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(redirect_page(str(meta["redirect"])), encoding="utf-8", newline="\n")
        return out_rel

    depth = depth_of(out_rel)
    out = DIST / out_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    html_out = render_page(meta, body, depth=depth, og_path=og_path_of(out_rel))
    out.write_text(html_out, encoding="utf-8", newline="\n")
    return out_rel


def copy_tree(src: Path, dest: Path, label: str) -> str:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return label


def copy_static() -> list[str]:
    """Copy CSS, JS, assets, and downloadable files into dist/."""
    copied: list[str] = []
    DIST.mkdir(parents=True, exist_ok=True)

    for name in ("styles.css", "script.js"):
        src = STATIC / name
        if not src.is_file():
            raise SystemExit(f"Missing static file: {src}")
        dest = DIST / name
        shutil.copy2(src, dest)
        copied.append(name)

    if not ASSETS.is_dir():
        raise SystemExit(f"Missing assets dir: {ASSETS}")
    copied.append(copy_tree(ASSETS, DIST / "assets", "assets/"))

    if FILES.is_dir():
        copied.append(copy_tree(FILES, DIST / "files", "files/"))
    return copied


def clean_dist() -> None:
    """Clear dist contents without removing the dist directory itself.

    Removing the directory fails on Windows when a preview server has
    cwd inside dist/ (PermissionError WinError 32).
    """
    DIST.mkdir(parents=True, exist_ok=True)
    for child in list(DIST.iterdir()):
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def build_all() -> list[Path]:
    if not CONTENT.is_dir():
        raise SystemExit(f"Missing content dir: {CONTENT}")
    clean_dist()
    for name in copy_static():
        print("copied", name)

    written: list[Path] = []
    for src in sorted(CONTENT.rglob("*.md")):
        if any(p.startswith("_") for p in src.relative_to(CONTENT).parts):
            continue
        rel = build_one(src)
        written.append(rel)
        print("built", rel.as_posix())
    return written


def main() -> None:
    written = build_all()
    print(f"done: {len(written)} pages → {DIST.relative_to(ROOT).as_posix()}/")


if __name__ == "__main__":
    main()
