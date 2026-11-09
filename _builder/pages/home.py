"""Home page (English and German)."""
from illustration import hero_svg

# The journey, Dais to watchtower. Shared with pages/journey.py so the two never drift apart.
ACTS = [
    (("Act 0", "Akt 0"), ("The Wayward Dais", "Das Wayward Dais"),
     ("The stone hums. The road leads north.", "Der Stein summt. Die Straße führt nach Norden."), ""),
    (("Act 1", "Akt 1"), ("The Watch House", "Das Wachhaus"),
     ("Captain Roland has a task, and not enough people.", "Hauptmann Roland hat eine Aufgabe und zu wenig Leute."), ""),
    (("Act 2", "Akt 2"), ("Choose your path", "Wähle deinen Weg"),
     ("Steel, bow, spring water or flame.", "Stahl, Bogen, Quellwasser oder Flamme."), ""),
    (("Act 3", "Akt 3"), ("The training grounds", "Die Übungsplätze"),
     ("The dummy does not hit back. Yet.", "Die Puppe schlägt nicht zurück. Noch nicht."), ""),
    (("Act 4", "Akt 4"), ("The forest edge", "Der Waldrand"),
     ("Silverleaf grows where the birches thin out.", "Silberblatt wächst dort, wo die Birken lichter werden."), ""),
    (("Act 5", "Akt 5"), ("The pack", "Das Rudel"),
     ("Grey shapes between the beeches.", "Graue Schatten zwischen den Buchen."), ""),
    (("Act 6", "Akt 6"), ("Town life", "Stadtleben"),
     ("Pelts for iron, iron for bracers.", "Felle gegen Eisen, Eisen für Armschienen."), ""),
    (("Act 7", "Akt 7"), ("The Alpha", "Der Alpha"),
     ("Bigger than the stories said.", "Größer, als die Geschichten erzählten."), "boss"),
    (("Act 8", "Akt 8"), ("The road to Frankfurt", "Die Straße nach Frankfurt"),
     ("One merchant's cart, and one already overturned.", "Ein Händlerkarren, und einer, der schon umgestürzt ist."), ""),
    (("Act 9", "Akt 9"), ("Beneath the hill", "Unter dem Hügel"),
     ("Old stone, and something older behind it.", "Alter Stein, und dahinter etwas noch Älteres."), ""),
    (("Act 10", "Akt 10"), ("The Saxenhausen Watchtower", "Die Sachsenhäuser Warte"),
     ("Frankfurt below, and the end of the vertical slice.", "Unten liegt Frankfurt, und hier endet die Vertical Slice."), "end"),
]

JOBS = [
    ("paladin", "Paladin", ("Tank", "Tank"), "PORTRAIT-PALADIN-M", ("Bron, at the training yard", "Bron, auf dem Übungsplatz"),
     ("Shield up. Again.", "Schild hoch. Nochmal.")),
    ("ranger", "Ranger", ("Ranged damage", "Fernkampf-Schaden"), "PORTRAIT-RANGER-F", ("Hagen, at the Hunters' Lodge", "Hagen, an der Jägerhütte"),
     ("Breathe out, then loose.", "Ausatmen, dann loslassen.")),
    ("whitemage", ("White Mage", "Weißmagier"), ("Healer", "Heiler"), "PORTRAIT-WHITEMAGE-F", ("Mira, at the Spring Shrine", "Mira, am Quellschrein"),
     ("Keep them standing. That is the whole job.", "Halt sie auf den Beinen. Das ist die ganze Arbeit.")),
    ("elementalist", ("Elementalist", "Elementarist"), ("Magic damage", "Magie-Schaden"), "PORTRAIT-ELEMENTALIST-M", ("Elwyn, in the tower courtyard", "Elwyn, im Turmhof"),
     ("Fire is easy. Stopping is the hard part.", "Feuer ist leicht. Aufhören ist das Schwere.")),
]


def _T(ctx, v):
    return ctx.t(*v) if isinstance(v, (tuple, list)) else v


def body(ctx):
    u, t = ctx.url, ctx.t

    pillars = [
        ("KA-01", t("A town that feels lived in", "Eine Stadt, in der gelebt wird"),
         t("Half-timbered houses, chimney smoke and firewood under every eave. Hayn is a real place with real work going on.",
           "Fachwerkhäuser, Kaminrauch und Brennholz unter jedem Dachvorsprung. Hayn ist ein echter Ort, in dem echte Arbeit getan wird.")),
        ("VW-04", t("Four guilds, four jobs", "Vier Gilden, vier Jobs"),
         t("Paladin, Ranger, White Mage or Elementalist. Each guild has its own building, banner, trainer and training ground.",
           "Paladin, Ranger, Weißmagier oder Elementarist. Jede Gilde hat ihr eigenes Haus, ihr Banner, ihren Trainer und ihren Übungsplatz.")),
        ("KA-05", t("Fights you can read", "Kämpfe, die man lesen kann"),
         t("Tab-target combat with a hotbar of abilities. Every special attack shows on the ground before it lands.",
           "Tab-Target-Kampf mit einer Leiste voller Fähigkeiten. Jeder Spezialangriff zeigt sich am Boden, bevor er trifft.")),
        ("KA-06", t("A forest that grows older", "Ein Wald, der älter wird"),
         t("The Wolfwood is built in rings. The deeper you go, the darker the trees and the bolder the wolves.",
           "Der Wolfwood ist in Ringen angelegt. Je tiefer du gehst, desto dunkler die Bäume und desto kühner die Wölfe.")),
        ("VW-08", t("The road goes on", "Die Straße geht weiter"),
         t("Guard a merchant's cart, survive an ambush, clear a dungeon under the hill and reach the Saxenhausen Watchtower above Frankfurt.",
           "Begleite einen Händlerkarren, überlebe einen Hinterhalt, säubere ein Verlies unter dem Hügel und erreiche die Sachsenhäuser Warte über Frankfurt.")),
    ]
    pillar_html = "".join(f'<li class="pillar">{ctx.figure(i, alt=n, link=False)}<h3>{n}</h3><p>{d}</p></li>' for i, n, d in pillars)

    job_html = "".join(
        f'<li><a class="job-card job-{key}" href="{u("game/jobs.html")}#{key}">{ctx.figure(img, alt=_T(ctx, name), link=False)}'
        f'<span class="job-body"><span class="job-role">{_T(ctx, role)}</span><span class="job-name">{_T(ctx, name)}</span>'
        f'<span class="job-line">{t("“", "„")}{_T(ctx, line)}{t("”", "“")}</span></span></a></li>'
        for key, name, role, img, where, line in JOBS)

    cast = [
        ("CH-ROLAND", t("Captain Roland", "Hauptmann Roland"), t("The tired border captain", "Der müde Grenzhauptmann")),
        ("CH-HALDOR", "Hermann", t("The smith", "Der Schmied")),
        ("CH-MIRA", "Mira", t("The herbalist", "Die Kräuterkundige")),
        ("CH-ELWYN", "Elwyn", t("The mage in the tower", "Der Magier im Turm")),
    ]
    cast_html = "".join(
        f'<a class="portrait" href="{u("characters/index.html")}">{ctx.figure(i, alt=n, link=False)}'
        f'<span class="portrait-text"><span class="portrait-name">{n}</span><span class="portrait-role">{r}</span></span></a>'
        for i, n, r in cast)

    oq, cq = t("“", "„"), t("”", "“")
    trail_html = "".join(
        f'<li class="waypoint{" wp-" + kind if kind else ""}" style="--i:{k}"><a href="{u("journey/index.html")}#act-{k}">'
        f'<span class="wp-act">{_T(ctx, act)}</span><span class="wp-name">{_T(ctx, name)}</span>'
        f'<span class="wp-line">{oq}{_T(ctx, line)}{cq}</span></a></li>'
        for k, (act, name, line, kind) in enumerate(ACTS))

    facts = [
        (t("Genre", "Genre"), t("Third-person fantasy online MMO", "Fantasy-Online-MMO in der dritten Person")),
        (t("Combat", "Kampf"), t("Tab-target, hotbar, group roles", "Tab-Target, Fähigkeitenleiste, Gruppenrollen")),
        (t("Jobs", "Jobs"), t("Paladin, Ranger, White Mage, Elementalist", "Paladin, Ranger, Weißmagier, Elementarist")),
        (t("Your character", "Deine Figur"), t("Male or female, with different races to choose from later", "Männlich oder weiblich, später auch verschiedene Völker zur Auswahl")),
        (t("Players", "Spieler"), t("Many players at the same time, online in one world", "Viele Spieler gleichzeitig, online in einer Welt")),
        (t("Vertical slice", "Vertical Slice"), t("A small finished part of the MMO, not the full game", "Ein kleiner fertiger Teil des MMOs, nicht das ganze Spiel")),
        (t("Look", "Look"), t("Grounded, semi-realistic fantasy", "Bodenständige, halbrealistische Fantasy")),
        (t("Engine", "Engine"), "Unreal Engine 5"),
        (t("Game framework used", "Verwendetes Spiele-Framework"), "Vertical Third"),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    key = "KEYART"  # the commissioned hero painting only; the drawn stand-in shows until it exists
    hero_cls = "hero"
    if ctx.has(key):
        alt = t("Below the walls of Hayn, a Paladin catches the leaping Alpha on his shield while a White Mage, "
                "an Elementalist and a Ranger hold off the wolf pack coming out of the Wolfwood.",
                "Unter den Mauern von Hayn fängt ein Paladin den springenden Alpha mit seinem Schild ab, während eine "
                "Weißmagierin, ein Elementarist und eine Rangerin das Wolfsrudel aus dem Wolfwood zurückhalten.")
        # The logo is its own transparent layer over the painting's calm sky, so it stays sharp at every size.
        hero_cls = "hero hero-has-art"
        hero_art = (f'<div class="hero-stage"><div class="hero-backdrop" style="{ctx.bg(key)}"></div><div class="hero-art"><img class="hero-painting" src="{ctx.img_src(key, "full")}" alt="{alt}" fetchpriority="high">'
                    + (f'<h1 class="hero-logo"><img src="{ctx.img_src("TITLE-LOGO", "full")}" alt="Destiny of Valendhar" fetchpriority="high"></h1>'
                       if ctx.has("TITLE-LOGO") else
                       '<h1 class="hero-wordmark"><span class="wm-small">Destiny of</span><span class="wm-big">Valendhar</span></h1>')
                    + '</div></div>')
    else:
        alt = t("A traveller at the Wayward Dais looks up the road to the gate of Hayn.",
                "Ein Reisender am Wayward Dais blickt die Straße hinauf zum Tor von Hayn.")
        hero_art = (f'<div class="hero-art">{hero_svg(alt)}'
                    '<h1 class="hero-wordmark"><span class="wm-small">Destiny of</span><span class="wm-big">Valendhar</span></h1></div>')

    return f"""
<section class="{hero_cls}">
  {hero_art}
  <div class="wrap hero-panel">
    <div class="hero-copy">
      <p class="hero-hook">{t("A forest town at the edge of a wood that has grown bold.",
                              "Eine Waldstadt am Rand eines Waldes, der kühn geworden ist.")}</p>
      <p class="hero-sub">{t("Destiny of Valendhar is a fantasy online MMO, played by many players at the same time, with tab-target combat and four job guilds. "
                             "This site shows its vertical slice, not the full game: from the Wayward Dais through Hayn and the Wolfwood to the Saxenhausen Watchtower above Frankfurt.",
                             "Destiny of Valendhar ist ein Fantasy-Online-MMO, das viele Spieler gleichzeitig spielen, mit Tab-Target-Kampf und vier Job-Gilden. "
                             "Diese Seite zeigt seine Vertical Slice, nicht das ganze Spiel: vom Wayward Dais durch Hayn und den Wolfwood bis zur Sachsenhäuser Warte über Frankfurt.")}</p>
      <div class="cta-row">
        <a class="btn btn-gold" href="{u('journey/index.html')}">{t("Walk the journey", "Die Reise antreten")}</a>
        <a class="btn btn-ghost" href="{u('game/jobs.html')}">{t("Meet the four jobs", "Die vier Jobs ansehen")}</a>
      </div>
    </div>
  </div>
</section>

<section class="wrap section intro">
  <div class="intro-text">
    <h2 class="intro-title">{t("Every blade, bow and spell is needed", "Jede Klinge, jeder Bogen und jeder Zauber wird gebraucht")}</h2>
    <p class="big">{t("You arrive as a stranger at the Wayward Dais, an old floating stone on the road outside Hayn, "
                      "a walled town in the king's forest of Three-Oaks, at the edge of the Wolfwood.",
                      "Du kommst als Fremder am Wayward Dais an, einem alten schwebenden Stein an der Straße vor Hayn, "
                      "einer ummauerten Stadt im Königsforst Dreieich, am Rand des Wolfwoods.")}</p>
    <p>{t("Captain Roland is short of people and the pack has started coming out of the trees. You choose one of four job guilds, "
          "learn to fight and gather, thin out the wolves, gear up at the forge and finally face the Alpha in its den. Then the road "
          "north opens: a merchant to protect, an ambush to survive, a dungeon under the hill, and at the end the Saxenhausen Watchtower, with Frankfurt below.",
          "Hauptmann Roland fehlen Leute, und das Rudel kommt neuerdings aus den Bäumen. Du wählst eine von vier Job-Gilden, lernst "
          "zu kämpfen und zu sammeln, dünnst die Wölfe aus, rüstest dich in der Schmiede aus und stellst dich schließlich dem Alpha in "
          "seinem Bau. Dann öffnet sich die Straße nach Norden: ein Händler, den du beschützen musst, ein Hinterhalt, den du überleben "
          "musst, ein Verlies unter dem Hügel und am Ende die Sachsenhäuser Warte, unter der Frankfurt liegt.")}</p>
    <a class="text-link" href="{u('game/index.html')}">{t("Read the full overview", "Zum vollständigen Überblick")}</a>
  </div>
  <dl class="facts">{fact_html}</dl>
</section>

<section class="wrap section">
  <div class="section-head">
    <h2>{t("Four guilds, one town", "Vier Gilden, eine Stadt")}</h2>
    <a class="text-link" href="{u('game/jobs.html')}">{t("All four jobs and their abilities", "Alle vier Jobs und ihre Fähigkeiten")}</a>
  </div>
  <ul class="jobs">{job_html}</ul>
</section>

<section class="palisade">
  <div class="wrap section">
    <h2>{t("What shapes the adventure", "Was das Abenteuer ausmacht")}</h2>
    <ul class="pillars">{pillar_html}</ul>
  </div>
</section>

<section class="wrap section split">
  <div class="split-media">{ctx.figure("KA-03", alt=t("Arrival at the Wayward Dais", "Ankunft am Wayward Dais"))}</div>
  <div class="split-text">
    <p class="kicker">{t("The world", "Die Welt")}</p>
    <h2>{t("Hayn guards the road", "Hayn bewacht die Straße")}</h2>
    <p>{t("Behind an oval stone wall stand steep-roofed half-timbered houses, a market square with a sandstone fountain, "
          "a forge, an inn called the Golden Acorn and a town hall with a slate bell turret. The town lives on timber, and it "
          "keeps watch over the road north to Frankfurt, the capital.",
          "Hinter einer ovalen Steinmauer stehen steilgiebelige Fachwerkhäuser, ein Marktplatz mit einem "
          "Sandsteinbrunnen, eine Schmiede, ein Gasthaus namens Zur Goldenen Eichel und ein Rathaus mit einem schiefergedeckten "
          "Glockentürmchen. Die Stadt lebt vom Holz und wacht über die Straße nach Norden, nach Frankfurt, der Hauptstadt.")}</p>
    <p>{t("North and west the Wolfwood begins: birch and hazel at the edge, tall beeches and old oaks further in, and dark spruce "
          "where the wolf den is.",
          "Im Norden und Westen beginnt der Wolfwood: Birken und Haselsträucher am Rand, hohe Buchen und alte Eichen weiter drinnen "
          "und dunkle Fichten dort, wo der Wolfsbau liegt.")}</p>
    <a class="text-link" href="{u('world/hayn.html')}">{t("Walk through Hayn", "Durch Hayn gehen")}</a>
  </div>
</section>

<section class="cast-band">
  <div class="wrap section">
    <div class="section-head">
      <h2>{t("Who you'll meet", "Wen du triffst")}</h2>
      <a class="text-link" href="{u('characters/index.html')}">{t("All the people of Hayn", "Alle Leute von Hayn")}</a>
    </div>
    <div class="cast">{cast_html}</div>
  </div>
</section>

<section class="trail-band">
  <div class="wrap section">
    <div class="trail-head">
      <div>
        <p class="kicker">{t("The vertical slice", "Die Vertical Slice")}</p>
        <h2>{t("From the Dais to the Saxenhausen Watchtower", "Vom Dais bis zur Sachsenhäuser Warte")}</h2>
        <p>{t("Eleven stops on one road. Each one teaches something new, from the first step to a boss fight and a dungeon.",
              "Elf Stationen auf einer Straße. Jede bringt dir etwas Neues bei, vom ersten Schritt bis zum Bosskampf und zum Verlies.")}</p>
      </div>
      {ctx.figure("TD-04", alt=t("Painted map of the Wolfwood", "Gemalte Karte des Wolfwoods"))}
    </div>
    <ol class="trail">{trail_html}</ol>
  </div>
</section>

<section class="story-band">
  <div class="wrap section story-inner">
    <h2>{t("A notice in the Watch House", "Ein Aushang im Wachhaus")}</h2>
    <p class="story-note">{t("Pinned beside the map of the region", "Neben der Karte der Gegend angeheftet")}</p>
    <p class="story-quote">{oq}{t("Three sheep at the mill, a woodcutter's dog, and now tracks inside the north pasture. The pack "
                              "has never come this close. Anyone who can hold a weapon, report to me.",
                              "Drei Schafe an der Mühle, der Hund eines Holzfällers, und jetzt Spuren auf der Nordweide. So nah "
                              "war das Rudel noch nie. Wer eine Waffe halten kann, meldet sich bei mir.")}{cq}<br>
      <em>{t("Captain Roland", "Hauptmann Roland")}</em></p>
    <a class="btn btn-ghost" href="{u('journey/quests.html')}">{t("See the quest chain", "Zur Questreihe")}</a>
  </div>
</section>
"""


PAGES = {
    "index.html": dict(
        title=("Home", "Start"),
        description=("Destiny of Valendhar: a fantasy online MMO. This site shows its vertical slice, which runs from the forest town of Hayn "
                     "through the Wolfwood to the Saxenhausen Watchtower above Frankfurt.",
                     "Destiny of Valendhar: ein Fantasy-Online-MMO. Diese Seite zeigt seine Vertical Slice, die von der Waldstadt Hayn "
                     "durch den Wolfwood bis zur Sachsenhäuser Warte über Frankfurt führt."),
        body=body,
        custom_header=True,
        no_pager=True,
        og=["KEYART-SHARE", "KEYART", "KA-03"],
    )
}
