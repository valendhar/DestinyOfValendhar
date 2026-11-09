"""World: Valendhar, Hayn, the Wolfwood, the road to Frankfurt."""
from components import back, facts, feature, modes, section, table


def valendhar(ctx):
    t = ctx.t
    return section(f"""
<div class="intro" style="margin-bottom:80px">
  <div class="prose">
    <p class="big">{t("Valendhar is a medieval Germany that never was: the United German Kingdom, ruled from Frankfurt on the Main. "
                      "Most people live by timber, field and trade, and magic is something you meet in a tower or at a shrine, not on the street.",
                      "Valendhar ist ein mittelalterliches Deutschland, das es so nie gab: das Vereinigte Deutsche Königreich, regiert von "
                      "Frankfurt am Main aus. Die meisten Leute leben von Holz, Feld und Handel, und Magie begegnet dir in einem Turm oder "
                      "an einem Schrein, nicht auf der Straße.")}</p>
    <p>{t("Scattered across the land stand the Daises: weathered stone platforms ringed with faint blue glyphs, each with a "
          "rough megalith floating above it. Travellers arrive by them and leave by them. Nobody in Hayn remembers who "
          "built them.",
          "Überall im Land stehen die Daise: verwitterte Steinplattformen mit einem Ring aus schwach blauen Glyphen, über denen "
          "jeweils ein roher Monolith schwebt. Reisende kommen durch sie an und reisen durch sie ab. Niemand in Hayn "
          "erinnert sich, wer sie gebaut hat.")}</p>
  </div>
  {facts(ctx, [
      (("The world", "Die Welt"), ("Valendhar", "Valendhar")),
      (("The kingdom", "Das Königreich"), ("The United German Kingdom", "Das Vereinigte Deutsche Königreich")),
      (("Capital", "Hauptstadt"), ("Frankfurt on the Main", "Frankfurt am Main")),
      (("First region", "Erste Region"), ("Hayn, in the king's forest of Three-Oaks", "Hayn im Königsforst Dreieich")),
      (("Neighbours", "Nachbarn"), ("The town of Ysenburg", "Die Stadt Ysenburg")),
      (("Season", "Jahreszeit"), ("Early autumn, late afternoon", "Frühherbst, später Nachmittag")),
      (("Magic", "Magie"), ("Rare in town, stronger in the wild", "Selten in der Stadt, stärker in der Wildnis")),
  ])}
</div>
{feature(ctx, "KA-03", ("Arrival", "Ankunft"), ("The Wayward Dais", "Das Wayward Dais"), [
    ("A circular granite platform twelve metres across, its rim carved with glyphs that glow softly blue. Above its centre, a "
     "rough-hewn stone hangs two metres in the air, with thin blue cracks running through it. This is where every adventurer "
     "in Hayn first sets foot.",
     "Eine runde Granitplattform, zwölf Meter breit, ihr Rand mit Glyphen verziert, die sanft blau leuchten. Über ihrer Mitte "
     "schwebt ein grob behauener Stein zwei Meter in der Luft, durchzogen von feinen blauen Rissen. Hier setzt jeder Abenteurer "
     "in Hayn zum ersten Mal einen Fuß auf den Boden.")])}
{feature(ctx, "BE-01", ("The region", "Die Region"), ("Three-Oaks, the king's forest", "Die Dreieich, der Forst des Königs"), [
    ("South of the river Main lies Three-Oaks, a royal hunting forest. Its name is said to come from three ancient oaks. "
     "Oak and beech woods cover it, broken by wet brook meadows, reed-fringed ponds and wide marshes the foresters call the Bruch, "
     "where the ground stays soft all year. The king's foresters guard the game, and the hunting courts sit in the villages "
     "around the edge.",
     "Südlich des Mains liegt die Dreieich, ein königlicher Jagdforst. Ihr Name soll von drei uralten Eichen stammen. "
     "Eichen- und Buchenwälder bedecken sie, unterbrochen von nassen Bachwiesen, schilfgesäumten Weihern und weiten Sümpfen, "
     "die die Förster das Bruch nennen und wo der Boden das ganze Jahr weich bleibt. Die Förster des Königs hüten das Wild, und "
     "die Jagdgerichte tagen in den Dörfern am Rand."),
    ("Hayn sits in a clearing about 300 by 240 metres on a gentle south-facing slope. A brook comes out of the forest "
     "in the north-west, feeds a mill pond, and runs past the west wall. Wooded ridges rise to the north and west, and the "
     "neighbouring town of Ysenburg lies beyond them.",
     "Hayn liegt auf einer Lichtung von etwa 300 mal 240 Metern an einem sanften Südhang. Ein Bach kommt im Nordwesten "
     "aus dem Wald, speist einen Mühlteich und fließt an der Westmauer vorbei. Im Norden und Westen steigen bewaldete Kämme an, "
     "und dahinter liegt die Nachbarstadt Ysenburg.")],
    flip=True)}
{feature(ctx, "OH-GATE", ("The capital", "Die Hauptstadt"), ("Frankfurt on the Main", "Frankfurt am Main"), [
    ("North of the forest the land opens onto the broad, fertile valley of the Main, with the blue line of the Taunus hills "
     "on the horizon. Frankfurt grew on a low hill at an old ford of the river. A long stone bridge, with mills built against "
     "it, crosses to Sachsenhausen on the south bank, a quarter of fishermen, gardens and orchards, and walls and towers ring "
     "both halves of the city. Above the steep roofs rise the cathedral tower and the king's hall.",
     "Nördlich des Waldes öffnet sich das Land zum breiten, fruchtbaren Tal des Mains, mit der blauen Linie des Taunus am "
     "Horizont. Frankfurt wuchs auf einem flachen Hügel an einer alten Furt des Flusses. Eine lange Steinbrücke, an die Mühlen "
     "gebaut sind, führt hinüber nach Sachsenhausen am Südufer, einem Viertel der Fischer, Gärten und Obstwiesen, und Mauern "
     "und Türme umschließen beide Hälften der Stadt. Über den steilen Dächern ragen der Domturm und die Halle des Königs auf."),
    ("Frankfurt is where the heroes truly learn their craft, in the great houses of their guilds, and where the real "
     "adventure begins. Its gate is the end of the vertical slice.",
     "In Frankfurt lernen die Helden ihr Handwerk wirklich, in den großen Häusern ihrer Gilden, und hier beginnt das "
     "eigentliche Abenteuer. Sein Tor ist das Ende der Vertical Slice.")])}
<h2 style="margin-top:56px">{t("Explore", "Erkunden")}</h2>
{modes(ctx, [
    (("The town", "Die Stadt"), (f'<a href="{ctx.url("world/hayn.html")}">Hayn</a>',) * 2,
     ("Half-timbered houses, four guilds, a forge, an inn and a captain with too few people.",
      "Fachwerkhäuser, vier Gilden, eine Schmiede, ein Gasthaus und ein Hauptmann mit zu wenig Leuten.")),
    (("The forest", "Der Wald"), (f'<a href="{ctx.url("world/wolfwood.html")}">{t("The Wolfwood", "Der Wolfwood")}</a>',) * 2,
     ("Ten zones from sunny meadow to the wolf den, each darker than the last.",
      "Zehn Zonen von der sonnigen Wiese bis zum Wolfsbau, jede dunkler als die vorige.")),
    (("The road", "Die Straße"), (f'<a href="{ctx.url("world/road.html")}">{t("Road to Frankfurt", "Straße nach Frankfurt")}</a>',) * 2,
     ("A milestone, a stone bridge, an ambush, a dungeon under a hill, and a gate.",
      "Ein Meilenstein, eine Steinbrücke, ein Hinterhalt, ein Verlies unter einem Hügel und ein Tor.")),
])}""")


def hayn(ctx):
    t = ctx.t
    return section(f"""
<div class="intro" style="margin-bottom:80px">
  <div class="prose">
    <p class="big">{t("A town of German half-timbered houses in the king's forest of Three-Oaks, built behind an oval stone wall "
                      "with towers and gates. Its name means the grove, after the walled court of the king's foresters it grew up around.",
                      "Eine Stadt aus deutschen Fachwerkhäusern im Königsforst Dreieich, gebaut hinter einer ovalen Steinmauer "
                      "mit Türmen und Toren. Ihr Name bedeutet Hain, nach dem umfriedeten Hof der königlichen Förster, um den sie gewachsen ist.")}</p>
    <p>{t("Black and oxblood-red beams over off-white lime plaster. Steep red tile roofs with moss, jettied upper floors on carved "
          "brackets, geraniums in the window boxes, firewood stacked under every eave. Every facade has something leaning on it, "
          "hanging off it or stacked against it.",
          "Schwarze und ochsenblutrote Balken über gebrochen weißem Kalkputz. Steile rote Ziegeldächer mit Moos, vorkragende "
          "Obergeschosse auf geschnitzten Knaggen, Geranien in den Blumenkästen, Brennholz unter jedem Dachvorsprung. An jeder "
          "Fassade lehnt, hängt oder stapelt sich etwas.")}</p>
  </div>
  {facts(ctx, [
      (("Size", "Größe"), ("Wall about 190 × 170 m", "Mauer etwa 190 × 170 m")),
      (("Gates", "Tore"), ("Two main gates, south and north, and small gates west and east", "Zwei Haupttore im Süden und Norden, dazu kleine Tore im Westen und Osten")),
      (("Landmarks", "Wahrzeichen"), ("Town hall, inn, Elwyn's tower, watchtower", "Rathaus, Gasthaus, Elwyns Turm, Wachturm")),
      (("Lives on", "Lebt von"), ("Timber, fields and the road to Frankfurt", "Holz, Feldern und der Straße nach Frankfurt")),
  ])}
</div>
{feature(ctx, "KA-01", ("The main street", "Die Hauptgasse"), ("Up the hill to the square", "Den Hügel hinauf zum Platz"), [
    ("From the South Gate a cobbled street climbs gently north. It bends a little on the way, so the square reveals itself "
     "rather than appearing at the end of a corridor. The forge glows on the left.",
     "Vom Südtor steigt eine gepflasterte Gasse sanft nach Norden an. Unterwegs biegt sie leicht ab, sodass sich der Platz erst "
     "nach und nach zeigt, statt am Ende eines Korridors zu stehen. Links glüht die Schmiede.")])}
{feature(ctx, "KA-02", ("The heart", "Das Herz"), ("Market square and fountain", "Marktplatz und Brunnen"), [
    ("Red sandstone slabs around a nine-metre fountain, where a bronze Forest Warden, the warden of the king's forest, "
     "stands with his hand on a red stag above four bronze stag-head spouts. Six market stalls, a great old linden with the bounty "
     "board, and the town hall on the north side.",
     "Rote Sandsteinplatten um einen neun Meter breiten Brunnen, wo ein bronzener Forstwart, der Hüter des königlichen Waldes, "
     "mit der Hand auf einem Rothirsch über vier bronzenen Hirschkopf-Speiern steht. Sechs Marktstände, eine große alte Linde mit "
     "dem Kopfgeldbrett und im Norden das Rathaus.")], flip=True)}
{feature(ctx, "VW-02", ("Captain Roland's post", "Hauptmann Rolands Posten"), ("Town Hall and Watch House", "Rathaus und Wachhaus"), [
    ("The grandest building in town: an arcade of four sandstone arches below, two richly carved half-timbered floors "
     "above, corner oriels and a slate bell turret. The guard room is at the back.",
     "Das prächtigste Gebäude der Stadt: unten eine Arkade aus vier Sandsteinbögen, darüber zwei reich geschnitzte Fachwerkgeschosse, "
     "Ecktürmchen und ein schiefergedecktes Glockentürmchen. Die Wachstube liegt dahinter.")])}
{feature(ctx, "KA-08", ("After dark", "Nach Einbruch der Dunkelheit"), ("Hayn at night", "Hayn bei Nacht"), [
    ("Lanterns on wet cobbles, candlelight in small leaded windows, the inn spilling light onto the square, and the top of "
     "Elwyn's tower glowing faintly red above the roofs.",
     "Laternen auf nassem Pflaster, Kerzenlicht in kleinen Butzenscheiben, das Gasthaus, das Licht auf den Platz wirft, und die "
     "Spitze von Elwyns Turm, die schwach rot über den Dächern glüht.")], flip=True)}
<h2 style="margin-top:72px">{t("Places in town", "Orte in der Stadt")}</h2>
{table(ctx, [("Place", "Ort"), ("Who", "Wer"), ("Why you go there", "Warum du hingehst")], [
    [("Wayward Dais", "Wayward Dais"), "—", ("Arrival and return point", "Ankunft und Rückkehrpunkt")],
    [("Town Hall & Watch House", "Rathaus & Wachhaus"), ("Captain Roland", "Hauptmann Roland"), ("The main quests", "Die Hauptquests")],
    [("Forge", "Schmiede"), "Hermann", ("Weapons, armour, pelts, forging", "Waffen, Rüstung, Felle, Schmieden")],
    [("Barracks & Training Yard", "Kaserne & Übungsplatz"), "Bron", ("Paladin guild", "Paladin-Gilde")],
    [("Hunters' Lodge", "Jägerhütte"), "Hagen", ("Ranger guild and archery range", "Ranger-Gilde und Bogenschießplatz")],
    [("Herbalist's House & Spring Shrine", "Kräuterhaus & Quellschrein"), "Mira", ("White Mage guild, herbs, alchemy", "Weißmagier-Gilde, Kräuter, Alchemie")],
    [("Elwyn's Tower", "Elwyns Turm"), "Elwyn", ("Elementalist guild and rune circle", "Elementaristen-Gilde und Runenkreis")],
    [("Inn: the Golden Acorn", "Gasthaus: Zur Goldenen Eichel"), ("The innkeeper", "Der Wirt"), ("Return point, food", "Rückkehrpunkt, Essen")],
    [("General store", "Krämerladen"), ("The storekeeper", "Der Krämer"), ("Potions, supplies, bags", "Tränke, Vorräte, Taschen")],
    [("North Gate & Watchtower", "Nordtor & Wachturm"), ("The guards", "Die Wachen"), ("The road to Frankfurt and the way into the Wolfwood", "Die Straße nach Frankfurt und der Weg in den Wolfwood")],
])}
<h2 style="margin-top:72px">{t("Around the wall", "Rund um die Mauer")}</h2>
{ctx.gallery([
    ("KA-09", t("Misty dawn at the mill pond", "Nebliger Morgen am Mühlteich")),
    ("VW-09", t("The farmstead and fields", "Der Bauernhof und die Felder")),
    ("VW-03", t("Through the west postern", "Durch die Westpforte")),
], "gallery-3")}""")


ZONES = [
    ("F1", ("Forest edge & meadow", "Waldrand & Wiese"), ("0–100 m", "0–100 m"),
     ("Birch, hazel, brambles and tall grass. Herbs to gather, deer and rabbits.", "Birken, Haseln, Brombeeren und hohes Gras. Kräuter zum Sammeln, Rehe und Hasen.")),
    ("F2", ("Woodcutters' fringe", "Holzfällersaum"), ("100–250 m", "100–250 m"),
     ("Stumps, log piles and a woodcutter's shelter. The first wolves.", "Baumstümpfe, Holzstapel und ein Holzfällerunterstand. Die ersten Wölfe.")),
    ("F3", ("Beech-oak forest", "Buchen-Eichen-Wald"), ("250–500 m", "250–500 m"),
     ("Silver beech trunks like pillars, old oaks, light shafts. Wolf packs and boar.", "Silberne Buchenstämme wie Säulen, alte Eichen, Lichtstrahlen. Wolfsrudel und Wildschweine.")),
    ("F4", ("Stream gorge", "Bachschlucht"), ("Crossing F3", "Quer durch F3"),
     ("A rocky stream, a small waterfall and a fallen-tree bridge.", "Ein felsiger Bach, ein kleiner Wasserfall und eine Brücke aus einem umgestürzten Baum.")),
    ("F5", ("The old glade", "Die alte Lichtung"), ("~400 m north", "~400 m nördlich"),
     ("A ring of standing stones, an ancient oak, glowing motes at night.", "Ein Ring stehender Steine, eine uralte Eiche, leuchtende Funken in der Nacht.")),
    ("F6", ("Spruce-fir deep wood", "Fichten-Tannen-Tiefwald"), ("500–900 m", "500–900 m"),
     ("Dark spruce, needle floor, deadfall and little light. Dark wolves.", "Dunkle Fichten, Nadelboden, Totholz und wenig Licht. Dunkle Wölfe.")),
    ("F7", ("The wolf den", "Der Wolfsbau"), ("~700 m", "~700 m"),
     ("A rock outcrop with a cave mouth, bones and gnawed antlers. The Alpha.", "Ein Felsvorsprung mit Höhleneingang, Knochen und abgenagten Geweihen. Der Alpha.")),
    ("F8", ("Ruined watchtower", "Verfallener Wachturm"), ("~600 m north-west", "~600 m nordwestlich"),
     ("A collapsed stone tower, overgrown. A view, and a lost satchel.", "Ein eingestürzter, überwucherter Steinturm. Eine Aussicht und eine verlorene Tasche.")),
    ("F9", ("Hunter's blind & camp", "Hochsitz & Lager"), ("~350 m", "~350 m"),
     ("A raised hunting stand, an abandoned campfire, a lean-to.", "Ein Hochsitz, ein verlassenes Lagerfeuer, ein Unterstand.")),
]


def wolfwood(ctx):
    t = ctx.t
    rows = [[z, n, d, w] for z, n, d, w in ZONES]
    return section(f"""
{feature(ctx, "KA-06", ("The forest", "Der Wald"), ("Rings that grow darker", "Ringe, die dunkler werden"), [
    ("About a square kilometre of temperate Central European forest north and west of the town, laid out in rings. Near the "
     "wall it is sunny and safe; further in, the trees get older and taller and the wolves get bolder.",
     "Etwa ein Quadratkilometer mitteleuropäischer Mischwald nördlich und westlich der Stadt, in Ringen angelegt. Nahe der Mauer "
     "ist es sonnig und sicher; weiter drinnen werden die Bäume älter und höher und die Wölfe kühner.")])}
{feature(ctx, "TD-04", ("The map", "Die Karte"), ("Ten zones", "Zehn Zonen"), [
    ("Each zone has its own trees, its own light and its own job in the journey, so you always have a feeling for how deep "
     "you are.",
     "Jede Zone hat ihre eigenen Bäume, ihr eigenes Licht und ihre eigene Rolle auf der Reise, sodass du immer ein Gefühl dafür "
     "hast, wie tief du drin bist.")], flip=True)}
<h2 style="margin-top:72px">{t("Zone by zone", "Zone für Zone")}</h2>
{table(ctx, [("Zone", "Zone"), ("Name", "Name"), ("From the town", "Von der Stadt aus"), ("What is there", "Was dort ist")], rows)}
<h2 style="margin-top:72px">{t("Pictures from the forest", "Bilder aus dem Wald")}</h2>
{ctx.gallery([
    ("KA-05", t("Wolves at the forest edge, at dusk", "Wölfe am Waldrand in der Dämmerung")),
    ("KA-07", t("The wolf den", "Der Wolfsbau")),
    ("BE-02", t("From the north-west, over the forest to the town", "Von Nordwesten über den Wald zur Stadt")),
    ("VW-10", t("From the forest ridge", "Vom Waldkamm aus")),
], "gallery-2")}""")


def road(ctx):
    t = ctx.t
    steps = [
        (("North Gate", "Nordtor"), ("The big gate toward the capital. The merchant's cart waits here.", "Das große Tor Richtung Hauptstadt. Hier wartet der Händlerkarren.")),
        (("Milestone and wayside shrine", "Meilenstein und Wegschrein"), ("Gravel, two worn tracks with grass between them, tall beeches on either side.", "Kies, zwei ausgefahrene Spuren mit Gras dazwischen, hohe Buchen zu beiden Seiten.")),
        (("The stone bridge", "Die Steinbrücke"), ("A small arch over a brook.", "Ein kleiner Bogen über einen Bach.")),
        (("The ambush point", "Der Hinterhalt"), ("An overturned cart and scattered crates. Two waves to survive.", "Ein umgestürzter Karren und verstreute Kisten. Zwei Wellen zu überleben.")),
        (("The wounded scout", "Der verwundete Kundschafter"), ("He has seen what is under the hill.", "Er hat gesehen, was unter dem Hügel ist.")),
        (("The dungeon entrance", "Der Verlieseingang"), ("An overgrown stone archway into a hillside, carved with wolf heads.", "Ein überwucherter Steinbogen in einen Hang, mit eingemeißelten Wolfsköpfen.")),
        (("The Saxenhausen Watchtower", "Die Sachsenhäuser Warte"), ("The end of the vertical slice, with Frankfurt below.", "Das Ende der Vertical Slice, mit Frankfurt darunter.")),
    ]
    return section(f"""
{feature(ctx, "VW-08", ("Leaving Hayn", "Hayn verlassen"), ("The road to the capital", "Die Straße zur Hauptstadt"), [
    ("Once the Alpha is dead, Captain Roland asks you to see a merchant safely to Frankfurt. The road is quiet for a while.",
     "Sobald der Alpha tot ist, bittet dich Hauptmann Roland, einen Händler sicher nach Frankfurt zu bringen. Eine Weile lang "
     "ist die Straße ruhig.")])}
<h2 style="margin-top:56px">{t("Along the road", "Entlang der Straße")}</h2>
<ol class="loops loops-3">{"".join(f'<li><span class="loop-label">{ctx.t(*a)}</span><p>{ctx.t(*b)}</p></li>' for a, b in steps)}</ol>
<div style="margin-top:80px">
{feature(ctx, "DG-01", ("Beneath the hill", "Unter dem Hügel"), ("The dungeon", "Das Verlies"), [
    ("An entrance hall, three rooms of enemies, a bridge, a round boss chamber thirty metres across, and a tunnel back out to "
     "the road. Best with other players. It is the barrow of a forgotten wolf-cult, and its dead still stand guard.",
     "Eine Eingangshalle, drei Räume voller Gegner, eine Brücke, eine runde Bosskammer von dreißig Metern und ein Tunnel zurück "
     "zur Straße. Am besten mit anderen Spielern. Es ist das Hügelgrab eines vergessenen Wolfskults, und seine Toten halten noch immer Wache.")],
    flip=True)}
</div>""")


PAGES = {
    "world/index.html": dict(
        title=("Valendhar", "Valendhar"), kicker=("World", "Welt"),
        lede=("A medieval Germany that never was: old forests, walled towns and the floating stones that bring travellers in.",
              "Ein mittelalterliches Deutschland, das es nie gab: alte Wälder, ummauerte Städte und die schwebenden Steine, die Reisende herbringen."),
        banner="BE-01", body=valendhar),
    "world/hayn.html": dict(
        title=("Hayn", "Hayn"), kicker=("World", "Welt"),
        lede=("A half-timbered town behind a stone wall, in the king's forest of Three-Oaks.",
              "Eine Fachwerkstadt hinter einer Steinmauer, im Königsforst Dreieich."),
        banner="KA-01", body=hayn),
    "world/wolfwood.html": dict(
        title=("The Wolfwood", "Der Wolfwood"), kicker=("World", "Welt"),
        lede=("Meadow, beech, spruce, den: the forest gets older the deeper you go.",
              "Wiese, Buche, Fichte, Bau: Der Wald wird älter, je tiefer du gehst."),
        banner="KA-06", body=wolfwood),
    "world/road.html": dict(
        title=("Road to Frankfurt", "Straße nach Frankfurt"), kicker=("World", "Welt"),
        lede=("A cart to guard, an ambush, a dungeon under a hill, and a gate at the end.",
              "Ein Karren zum Beschützen, ein Hinterhalt, ein Verlies unter einem Hügel und am Ende ein Tor."),
        banner="VW-08", body=road),
}
