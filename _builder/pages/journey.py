"""The Journey: the eleven stops, the quest chain, the Alpha fight."""
import importlib.util
from pathlib import Path

from components import T, back, facts, feature, modes, quote, section, table

# Reuse the act list from the home page so the two never drift apart.
_spec = importlib.util.spec_from_file_location("home_acts", Path(__file__).with_name("home.py"))
_home = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_home)
ACTS = _home.ACTS

# What each stop teaches, and its picture
STOPS = [
    ("KA-03", ("Spawn at the floating stone, learn to move, look around and read the first signpost.",
               "Du erscheinst am schwebenden Stein, lernst dich zu bewegen, umzusehen und liest den ersten Wegweiser.")),
    ("VW-02", ("Report to Captain Roland under the town-hall arcade. Dialogue, the quest log and the tracker.",
               "Melde dich bei Hauptmann Roland unter den Arkaden des Rathauses. Gespräche, Questlog und Questanzeige.")),
    ("VW-04", ("Visit the four guilds and choose one job. Your trainer hands you a weapon, armour and your first two abilities.",
               "Besuche die vier Gilden und wähle einen Job. Dein Trainer gibt dir eine Waffe, Rüstung und deine ersten zwei Fähigkeiten.")),
    ("VW-05", ("Target a dummy, use your abilities, defeat a sparring partner, and reach level 2.",
               "Nimm eine Übungspuppe ins Ziel, setz deine Fähigkeiten ein, besiege einen Übungsgegner und erreiche Stufe 2.")),
    ("KA-05", ("Gather Silverleaf in the meadow outside the north gate, before any wolf shows up.",
               "Sammle Silberblatt auf der Wiese vor dem Nordtor, bevor sich ein Wolf zeigt.")),
    ("KA-06", ("Grey wolves in packs of two and three, a wild boar that charges. Loot, experience and level 3.",
               "Graue Wölfe in Rudeln zu zweit und zu dritt, ein Wildschwein, das angreift. Beute, Erfahrung und Stufe 3.")),
    ("KA-04", ("Sell pelts, forge Wolfhide Bracers, brew Healing Draughts, and find the scout's satchel at the ruined watchtower.",
               "Verkaufe Felle, schmiede Wolfsleder-Armschienen, braue Heiltränke und finde die Tasche des Kundschafters am verfallenen Wachturm.")),
    ("KA-07", ("Dark wolves in the spruce, then the Alpha in its den: telegraphs, summoned wolves and a frenzy at the end.",
               "Dunkle Wölfe in den Fichten, dann der Alpha in seinem Bau: Bodenmarkierungen, herbeigerufene Wölfe und am Ende eine Raserei.")),
    ("VW-08", ("Escort a merchant's cart out of the East Gate, then hold off two waves of ambushers.",
               "Begleite einen Händlerkarren aus dem Osttor und wehre dann zwei Wellen von Angreifern ab.")),
    ("DG-01", ("A wounded scout warns you about the hill. Three packs, a two-phase boss, and a way back out to the road.",
               "Ein verwundeter Kundschafter warnt dich vor dem Hügel. Drei Gruppen, ein Boss mit zwei Phasen und ein Weg zurück zur Straße.")),
    ("OH-GATE", ("Follow the last stretch of road to Oakhaven's gate, where the first chapter ends with a summary of your run.",
                 "Folge dem letzten Stück Straße bis zum Tor von Oakhaven, wo das erste Kapitel mit einer Übersicht deines Laufs endet.")),
]


def path_page(ctx):
    t = ctx.t
    oq, cq = t("“", "„"), t("”", "“")
    rows = []
    for k, ((act, name, line, kind), (img, what)) in enumerate(zip(ACTS, STOPS)):
        extra = f'<p class="wp-line" style="margin-top:6px">{oq}{T(ctx, line)}{cq}</p>'
        rows.append(f'<div id="act-{k}" style="scroll-margin-top:90px">'
                    + feature(ctx, img, act, name, [what], flip=k % 2 == 1, extra=extra) + '</div>')
    return section(f"""
<div class="intro" style="margin-bottom:80px">
  <p class="big">{t("The first chapter is one road, walked in eleven stops. It takes 45 to 75 minutes with one job, "
                    "and every stop teaches one new thing.",
                    "Das erste Kapitel ist eine Straße in elf Stationen. Mit einem Job dauert es 45 bis 75 Minuten, "
                    "und jede Station bringt dir eine neue Sache bei.")}</p>
  {facts(ctx, [
      (("Play time", "Spielzeit"), ("45–75 minutes", "45–75 Minuten")),
      (("Levels", "Stufen"), ("1 to 5 by the Alpha, 6–7 after the dungeon", "1 bis 5 beim Alpha, 6–7 nach dem Verlies")),
      (("Quests", "Quests"), ("17 main steps, one optional", "17 Hauptschritte, einer optional")),
      (("Bosses", "Bosse"), ("The Alpha, and the dungeon boss", "Der Alpha und der Verliesboss")),
  ])}
</div>
{"".join(rows)}""")


QUESTS = [
    ("The Wayward Road", "Die Wayward-Straße", "Walk from the Dais to the South Gate and read the signpost.", "Geh vom Dais zum Südtor und lies den Wegweiser."),
    ("Report to the Captain", "Melde dich beim Hauptmann", "Find Captain Roland at the Watch House.", "Finde Hauptmann Roland im Wachhaus."),
    ("A Calling", "Eine Berufung", "Visit the guilds and choose your job.", "Besuche die Gilden und wähle deinen Job."),
    ("First Lessons", "Erste Lektionen", "Train with your guild master and beat the sparring dummy.", "Trainiere bei deinem Gildenmeister und besiege die Übungspuppe."),
    ("Field Supplies", "Vorräte vom Feld", "Gather six Silverleaf at the forest edge for Mira.", "Sammle sechs Silberblatt am Waldrand für Mira."),
    ("Cull the Pack", "Dünn das Rudel aus", "Defeat six grey wolves in the Wolfwood.", "Besiege sechs graue Wölfe im Wolfwood."),
    ("Pelts for the Smith", "Felle für den Schmied", "Bring Haldor five wolf pelts.", "Bring Haldor fünf Wolfsfelle."),
    ("Gear Up", "Ausrüsten", "Craft Wolfhide Bracers and equip a forged weapon.", "Stell Wolfsleder-Armschienen her und rüste eine geschmiedete Waffe aus."),
    ("Bitter Remedy", "Bittere Arznei", "Brew three Healing Draughts at Mira's table.", "Braue drei Heiltränke an Miras Tisch."),
    ("The Old Watchtower", "Der alte Wachturm", "Find the scout's satchel at the ruined tower.", "Finde die Tasche des Kundschafters am verfallenen Turm."),
    ("Darker Woods", "Dunklere Wälder", "Defeat four dark wolves in the spruce wood.", "Besiege vier dunkle Wölfe im Fichtenwald."),
    ("The Alpha", "Der Alpha", "Enter the wolf den and defeat the Alpha.", "Betritt den Wolfsbau und besiege den Alpha."),
    ("Rest at the Wolf's Rest", "Rast im Wolf's Rest", "Set your return point at the inn and eat.", "Leg im Gasthaus deinen Rückkehrpunkt fest und iss."),
    ("Road to Oakhaven", "Straße nach Oakhaven", "Escort the merchant's cart from the East Gate.", "Begleite den Händlerkarren vom Osttor."),
    ("Ambush!", "Hinterhalt!", "Defend the cart through two waves.", "Verteidige den Karren gegen zwei Wellen."),
    ("The Wounded Scout", "Der verwundete Kundschafter", "Optional: help the scout and hear his warning.", "Optional: Hilf dem Kundschafter und hör dir seine Warnung an."),
    ("Beneath the Hill", "Unter dem Hügel", "Clear the dungeon and defeat its boss.", "Säubere das Verlies und besiege seinen Boss."),
    ("The Gates of Oakhaven", "Die Tore von Oakhaven", "Follow the road to the gate.", "Folge der Straße bis zum Tor."),
]


def quests_page(ctx):
    t = ctx.t
    rows = [[str(k + 1), (en, de), (den, dde)] for k, (en, de, den, dde) in enumerate(QUESTS)]
    return section(f"""
<p class="lede" style="margin-bottom:28px">{t("Eighteen steps from the first signpost to the last gate. Names are working names.",
                     "Achtzehn Schritte vom ersten Wegweiser bis zum letzten Tor. Die Namen sind Arbeitstitel.")}</p>
{table(ctx, [("Step", "Schritt"), ("Quest", "Quest"), ("What you do", "Was du tust")], rows, "quest-table")}
<h2 style="margin-top:80px">{t("On the side", "Nebenbei")}</h2>
{modes(ctx, [
    (("The linden", "Die Linde"), ("The bounty board", "Das Kopfgeldbrett"),
     ("Repeatable jobs pinned under the old linden: five boar, or five Moonberries from the glade.",
      "Wiederholbare Aufträge unter der alten Linde: fünf Wildschweine oder fünf Mondbeeren von der Lichtung.")),
    (("The hunter's blind", "Der Hochsitz"), ("A ranger's hunt", "Eine Rangerjagd"),
     ("A hunt from the raised stand deep in the beech forest.", "Eine Jagd vom Hochsitz tief im Buchenwald.")),
    (("The old glade", "Die alte Lichtung"), ("The stone circle", "Der Steinkreis"),
     ("A ring of standing stones around a single ancient oak, and a story older than the village.",
      "Ein Ring aus stehenden Steinen um eine einzelne uralte Eiche, und eine Geschichte, die älter ist als das Dorf.")),
])}""")


def alpha_page(ctx):
    t = ctx.t
    return section(f"""
<div class="intro" style="margin-bottom:72px">
  <div class="prose">
    {quote(ctx, ("It's bigger than the others. Bigger than any wolf should be. Take antidotes.",
                 "Er ist größer als die anderen. Größer, als ein Wolf sein sollte. Nimm Gegengift mit."), ("Captain Roland", "Hauptmann Roland"))}
    <p>{t("The Alpha leads the pack from a den under a rock outcrop deep in the spruce. It is the first-chapter boss: winnable alone "
          "at level 5 with any job, and noticeably easier with a friend who can hold its attention or keep you healed.",
          "Der Alpha führt das Rudel aus einem Bau unter einem Felsvorsprung tief im Fichtenwald. Er ist der Boss des ersten Kapitels: "
          "allein auf Stufe 5 mit jedem Job zu schaffen und spürbar leichter mit einem Freund, der seine Aufmerksamkeit hält oder dich heilt.")}</p>
  </div>
  {facts(ctx, [
      (("Where", "Wo"), ("The wolf den, deep in the spruce wood", "Der Wolfsbau, tief im Fichtenwald")),
      (("Level", "Stufe"), ("5, elite", "5, Elite")),
      (("Size", "Größe"), ("2.2 m long, 1.1 m at the shoulder", "2,2 m lang, 1,1 m Schulterhöhe")),
      (("Drops", "Beute"), ("Alpha fang, always; a rare item, sometimes", "Alphazahn immer, manchmal ein seltener Gegenstand")),
  ])}
</div>
<h2>{t("Three phases", "Drei Phasen")}</h2>
{modes(ctx, [
    (("100 – 60 %", "100 – 60 %"), ("The hunt", "Die Jagd"),
     ("Bite combos, a Lunge along a line you can see coming, and Rend, a bleed that a healer can cleanse.",
      "Bisskombos, ein Sprung entlang einer Linie, die du kommen siehst, und Zerfleischen, eine Blutung, die ein Heiler reinigen kann.")),
    (("60 – 25 %", "60 – 25 %"), ("The howl", "Das Heulen"),
     ("It howls for two grey wolves and grows stronger. Interrupt the howl, or kill the adds fast.",
      "Er heult nach zwei grauen Wölfen und wird stärker. Unterbrich das Heulen oder töte die Helfer schnell.")),
    (("Below 25 %", "Unter 25 %"), ("Frenzy", "Raserei"),
     ("Faster attacks and Savage Spin, a circle around it marked on the ground. Step out, then finish it.",
      "Schnellere Angriffe und Wilder Wirbel, ein Kreis um ihn, der am Boden markiert ist. Raus aus dem Kreis, dann erledige ihn.")),
])}
<div style="margin-top:72px">
{feature(ctx, "KA-07", ("The arena", "Die Arena"), ("The den", "Der Bau"), [
    ("A clearing of trampled earth and pine needles, ringed by fallen trunks, with the cave mouth at the back. Bones and a torn "
     "traveller's pack near the entrance. One shaft of pale light.",
     "Eine Lichtung aus zertrampelter Erde und Fichtennadeln, umringt von umgestürzten Stämmen, mit dem Höhleneingang im Hintergrund. "
     "Knochen und ein zerrissener Reisesack am Eingang. Ein einzelner Strahl fahlen Lichts.")])}
</div>
{back(ctx, "journey/index.html", ("Back to the journey", "Zurück zur Reise"))}""")


PAGES = {
    "journey/index.html": dict(
        title=("From Dais to Gate", "Vom Dais zum Tor"), kicker=("The Journey", "Die Reise"),
        lede=("The whole first chapter, stop by stop.", "Das ganze erste Kapitel, Station für Station."),
        banner="KA-03", body=path_page),
    "journey/quests.html": dict(
        title=("The Quest Chain", "Die Questreihe"), kicker=("The Journey", "Die Reise"),
        lede=("Every step of the main story, and what waits on the side.", "Jeder Schritt der Hauptgeschichte, und was nebenbei wartet."),
        body=quests_page),
    "journey/the-alpha.html": dict(
        title=("The Alpha", "Der Alpha"), kicker=("Boss", "Boss"),
        lede=("The wolf that taught the pack to come out of the trees.", "Der Wolf, der dem Rudel beibrachte, aus den Bäumen zu kommen."),
        banner="KA-07", body=alpha_page),
}
