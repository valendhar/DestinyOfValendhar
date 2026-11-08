"""Concept Art: every design and modeling sheet, page by page, with a "coming soon" box for each one that isn't made yet.

The sheet list comes from _builder/concept_sheets.json, which the prompt generator (gen_order.py) writes, so the pages always match the
prompt file. A sheet appears as soon as its image is saved in _builder/images/sheets/<folder>/ and the site is built.
"""
import json
import re
from pathlib import Path

from components import section
from concept_de import NAMES, SUFFIX

SHEETS = json.loads((Path(__file__).resolve().parent.parent / "concept_sheets.json").read_text(encoding="utf-8"))
BY_ID = {e["id"]: e for e in SHEETS}
EXTRA = re.compile(r"-(E1|E2|D)$")
SHOW_EN = {"CC5 1: four-view character": "model sheet"}
MISSING_DE = set()

JOBS = [("PALADIN", ("Paladin", "Paladin")), ("RANGER", ("Ranger", "Waldläufer")), ("WHITEMAGE", ("White Mage", "Weißmagier")),
        ("ELEMENTALIST", ("Elementalist", "Elementalist"))]


def label(ctx, e):
    """A sheet's caption in the page language."""
    name = e["name"]
    m = EXTRA.search(e["id"])
    if m and e["id"][:m.start()] in BY_ID:
        name = f'{BY_ID[e["id"][:m.start()]]["name"]}, {name}'
    if e["folder"] == "kit" and e["id"].startswith("KP-"):
        return name.replace("_", " ")
    for suf in sorted(SUFFIX, key=len, reverse=True):
        if name.endswith(", " + suf):
            base = name[: -len(suf) - 2]
            if ctx.lang == "de":
                if base not in NAMES:
                    MISSING_DE.add(base)
                return f"{NAMES.get(base, base)}, {SUFFIX[suf]}"
            return f"{base}, {SHOW_EN.get(suf, suf)}"
    if ctx.lang == "de":
        if name not in NAMES:
            MISSING_DE.add(name)
        return NAMES.get(name, name)
    return name


def sheet_grid(ctx, entries, tall=False):
    """Made sheets first, then a box for each sheet still to come."""
    made = [e for e in entries if ctx.has(e["id"])]
    todo = [e for e in entries if not ctx.has(e["id"])]
    figs = "".join(ctx.figure(e["id"], label(ctx, e), swap=False, note=ctx.t("Coming soon", "Demnächst")) for e in made + todo)
    return f'<div class="gallery gallery-sheets{" gallery-tall" if tall else ""}">{figs}</div>'


def block(ctx, title, intro, entries, tall=False, first=False):
    if not entries:
        return ""
    made = sum(1 for e in entries if ctx.has(e["id"]))
    count = ctx.t(f"{made} of {len(entries)} made", f"{made} von {len(entries)} fertig")
    p = f'<p class="sheet-intro">{ctx.t(*intro)}</p>' if intro else ""
    return (f'<div class="sheet-block{" first" if first else ""}"><div class="sheet-head"><h2>{ctx.t(*title)}</h2>'
            f'<span class="sheet-count">{count}</span></div>{p}{sheet_grid(ctx, entries, tall)}</div>')


def pick(folder, pattern=None, exclude=None):
    out = [e for e in SHEETS if e["folder"] == folder]
    if pattern:
        out = [e for e in out if re.search(pattern, e["id"])]
    if exclude:
        out = [e for e in out if not re.search(exclude, e["id"])]
    return out


def fixed(ctx, title, intro, items, tall=False, first=False):
    """A block of images that aren't in the prompt file, such as the hero line-ups: (id, (en, de))."""
    made = sum(1 for i, _ in items if ctx.has(i))
    count = ctx.t(f"{made} of {len(items)} made", f"{made} von {len(items)} fertig")
    figs = "".join(ctx.figure(i, ctx.t(*c), swap=False, note=ctx.t("Coming soon", "Demnächst")) for i, c in items)
    p = f'<p class="sheet-intro">{ctx.t(*intro)}</p>' if intro else ""
    return (f'<div class="sheet-block{" first" if first else ""}"><div class="sheet-head"><h2>{ctx.t(*title)}</h2>'
            f'<span class="sheet-count">{count}</span></div>{p}'
            f'<div class="gallery gallery-sheets{" gallery-tall" if tall else ""}">{figs}</div></div>')


# ---------------------------------------------------------------- pages
def heroes(ctx):
    sex = {"M": ("male", "männlich"), "F": ("female", "weiblich")}
    portraits = [(f"PORTRAIT-{j}-{g}", (f"{n[0]}, {sex[g][0]}", f"{n[1]}, {sex[g][1]}")) for j, n in JOBS for g in "MF"]
    full = [(f"FULL_{j}_{g}", (f"{n[0]}, {sex[g][0]}", f"{n[1]}, {sex[g][1]}")) for j, n in JOBS for g in "MF"]
    return section(
        fixed(ctx, ("The line-ups", "Die Aufstellungen"), ("Every job can be played as a man or a woman.", "Jeder Job lässt sich als Mann oder Frau spielen."),
              [("PC-GROUP-M", ("The four jobs, men", "Die vier Jobs, Männer")), ("PC-GROUP-F", ("The four jobs, women", "Die vier Jobs, Frauen"))], first=True)
        + fixed(ctx, ("Portraits", "Porträts"), None, portraits, tall=True)
        + fixed(ctx, ("Full body", "Ganzer Körper"), ("The source of truth for each hero's face, build and outfit.",
                                                     "Die verbindliche Vorlage für Gesicht, Statur und Ausrüstung jedes Helden."), full, tall=True)
        + block(ctx, ("Starter outfits", "Startausrüstung"), None, pick("heroes", r"-K$"), tall=True)
        + block(ctx, ("Model sheets", "Modellblätter"), ("Four straight views of each hero, used to build the character in Character Creator 5.",
                                                        "Vier gerade Ansichten jedes Helden, als Vorlage für den Bau der Figur in Character Creator 5."),
                pick("heroes", r"-C1$")))


def people(ctx):
    return section(
        block(ctx, ("The named townsfolk", "Die Leute mit Namen"), ("A portrait and a full-body image for everyone the heroes meet by name.",
                                                                     "Ein Porträt und ein Bild in voller Größe für jeden, den die Helden mit Namen kennenlernen."),
              pick("people", r"^CH-.*-(PT|FULL)$"), tall=True, first=True)
        + block(ctx, ("Townsfolk", "Stadtbewohner"), ("Line-ups for the people who fill the streets, the market and the inn.",
                                                     "Gruppenbilder für die Leute auf den Gassen, auf dem Markt und im Gasthaus."), pick("people", r"^NP-"))
        + block(ctx, ("Model sheets", "Modellblätter"), None, pick("people", r"-C1$")))


def creatures(ctx):
    return section(
        block(ctx, ("Wolves and the Alpha", "Wölfe und der Alpha"), ("Design sheets, straight views, head studies and attack poses.",
                                                                       "Designblätter, gerade Ansichten, Kopfstudien und Angriffsposen."),
              pick("creatures", r"^EN-0[124]-"), first=True)
        + block(ctx, ("Beasts of the forest", "Tiere des Waldes"), None, pick("creatures", r"^(EN-03-|CR-)"))
        + block(ctx, ("Road bandits", "Straßenräuber"), None, pick("creatures", r"^EN-05"), tall=True)
        + block(ctx, ("Beneath the hill", "Unter dem Hügel"), ("The barrow's dead and the Warden who guards them.",
                                                              "Die Toten im Hügelgrab und der Hüter, der über sie wacht."), pick("creatures", r"^EN-0[67]"), tall=True)
        + block(ctx, ("Farm animals", "Hoftiere"), None, pick("creatures", r"^AN-")))


def buildings(ctx):
    return section(
        block(ctx, ("Landmarks and houses", "Wahrzeichen und Häuser"), ("Each building of Hayn, with straight elevations and construction details "
                                                                         "for the larger ones.", "Jedes Gebäude von Hayn, für die größeren mit geraden "
                                                                         "Ansichten und Baudetails."), pick("buildings", r"^BL-"), first=True)
        + block(ctx, ("Bridges and signposts", "Brücken und Wegweiser"), None, pick("buildings", r"^ST-")))


def props(ctx):
    return section(
        block(ctx, ("Street and yard", "Gasse und Hof"), None, pick("props", r"^EX-"), first=True)
        + block(ctx, ("The market", "Der Markt"), None, pick("props", r"^MK-"))
        + block(ctx, ("Workshops", "Werkstätten"), None, pick("props", r"^WS-"))
        + block(ctx, ("Lights", "Licht"), None, pick("props", r"^LT-"))
        + block(ctx, ("Furniture and interiors", "Möbel und Innenräume"), None, pick("props", r"^IN-"))
        + block(ctx, ("Items", "Gegenstände"), ("Loot, crafting materials, potions and food.", "Beute, Handwerksmaterial, Tränke und Speisen."),
                pick("props", r"^IM-")))


def wolfwood(ctx):
    return section(
        block(ctx, ("Places in the forest", "Orte im Wald"), None, pick("wolfwood", r"^FS-"), first=True)
        + block(ctx, ("Trees", "Bäume"), None, pick("wolfwood", r"^FO-"))
        + block(ctx, ("Plants", "Pflanzen"), None, pick("wolfwood", r"^PL-"))
        + block(ctx, ("Rocks and deadwood", "Felsen und Totholz"), None, pick("wolfwood", r"^RK-"))
        + block(ctx, ("The barrow", "Das Hügelgrab"), ("The dungeon beneath the hill: its halls, its bridge and the boss chamber.",
                                                       "Der Dungeon unter dem Hügel: seine Hallen, seine Brücke und die Kammer des Endgegners."), pick("wolfwood", r"^DK-")))


def kit(ctx):
    return section(
        block(ctx, ("Materials", "Materialien"), ("Seamless surfaces for plaster, timber, stone and roofs. Each one tiles across a whole wall.",
                                                  "Nahtlose Oberflächen für Putz, Holz, Stein und Dächer. Jede wiederholt sich über eine ganze Wand."),
              pick("kit", r"^KM-"), first=True)
        + block(ctx, ("Trim sheets", "Trim Sheets"), ("Carved and edged strips that dress beams, stone and roof edges.",
                                                      "Geschnitzte und gekantete Streifen für Balken, Stein und Dachkanten."), pick("kit", r"^KX-"))
        + block(ctx, ("How the kit fits together", "Wie das Baukastensystem zusammenpasst"), ("Every house is built from the same reusable pieces: "
                                                                                              "sills, posts, braces, panels, windows and roofs.",
                                                                                              "Jedes Haus entsteht aus denselben wiederverwendbaren Teilen: "
                                                                                              "Schwellen, Pfosten, Streben, Gefache, Fenster und Dächer."),
                pick("kit", r"^KE-"))
        + block(ctx, ("Kit pieces", "Bauteile"), ("The detailed single pieces: doors, carved brackets, chimney caps and more.",
                                                  "Die detaillierten Einzelteile: Türen, geschnitzte Knaggen, Schornsteinköpfe und mehr."), pick("kit", r"^KP-")))


def gear(ctx):
    return section(
        block(ctx, ("Cosmetic sets", "Kosmetische Sets"), ("Outfits a player can wear over their gear, shown without a body.",
                                                          "Kleidung, die man über der Ausrüstung tragen kann, ohne Körper gezeigt."), pick("gear"), first=True))


SUB = [
    ("concept/heroes.html", ("Heroes", "Helden"), "PC-GROUP-M", heroes, "heroes"),
    ("concept/people.html", ("People of Hayn", "Die Leute von Hayn"), "NP-02", people, "people"),
    ("concept/creatures.html", ("Creatures & Enemies", "Kreaturen & Gegner"), "EN-04-S", creatures, "creatures"),
    ("concept/buildings.html", ("Buildings & Landmarks", "Gebäude & Wahrzeichen"), "BL-30", buildings, "buildings"),
    ("concept/props.html", ("Props & Interiors", "Requisiten & Innenräume"), None, props, "props"),
    ("concept/wolfwood.html", ("Wolfwood & Barrow", "Wolfwood & Hügelgrab"), "DK-02", wolfwood, "wolfwood"),
    ("concept/kit.html", ("Modular Kit", "Baukasten"), "KX-TIMBER", kit, "kit"),
    ("concept/gear.html", ("Gear & Costumes", "Ausrüstung & Kostüme"), None, gear, "gear"),
]
LEDE = {
    "heroes": ("The four jobs, each as a man and a woman.", "Die vier Jobs, jeweils als Mann und als Frau."),
    "people": ("The townsfolk of Hayn.", "Die Leute von Hayn."),
    "creatures": ("Everything that hunts in the Wolfwood, waits on the road or sleeps beneath the hill.",
                  "Alles, was im Wolfwood jagt, an der Straße lauert oder unter dem Hügel schläft."),
    "buildings": ("The town, building by building.", "Die Stadt, Haus für Haus."),
    "props": ("What fills the streets, the workshops and the rooms.", "Was die Gassen, Werkstätten und Zimmer füllt."),
    "wolfwood": ("The forest, its stones and the barrow beneath the hill.", "Der Wald, seine Steine und das Hügelgrab unter dem Hügel."),
    "kit": ("The reusable pieces every building in Hayn is made from.", "Die wiederverwendbaren Teile, aus denen jedes Gebäude in Hayn besteht."),
    "gear": ("Outfits for the cosmetic wardrobe.", "Kleidung für die kosmetische Garderobe."),
}


def counts(ctx, folder):
    entries = [e for e in SHEETS if e["folder"] == folder]
    extra = []
    if folder == "heroes":
        extra = ["PC-GROUP-M", "PC-GROUP-F"] + [f"PORTRAIT-{j}-{g}" for j, _ in JOBS for g in "MF"] + [f"FULL_{j}_{g}" for j, _ in JOBS for g in "MF"]
    made = sum(1 for e in entries if ctx.has(e["id"])) + sum(1 for i in extra if ctx.has(i))
    return made, len(entries) + len(extra)


def overview(ctx):
    t = ctx.t
    cards = []
    for path, title, cover, _, folder in SUB:
        made, total = counts(ctx, folder)
        firsts = [e["id"] for e in SHEETS if e["folder"] == folder and ctx.has(e["id"])]
        img = cover if cover and ctx.has(cover) else (firsts[0] if firsts else (cover or "CONCEPT-" + folder.upper()))
        fig = ctx.figure(img, alt=ctx.t(*title), swap=False, link=False, note=t("Coming soon", "Demnächst"))
        cards.append(f'<a class="concept-card" href="{ctx.url(path)}">{fig}<span class="concept-card-text"><span class="concept-card-title">{ctx.t(*title)}</span>'
                     f'<span class="concept-card-lede">{ctx.t(*LEDE[folder])}</span>'
                     f'<span class="sheet-count">{t(f"{made} of {total} made", f"{made} von {total} fertig")}</span></span></a>')
    return section(f"""
<div class="intro" style="margin-bottom:56px">
  <div class="prose">
    <p class="big">{t("The working drawings behind the game: every hero, townsperson, creature, building and prop, drawn before it is built.",
                      "Die Arbeitszeichnungen hinter dem Spiel: jeder Held, jeder Stadtbewohner, jede Kreatur, jedes Gebäude und jedes "
                      "Requisit, gezeichnet, bevor es gebaut wird.")}</p>
    <p>{t("People are drawn as polished, semi-realistic 3D game characters. The world, its buildings and its props are painted concept art. "
          "Many sheets show an object from several sides, because they guide the 3D models. Empty frames are sheets still to come.",
          "Figuren entstehen als polierte, halbrealistische 3D-Spielfiguren. Die Welt, ihre Gebäude und Requisiten sind gemalte "
          "Konzeptkunst. Viele Blätter zeigen ein Objekt von mehreren Seiten, weil sie als Vorlage für die 3D-Modelle dienen. Leere "
          "Rahmen sind Blätter, die noch kommen.")}</p>
  </div>
</div>
<div class="concept-cards">{"".join(cards)}</div>""")


PAGES = {
    "concept/index.html": dict(
        title=("Concept Art", "Konzeptkunst"), kicker=("Concept Art", "Konzeptkunst"),
        lede=("Design and modeling sheets for everything in the vertical slice.", "Design- und Modellblätter für alles in der Vertical Slice."),
        banner=["BE-01", "KA-01"], body=overview),
}
for _path, _title, _cover, _fn, _folder in SUB:
    PAGES[_path] = dict(title=_title, kicker=("Concept Art", "Konzeptkunst"), lede=LEDE[_folder], banner=None, body=_fn)
