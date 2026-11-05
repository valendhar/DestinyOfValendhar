"""A hand-drawn SVG stand-in for the key art, used until KEYART (or KA-03) exists.

It shows the arrival view from the design doc: the Wayward Dais in the foreground, the road north to the
South Gate, the palisade, and the four landmark silhouettes (town-hall bell turret, inn, Elwyn's tower,
watchtower) under a late-afternoon autumn sky, with the Wolfwood behind.
"""
import random

W, H = 1600, 900


def _spruces(rng, y0, y1, n, scale, color):
    out = []
    for _ in range(n):
        x = rng.uniform(-40, W + 40)
        base = rng.uniform(y0, y1)
        h = rng.uniform(70, 140) * scale
        w = h * rng.uniform(.32, .42)
        out.append(f'<path d="M{x:.0f} {base - h:.0f} L{x + w / 2:.0f} {base:.0f} L{x - w / 2:.0f} {base:.0f}Z"/>')
    return f'<g fill="{color}">{"".join(out)}</g>'


def _house(x, y, w, h, roof, beam):
    """A gable-front half-timbered house: plaster body, dark beams, steep roof."""
    top = y - h
    peak = top - roof
    beams = (f'<path d="M{x} {top + h * .45}h{w} M{x + w / 3:.0f} {top}v{h} M{x + 2 * w / 3:.0f} {top}v{h} '
             f'M{x} {top}l{w / 3:.0f} {h * .45:.0f} M{x + w} {top}l{-w / 3:.0f} {h * .45:.0f}" stroke="{beam}" stroke-width="3" fill="none"/>')
    win = f'<rect x="{x + w * .4:.0f}" y="{top + h * .6:.0f}" width="{w * .2:.0f}" height="{h * .18:.0f}" fill="#F2C46E" opacity=".85"/>'
    return (f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="#D9CDB2"/>{beams}{win}'
            f'<path d="M{x - 6} {top + 2} L{x + w / 2:.0f} {peak} L{x + w + 6} {top + 2}Z" fill="#7A3A26"/>'
            f'<path d="M{x + w / 2:.0f} {peak} L{x + w + 6} {top + 2} L{x + w / 2 + 6:.0f} {top + 2}Z" fill="#5E2B1C"/>')


def hero_svg(title):
    rng = random.Random(7)
    parts = [
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">',
        '<defs>'
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B2733"/>'
        '<stop offset=".45" stop-color="#6B5A4E"/><stop offset=".72" stop-color="#D08A45"/><stop offset="1" stop-color="#F2C46E"/></linearGradient>'
        '<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF1C9"/>'
        '<stop offset=".25" stop-color="#F5C46A" stop-opacity=".9"/><stop offset="1" stop-color="#F2C46E" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="glyph" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#8FD3EA" stop-opacity=".55"/>'
        '<stop offset="1" stop-color="#8FD3EA" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B4A2C"/><stop offset="1" stop-color="#121B14"/></linearGradient>'
        '<linearGradient id="road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8C7A5C"/><stop offset="1" stop-color="#4A3F30"/></linearGradient>'
        '</defs>',
        f'<rect width="{W}" height="{H}" fill="url(#sky)"/>',
        '<circle cx="330" cy="470" r="260" fill="url(#sun)"/>',
        # far hills and the Wolfwood
        '<path d="M0 470 C200 400 380 430 560 390 S900 360 1100 395 S1450 370 1600 410 V900 H0Z" fill="#3A4142" opacity=".75"/>',
        _spruces(rng, 430, 520, 140, .8, "#25302A"),
        '<path d="M0 520 C300 480 600 500 800 485 S1300 470 1600 505 V900 H0Z" fill="#1E2A22"/>',
        _spruces(rng, 500, 560, 90, 1.0, "#18221C"),
    ]
    # village on its slope, climbing toward the north (up the picture)
    village = []
    houses = [(560, 590, 46, 44, 46, "#1F1A15"), (612, 585, 40, 40, 42, "#7A2E22"), (655, 592, 44, 46, 44, "#1F1A15"),
              (900, 588, 44, 42, 44, "#7A2E22"), (948, 584, 40, 46, 42, "#1F1A15"), (994, 590, 46, 40, 46, "#7A2E22"),
              (700, 570, 38, 36, 38, "#7A2E22"), (860, 568, 38, 38, 38, "#1F1A15"), (1040, 596, 40, 40, 40, "#1F1A15"),
              (520, 598, 38, 36, 38, "#7A2E22")]
    for x, y, w, h, r, beam in houses:
        village.append(_house(x, y, w, h, r, beam))
    # town hall with its slate bell turret (centre, north of the square)
    village.append('<rect x="745" y="512" width="110" height="58" fill="#D9CDB2"/>'
                   '<path d="M745 540h110 M772 512v58 M800 512v58 M828 512v58" stroke="#7A2E22" stroke-width="3"/>'
                   '<path d="M738 514 L800 470 L862 514Z" fill="#4E5660"/>'
                   '<rect x="792" y="438" width="16" height="36" fill="#4E5660"/><path d="M788 440 L800 400 L812 440Z" fill="#3D444C"/>')
    # inn, three storeys (east)
    village.append(_house(1080, 600, 70, 80, 60, "#7A2E22"))
    # Elwyn's tower (west): round stone, timber top room, faint red glow
    village.append('<rect x="440" y="470" width="44" height="140" fill="#8D8A80"/>'
                   '<rect x="434" y="440" width="56" height="34" fill="#D9CDB2"/><path d="M434 456h56 M452 440v34 M472 440v34" stroke="#1F1A15" stroke-width="3"/>'
                   '<path d="M428 442 L462 380 L496 442Z" fill="#3D444C"/><rect x="456" y="450" width="12" height="14" fill="#E0623E"/>')
    # watchtower (north-east): four posts, braces, shingled lookout
    village.append('<path d="M1196 610 L1206 430 M1244 610 L1234 430 M1206 470 L1234 520 M1234 470 L1206 520 M1204 540 L1236 590 M1236 540 L1204 590" stroke="#2A221A" stroke-width="6"/>'
                   '<rect x="1194" y="404" width="52" height="30" fill="#4A3A2A"/><path d="M1186 406 L1220 370 L1254 406Z" fill="#3A2C20"/>'
                   '<rect x="1214" y="412" width="12" height="10" fill="#F2C46E"/>')
    parts.append(f'<g>{"".join(village)}</g>')
    # chimney smoke
    parts.append('<g fill="none" stroke="#E8DCC8" stroke-width="10" stroke-linecap="round" opacity=".18">'
                 '<path d="M640 548 C630 510 660 490 640 450 S660 400 650 360"/><path d="M972 540 C985 500 960 480 978 440 S960 400 975 360"/></g>')
    # palisade: sharpened logs on a fieldstone base, with the South Gate in the middle
    logs = []
    x = 380
    while x < 1240:
        if 760 < x < 840:
            x += 14
            continue
        h = rng.uniform(26, 40)
        logs.append(f'<path d="M{x:.0f} 640 V{640 - h:.0f} L{x + 6:.0f} {640 - h - 9:.0f} L{x + 12:.0f} {640 - h:.0f} V640Z"/>')
        x += 13
    parts.append(f'<rect x="372" y="636" width="876" height="14" fill="#5A5650"/><g fill="#4A3826">{"".join(logs)}</g>')
    parts.append('<rect x="764" y="568" width="72" height="82" fill="#7C766C"/><rect x="760" y="560" width="80" height="30" fill="#D9CDB2"/>'
                 '<path d="M760 575h80 M786 560v30 M814 560v30" stroke="#1F1A15" stroke-width="3"/>'
                 '<path d="M752 562 L800 528 L848 562Z" fill="#7A3A26"/>'
                 '<path d="M782 650 V620 A18 18 0 0 1 818 620 V650Z" fill="#F2C46E" opacity=".75"/>')
    # fields, the road and the Dais
    parts.append('<path d="M0 650 C400 630 1200 630 1600 655 V900 H0Z" fill="url(#ground)"/>')
    parts.append('<g stroke="#5C6A3A" stroke-width="2" opacity=".55">'
                 + "".join(f'<path d="M{80 + i * 70} 900 L{560 + i * 22} 660"/>' for i in range(6))
                 + "".join(f'<path d="M{1110 + i * 80} 900 L{870 + i * 30} 660"/>' for i in range(6)) + '</g>')
    parts.append('<path d="M786 650 L814 650 L980 900 L620 900Z" fill="url(#road)" opacity=".9"/>'
                 '<path d="M800 652 L800 900" stroke="#5C6A3A" stroke-width="10" opacity=".5"/>')
    parts.append('<ellipse cx="800" cy="842" rx="300" ry="62" fill="url(#glyph)"/>'
                 '<ellipse cx="800" cy="840" rx="250" ry="44" fill="#6E6B66"/><ellipse cx="800" cy="834" rx="250" ry="44" fill="#8A877F"/>'
                 '<ellipse cx="800" cy="834" rx="214" ry="34" fill="none" stroke="#8FD3EA" stroke-width="3" stroke-dasharray="10 14" opacity=".85"/>'
                 '<ellipse cx="800" cy="760" rx="120" ry="20" fill="url(#glyph)"/>'
                 '<path d="M770 742 L792 600 L826 594 L842 740 L806 756Z" fill="#6E6B66"/>'
                 '<path d="M806 756 L842 740 L826 594 L812 598Z" fill="#55524D"/>'
                 '<path d="M800 620 L810 660 L798 700 L812 735" stroke="#8FD3EA" stroke-width="2.5" fill="none"/>')
    # a lone adventurer on the dais, seen from behind
    parts.append('<g fill="#141A17"><path d="M690 828 L684 790 Q690 770 700 768 Q710 770 716 790 L710 828Z"/>'
                 '<circle cx="700" cy="760" r="9"/><path d="M706 772 L726 742" stroke="#141A17" stroke-width="3"/></g>')
    parts.append('</svg>')
    return "".join(parts)
