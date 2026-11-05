"""Shared building blocks for page modules."""


def T(ctx, v):
    """Resolve an (en, de) pair for the current page language; plain strings pass through."""
    return ctx.t(*v) if isinstance(v, (tuple, list)) else v


def paras(ctx, items):
    return "".join(f"<p>{T(ctx, p)}</p>" for p in items)


def feature(ctx, img, kicker, title, text, flip=False, caption=None, extra=""):
    """Image beside a text block; flip puts the image on the right. text: list of (en, de) paragraphs or html."""
    cls = " flip" if flip else ""
    k = f'<p class="kicker">{T(ctx, kicker)}</p>' if kicker else ""
    body = paras(ctx, text) if isinstance(text, list) else text
    title = T(ctx, title)
    return (f'<div class="feature{cls}"><div class="feature-media">{ctx.figure(img, T(ctx, caption) if caption else None, alt=title)}</div>'
            f'<div class="feature-text">{k}<h3>{title}</h3>{body}{extra}</div></div>')


def facts(ctx, rows):
    return '<dl class="facts">' + "".join(f"<div><dt>{T(ctx, k)}</dt><dd>{T(ctx, v)}</dd></div>" for k, v in rows) + "</dl>"


def tags(ctx, pairs):
    if not pairs:
        return ""
    return '<p class="tags">' + "".join(f"<span>{T(ctx, p)}</span>" for p in pairs) + "</p>"


def quote(ctx, line, who):
    oq, cq = ctx.t("“", "„"), ctx.t("”", "“")
    return f'<blockquote class="quote"><p>{oq}{T(ctx, line)}{cq}</p><cite>{T(ctx, who)}</cite></blockquote>'


def loops(ctx, rows, cls=""):
    """Numbered steps: rows of (label, text)."""
    items = "".join(f'<li><span class="loop-label">{T(ctx, a)}</span><p>{T(ctx, b)}</p></li>' for a, b in rows)
    return f'<ol class="loops {cls}">{items}</ol>'


def modes(ctx, rows):
    """Small cards: rows of (kicker, title, text)."""
    items = "".join(f'<div class="mode"><p class="kicker">{T(ctx, k)}</p><h3>{T(ctx, h)}</h3><p>{T(ctx, p)}</p></div>'
                    for k, h, p in rows)
    return f'<div class="modes">{items}</div>'


def table(ctx, head, rows, cls=""):
    """head: list of (en, de); rows: lists whose first cell becomes a row header."""
    th = "".join(f"<th scope=\"col\">{T(ctx, h)}</th>" for h in head)
    body = ""
    for r in rows:
        first, rest = r[0], r[1:]
        body += f'<tr><th scope="row">{T(ctx, first)}</th>' + "".join(f"<td>{T(ctx, c)}</td>" for c in rest) + "</tr>"
    return f'<div class="table-wrap"><table class="data-table {cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def catalog(ctx, rows, cls=""):
    """Pictures with an ID, a name and one line. rows: (image_id, name, line)."""
    items = []
    for img, name, line in rows:
        nm = T(ctx, name)
        ln = f"<p>{T(ctx, line)}</p>" if line else ""
        items.append(f'<article class="cat-item">{ctx.figure(img, alt=nm)}'
                     f'<p class="cat-id">{img}</p><h3>{nm}</h3>{ln}</article>')
    return f'<div class="catalog {cls}">{"".join(items)}</div>'


def back(ctx, path, label):
    return f'<p class="back"><a class="text-link" href="{ctx.url(path)}">{T(ctx, label)}</a></p>'


def section(inner, cls=""):
    return f'<section class="wrap section {cls}">{inner}</section>'
