"""The Game: overview, combat, the four jobs, town life."""
from components import back, facts, feature, loops, modes, quote, section, table, tags


def overview(ctx):
    t = ctx.t
    intro = section(f"""
<div class="intro">
  <div class="prose">
    <p class="big">{t("Destiny of Valendhar is a third-person fantasy online MMO set in the world of Valendhar, played by many players at the same time. You pick a job, "
                      "join its guild, and fight with a hotbar of abilities against enemies you select with a target key, the way "
                      "classic MMOs play.",
                      "Destiny of Valendhar ist ein Fantasy-Online-MMO in der dritten Person, das viele Spieler gleichzeitig spielen, angesiedelt in der Welt "
                      "Valendhar. Du wählst einen Job, trittst seiner Gilde bei und kämpfst mit einer Leiste voller Fähigkeiten gegen "
                      "Gegner, die du per Zieltaste auswählst, so wie klassische MMOs sich spielen.")}</p>
    <p>{t("This site shows the game's vertical slice, not the full game. A vertical slice is one small part built to finished quality "
          "first: here, one town, one forest, one road and one dungeon, from the first step to the last boss. "
          "It is the part being built now, and the measure for everything after it.",
          "Diese Seite zeigt die Vertical Slice des Spiels, nicht das ganze Spiel. Eine Vertical Slice ist ein kleiner Teil, der zuerst "
          "in fertiger Qualität entsteht: hier eine Stadt, ein Wald, eine Straße und ein Verlies, vom ersten "
          "Schritt bis zum letzten Boss. Es ist der Teil, der gerade entsteht, und der Maßstab für alles, "
          "was danach kommt.")}</p>
  </div>
  {facts(ctx, [
      (("Genre", "Genre"), ("Fantasy online MMO, third person", "Fantasy-Online-MMO, dritte Person")),
      (("Camera", "Kamera"), ("Orbit camera behind your character", "Orbit-Kamera hinter deiner Figur")),
      (("Combat", "Kampf"), ("Tab-target with a 10-slot hotbar", "Tab-Target mit einer Leiste aus 10 Plätzen")),
      (("Party roles", "Gruppenrollen"), ("Tank, healer, damage", "Tank, Heiler, Schaden")),
      (("Your character", "Deine Figur"), ("Male or female, with different races to choose from later", "Männlich oder weiblich, später auch verschiedene Völker zur Auswahl")),
      (("Vertical slice", "Vertical Slice"), ("A small finished part of the MMO, not the full game", "Ein kleiner fertiger Teil des MMOs, nicht das ganze Spiel")),
      (("Players", "Spieler"), ("Many players at the same time, online in one world", "Viele Spieler gleichzeitig, online in einer Welt")),
      (("Platform", "Plattform"), ("PC first", "Zuerst für PC")),
      (("Engine", "Engine"), ("Unreal Engine 5", "Unreal Engine 5")),
  ])}
</div>""")

    pillars = section(f"""
<h2>{t("What the game stands on", "Worauf das Spiel steht")}</h2>
{feature(ctx, "KA-01", ("Pillar 1", "Säule 1"), ("A grounded world", "Eine bodenständige Welt"), [
    ("Valendhar looks semi-realistic: real proportions, honest materials, painterly light. The towns read like a late-medieval "
     "Germany that never was. Magic is rare in town and grows stronger out in the forest and at the old monuments.",
     "Valendhar sieht halbrealistisch aus: echte Proportionen, ehrliche Materialien, malerisches Licht. Die Städte wirken wie ein "
     "spätmittelalterliches Deutschland, das es nie gab. Magie ist in der Stadt selten und wird draußen im Wald und an den alten Monumenten stärker.")])}
{feature(ctx, "VW-04", ("Pillar 2", "Säule 2"), ("Jobs, not classes on a menu", "Jobs statt Klassen aus einem Menü"), [
    ("You choose your job in the world, by walking into a guild and talking to its trainer. Each guild is a real building with "
     "its own banner, people and training ground.",
     "Du wählst deinen Job in der Welt, indem du eine Gilde betrittst und mit ihrem Trainer sprichst. Jede Gilde ist ein echtes "
     "Gebäude mit eigenem Banner, eigenen Leuten und eigenem Übungsplatz.")], flip=True)}
{feature(ctx, "KA-05", ("Pillar 3", "Säule 3"), ("Combat you can read", "Kampf, den man lesen kann"), [
    ("A target frame, cast bars, damage numbers and ground markings for every special attack. You should always know what is "
     "about to hit you, and have a moment to move.",
     "Ein Zielfenster, Zauberleisten, Schadenszahlen und Bodenmarkierungen für jeden Spezialangriff. Du sollst immer wissen, was "
     "gleich auf dich zukommt, und einen Moment haben, um auszuweichen.")])}
{feature(ctx, "KA-06", ("Pillar 4", "Säule 4"), ("A gradient of danger", "Gefahr in Stufen"), [
    ("Outward from the town, the land gets older, darker and more dangerous: meadow, woodcutters' clearings, beech forest, "
     "deep spruce, the wolf den. You always know roughly how far you have come.",
     "Von der Stadt aus wird das Land älter, dunkler und gefährlicher: Wiese, Holzfällerlichtungen, Buchenwald, tiefer Fichtenwald, "
     "der Wolfsbau. Du weißt immer ungefähr, wie weit du gekommen bist.")], flip=True)}
{feature(ctx, "VW-08", ("Pillar 5", "Säule 5"), ("Better together", "Gemeinsam besser"), [
    ("Every fight can be won alone, and every fight gets easier with other players. A tank who holds attention and a healer who keeps "
     "people standing change how the Alpha plays.",
     "Jeder Kampf lässt sich allein gewinnen, und jeder Kampf wird mit anderen Spielern leichter. Ein Tank, der die Aufmerksamkeit "
     "hält, und ein Heiler, der alle auf den Beinen hält, verändern, wie sich der Alpha spielt.")])}
""")

    loop = section(f"""
<h2>{t("The loop", "Der Kreislauf")}</h2>
<p class="lede">{t("What you do, again and again, between the Dais and Frankfurt.", "Was du zwischen dem Dais und Frankfurt immer wieder tust.")}</p>
{loops(ctx, [
    (("Take a task", "Auftrag annehmen"), ("From Captain Roland, a trainer or a townsperson with a problem.",
                                           "Von Hauptmann Roland, einem Trainer oder einem Stadtbewohner mit einem Problem.")),
    (("Head out", "Losziehen"), ("Gather herbs at the forest edge, hunt wolves, find what was lost.",
                                 "Kräuter am Waldrand sammeln, Wölfe jagen, Verlorenes finden.")),
    (("Come back", "Zurückkehren"), ("Turn in, level up, sell pelts, buy and craft better gear.",
                                     "Abgeben, aufsteigen, Felle verkaufen, bessere Ausrüstung kaufen und herstellen.")),
    (("Go further", "Weiter vorstoßen"), ("New abilities open deeper, darker parts of the forest.",
                                          "Neue Fähigkeiten öffnen tiefere, dunklere Teile des Waldes.")),
])}""", "band-dark")
    frameworks = section(f"""
<h2>{t("Game framework used", "Verwendetes Spiele-Framework")}</h2>
<ul class="abilities"><li>Vertical Third</li></ul>""")
    return intro + pillars + loop + frameworks


def combat(ctx):
    t = ctx.t
    return section(f"""
{feature(ctx, "KA-05", ("Targeting", "Zielauswahl"), ("Pick your target, then act", "Ziel wählen, dann handeln"), [
    ("Press Tab to cycle through enemies in front of you, use the nearest-target key, or click an enemy. Your target shows in a "
     "frame at the top of the screen with its health and whatever it is casting.",
     "Mit Tab wechselst du zwischen den Gegnern vor dir, mit der Nächstes-Ziel-Taste nimmst du den nächsten, oder du klickst einen "
     "Gegner an. Dein Ziel erscheint oben in einem Fenster, mit seiner Gesundheit und allem, was es gerade wirkt.")])}
{feature(ctx, "KA-07", ("Abilities", "Fähigkeiten"), ("A hotbar, not a button-masher", "Eine Fähigkeitenleiste, kein Tastenhämmern"), [
    ("Auto-attack runs while you have a target. Your abilities sit on a hotbar of at least ten slots on the number keys, with a "
     "shared cooldown that gives each choice weight. New abilities arrive at levels 2, 3 and 5.",
     "Der automatische Angriff läuft, solange du ein Ziel hast. Deine Fähigkeiten liegen auf einer Leiste mit mindestens zehn "
     "Plätzen auf den Zahlentasten, mit einer gemeinsamen Abklingzeit, die jeder Entscheidung Gewicht gibt. Neue Fähigkeiten "
     "kommen auf Stufe 2, 3 und 5.")], flip=True)}
<h2>{t("What keeps a fight readable", "Was einen Kampf lesbar macht")}</h2>
{modes(ctx, [
    (("Warning", "Warnung"), ("Ground telegraphs", "Bodenmarkierungen"),
     ("Every special attack marks its area on the ground when the cast starts: a line, a cone or a circle.",
      "Jeder Spezialangriff markiert seine Fläche am Boden, sobald er beginnt: eine Linie, ein Kegel oder ein Kreis.")),
    (("Timing", "Timing"), ("Cast bars", "Zauberleisten"),
     ("You see what your target is casting and how long you have, so you can interrupt or step out.",
      "Du siehst, was dein Ziel wirkt und wie viel Zeit du hast, um zu unterbrechen oder auszuweichen.")),
    (("Feedback", "Rückmeldung"), ("Damage numbers", "Schadenszahlen"),
     ("Hits, heals and misses float above the target, so every ability tells you what it did.",
      "Treffer, Heilungen und Fehlschläge schweben über dem Ziel, sodass jede Fähigkeit zeigt, was sie bewirkt hat.")),
])}
<h2 style="margin-top:72px">{t("Controls", "Steuerung")}</h2>
{table(ctx, [("Action", "Aktion"), ("Default", "Standard"), ("Notes", "Hinweise")], [
    [("Move and sprint", "Bewegen und sprinten"), "WASD, Shift", ("Jump on Space", "Springen mit Leertaste")],
    [("Look around", "Umsehen"), ("Hold right mouse", "Rechte Maustaste halten"), ("Wheel to zoom", "Mausrad zum Zoomen")],
    [("Next target", "Nächstes Ziel"), "Tab", ("Cycles enemies in front of you", "Wechselt zwischen Gegnern vor dir")],
    [("Use ability", "Fähigkeit nutzen"), "1 – 0", ("Ten hotbar slots", "Zehn Plätze auf der Leiste")],
    [("Free the cursor", "Mauszeiger lösen"), "Alt", ("To click on menus and windows", "Zum Klicken auf Menüs und Fenster")],
])}""")


JOB_DETAILS = [
    ("paladin", "VW-04", ("Paladin", "Paladin"), ("Tank · sword and shield, blessed", "Tank · Schwert und Schild, gesegnet"),
     ("Bron, drill master of the Barracks and Training Yard", "Bron, Drillmeister der Kaserne und des Übungsplatzes"),
     ("Oxblood red, the kingdom's golden eagle", "Ochsenblutrot, der goldene Adler des Königreichs"),
     ("Paladins stand in front. They hold an enemy's attention, take the blows and keep the rest of the party out of harm's way.",
      "Paladine stehen vorn. Sie halten die Aufmerksamkeit eines Gegners, stecken die Schläge ein und halten den Rest der Gruppe aus der Gefahr."),
     ["Combo strike", "Shield Bash", "Provoke", "Holy Guard", "Radiant Sweep"],
     ("Shield up. Again. The wolf won't wait for you to be ready.", "Schild hoch. Nochmal. Der Wolf wartet nicht, bis du bereit bist."), "Bron"),
    ("ranger", "VW-05", ("Ranger", "Ranger"), ("Ranged damage · bow", "Fernkampf-Schaden · Bogen"),
     ("Hagen, ranger master of the Hunters' Lodge", "Hagen, Rangermeister der Jägerhütte"),
     ("Forest green, a bow", "Waldgrün, ein Bogen"),
     ("Rangers fight from a distance, set traps and leap back out of reach when a wolf gets too close.",
      "Ranger kämpfen aus der Distanz, stellen Fallen und springen zurück, wenn ein Wolf zu nah kommt."),
     ["Quick Shot", "Piercing Arrow", "Volley", "Snare Trap", "Disengage"],
     ("Breathe out, then loose. The forest is patient. Be more patient.", "Ausatmen, dann loslassen. Der Wald ist geduldig. Sei geduldiger."), "Hagen"),
    ("whitemage", "VW-06", ("White Mage", "Weißmagier"), ("Healer · staff", "Heiler · Stab"),
     ("Mira, herbalist of the Herbalist's House and the Spring Shrine", "Mira, Kräuterkundige im Kräuterhaus und am Quellschrein"),
     ("White and pale gold, a water drop", "Weiß und Blassgold, ein Wassertropfen"),
     ("White Mages keep people alive: heals for one or for everyone, healing over time, cleansing poison, and raising the fallen.",
      "Weißmagier halten Leute am Leben: Heilung für einen oder alle, Heilung über Zeit, Gift reinigen und Gefallene wiederbeleben."),
     ["Stone", "Cure", "Medica", "Regen", "Esuna", "Raise"],
     ("Keep them standing. That is the whole job, and it is enough.", "Halt sie auf den Beinen. Das ist die ganze Arbeit, und sie reicht."), "Mira"),
    ("elementalist", "VW-07", ("Elementalist", "Elementarist"), ("Magic damage · staff", "Magie-Schaden · Stab"),
     ("Elwyn, the mage of Elwyn's Tower", "Elwyn, der Magier aus Elwyns Turm"),
     ("Deep indigo, a golden four-pointed star", "Tiefes Indigo, ein goldener vierzackiger Stern"),
     ("Elementalists throw fire, frost, lightning and earth: bolts, cones, channelled beams and spikes from the ground, with a "
      "short blink to get clear.",
      "Elementaristen schleudern Feuer, Frost, Blitz und Erde: Geschosse, Kegel, gebündelte Strahlen und Stacheln aus dem Boden, "
      "dazu ein kurzer Sprung, um freizukommen."),
     ["Fire Bolt", "Frost Cone", "Lightning Beam", "Earth Spike", "Blink"],
     ("Fire is easy. Stopping is the hard part. Mind the books.", "Feuer ist leicht. Aufhören ist das Schwere. Pass auf die Bücher auf."), "Elwyn"),
]


# Same left-to-right order as the line-ups.
PORTRAIT_JOBS = [
    ("WHITEMAGE", ("White Mage", "Weißmagier")),
    ("PALADIN", ("Paladin", "Paladin")),
    ("ELEMENTALIST", ("Elementalist", "Elementarist")),
    ("RANGER", ("Ranger", "Ranger")),
]


def jobs(ctx):
    t = ctx.t
    out = []
    for k, (key, img, name, role, trainer, banner, text, abil, line, who) in enumerate(JOB_DETAILS):
        extra = (f'<ul class="abilities">{"".join(f"<li>{a}</li>" for a in abil)}</ul>'
                 f'<div style="margin-top:22px">{quote(ctx, line, who)}</div>')
        body = (f'<p class="job-role" style="font-size:1rem">{ctx.t(*role)}</p><p>{ctx.t(*text)}</p>'
                f'{tags(ctx, [trainer, banner])}')
        out.append(f'<div id="{key}" class="job-{key}" style="scroll-margin-top:90px">'
                   + feature(ctx, img, None, name, body, flip=k % 2 == 1, extra=extra) + '</div>')
    # The two line-ups appear once both images exist, so the page never shows a placeholder for them.
    line_ups = ""
    if ctx.has("PC-GROUP-M") and ctx.has("PC-GROUP-F"):
        line_ups = '<div style="margin-bottom:72px">' + ctx.gallery([
            ("PC-GROUP-M", t("The four jobs as male characters", "Die vier Jobs mit männlichen Figuren")),
            ("PC-GROUP-F", t("The four jobs as female characters", "Die vier Jobs mit weiblichen Figuren")),
        ], "gallery-2") + "</div>"
    # Portraits appear one by one as their images are added, so there are never placeholders.
    portraits = ""
    for sex, label in (("F", ("female", "weiblich")), ("M", ("male", "männlich"))):
        row = [(f"PORTRAIT-{key}-{sex}", f"{t(*name)} ({t(*label)})")
               for key, name in PORTRAIT_JOBS if ctx.has(f"PORTRAIT-{key}-{sex}")]
        if row:
            portraits += '<div style="margin-bottom:22px">' + ctx.gallery(row, "gallery-4") + "</div>"
    if portraits:
        portraits = f'<div style="margin-bottom:72px">{portraits}</div>'
    return section(f"""
<p class="lede" style="margin-bottom:56px">{t("Every job can be played as a male or female character, and different races to choose from will come later. You pick one job in the vertical slice. Ability names are working names and will change as the jobs are tuned.",
                       "Jeder Job lässt sich mit einer männlichen oder weiblichen Figur spielen, und später kommen verschiedene Völker zur Auswahl dazu. In der Vertical Slice wählst du einen Job. Die Namen der Fähigkeiten sind Arbeitstitel und ändern sich, während die Jobs abgestimmt werden.")}</p>
{line_ups}{portraits}{"".join(out)}""")


def town_life(ctx):
    t = ctx.t
    return section(f"""
{feature(ctx, "KA-04", ("The forge", "Die Schmiede"), ("Haldor buys pelts and sells steel", "Haldor kauft Felle und verkauft Stahl"), [
    ("Haldor the smith sells weapons and armour, buys the wolf pelts you bring back, and teaches you to forge: five pelts and "
     "some iron make a pair of Wolfhide Bracers.",
     "Haldor der Schmied verkauft Waffen und Rüstungen, kauft die Wolfsfelle, die du mitbringst, und bringt dir das Schmieden bei: "
     "fünf Felle und etwas Eisen ergeben ein Paar Wolfsleder-Armschienen.")])}
{feature(ctx, "IT-08", ("The herbalist", "Die Kräuterkundige"), ("Silverleaf into Healing Draughts", "Silberblatt wird zu Heiltränken"), [
    ("The herbs you gather at the forest edge go onto Mira's alchemy table and come back as Healing Draughts. Wolfsbane makes "
     "antidotes, which you will want before the Alpha.",
     "Die Kräuter vom Waldrand landen auf Miras Alchemietisch und kommen als Heiltränke zurück. Aus Wolfseisenhut werden "
     "Gegengifte, die du vor dem Alpha haben willst.")], flip=True)}
{feature(ctx, "IT-01", ("The inn", "Das Gasthaus"), ("A bed and a hot meal at the Wolf's Rest", "Ein Bett und eine warme Mahlzeit im Wolf's Rest"), [
    ("Set your return point at the inn, and eat before a hard fight: the innkeeper's food gives a short boost.",
     "Leg im Gasthaus deinen Rückkehrpunkt fest und iss vor einem schweren Kampf: Das Essen des Wirts gibt dir einen kurzen Bonus.")])}
<h2 style="margin-top:72px">{t("What you gather and earn", "Was du sammelst und verdienst")}</h2>
{table(ctx, [("Item", "Gegenstand"), ("Where from", "Woher"), ("What for", "Wofür")], [
    [("Silverleaf", "Silberblatt"), ("Forest edge and beech forest", "Waldrand und Buchenwald"), ("Healing Draughts", "Heiltränke")],
    [("Wolfsbane", "Wolfseisenhut"), ("Beech forest and deep wood", "Buchenwald und tiefer Wald"), ("Antidotes", "Gegengifte")],
    [("Sunpetal", "Sonnenblüte"), ("Forest edge meadow", "Wiese am Waldrand"), ("The inn's buff food", "Das Stärkungsessen im Gasthaus")],
    [("Moonberry", "Mondbeere"), ("The old glade", "Die alte Lichtung"), ("Bounties at the linden", "Kopfgelder an der Linde")],
    [("Wolf pelt", "Wolfsfell"), ("Grey and dark wolves", "Graue und dunkle Wölfe"), ("Wolfhide Bracers, coin", "Wolfsleder-Armschienen, Münzen")],
    [("Alpha fang", "Alphazahn"), ("The Alpha", "Der Alpha"), ("A trophy, and an upgrade", "Eine Trophäe und eine Verbesserung")],
])}""")


PAGES = {
    "game/index.html": dict(
        title=("The Game", "Das Spiel"), kicker=("Overview & pillars", "Überblick & Säulen"),
        lede=("A fantasy online MMO of jobs, guilds and readable fights, starting in one forest town.",
              "Ein Fantasy-Online-MMO mit Jobs, Gilden und lesbaren Kämpfen, das in einer Waldstadt beginnt."),
        banner="KA-01", body=overview),
    "game/combat.html": dict(
        title=("Combat", "Kampf"), kicker=("The Game", "Das Spiel"),
        lede=("Select a target, read what it is about to do, and answer with the right ability.",
              "Wähle ein Ziel, lies, was es gleich tun wird, und antworte mit der richtigen Fähigkeit."),
        banner="KA-07", body=combat),
    "game/jobs.html": dict(
        title=("The Four Jobs", "Die vier Jobs"), kicker=("The Game", "Das Spiel"),
        lede=("Tank, ranged damage, healer and magic damage, each taught by its own guild in Hayn.",
              "Tank, Fernkampf-Schaden, Heiler und Magie-Schaden, jeder gelehrt von seiner eigenen Gilde in Hayn."),
        banner="VW-04", body=jobs),
    "game/town-life.html": dict(
        title=("Town Life", "Stadtleben"), kicker=("The Game", "Das Spiel"),
        lede=("Between the fights: vendors, crafting, potions and a warm bed.",
              "Zwischen den Kämpfen: Händler, Handwerk, Tränke und ein warmes Bett."),
        banner="KA-02", body=town_life),
}
