"""Characters: the people of Hayn, and the creatures of the Wolfwood."""
from components import T, catalog, feature, quote, section, tags

PEOPLE = [
    ("CH-ROLAND", ("Captain Roland", "Hauptmann Roland"), ("Captain of the watch", "Hauptmann der Wache"),
     ("Town Hall & Watch House", "Rathaus & Wachhaus"),
     ("A tired, decent border captain with too much road to guard and too few people to guard it. He gives you your first "
      "task and most of the ones after it.",
      "Ein müder, anständiger Grenzhauptmann mit zu viel Straße zum Bewachen und zu wenig Leuten dafür. Er gibt dir deine erste "
      "Aufgabe und die meisten danach."),
     ("You can hold a weapon? Good. That puts you ahead of most of my watch.",
      "Du kannst eine Waffe halten? Gut. Damit bist du den meisten meiner Wache voraus.")),
    ("CH-BRON", ("Bron", "Bron"), ("Drill master · Paladin guild", "Drillmeister · Paladin-Gilde"),
     ("Barracks & Training Yard", "Kaserne & Übungsplatz"),
     ("Gruff, loud, and right more often than anyone likes. Bron has trained every guard in Hayn.",
      "Barsch, laut und öfter im Recht, als irgendwem lieb ist. Bron hat jede Wache in Hayn ausgebildet."),
     ("Shield up. Again.", "Schild hoch. Nochmal.")),
    ("CH-HAGEN", ("Hagen", "Hagen"), ("Ranger master · Ranger guild", "Rangermeister · Ranger-Gilde"),
     ("Hunters' Lodge", "Jägerhütte"),
     ("Quiet. Hagen knows the Wolfwood better than anyone alive, and was the first to notice the pack changing.",
      "Ruhig. Hagen kennt den Wolfwood besser als jeder andere, und er hat als Erster bemerkt, dass sich das Rudel verändert."),
     ("They're not hungry. That's what worries me.", "Sie sind nicht hungrig. Das macht mir Sorgen.")),
    ("CH-MIRA", ("Mira", "Mira"), ("Herbalist · White Mage guild", "Kräuterkundige · Weißmagier-Gilde"),
     ("Herbalist's House & Spring Shrine", "Kräuterhaus & Quellschrein"),
     ("Warm and practical, and a Shumadii, one of the elf-like people from another world. Mira patches up the town, sells herbs, and teaches healing at the old spring shrine in her garden.",
      "Warmherzig und praktisch, und eine Shumadii vom elfenhaften Volk aus einer anderen Welt. Mira flickt die Stadt zusammen, verkauft Kräuter und lehrt das Heilen am alten Quellschrein in ihrem Garten."),
     ("Sit. Drink this. Then tell me which wolf.", "Setz dich. Trink das. Dann sag mir, welcher Wolf.")),
    ("CH-ELWYN", ("Elwyn", "Elwyn"), ("The mage · Elementalist guild", "Der Magier · Elementaristen-Gilde"),
     ("Elwyn's Tower", "Elwyns Turm"),
     ("A Shumadii, one of the elf-like people from another world, older than anyone in Hayn can remember. Curious and slightly distracted, with candles melted onto stacks of books. The red glow in the tower window at night "
      "is the only magic most townsfolk ever see.",
      "Ein Shumadii aus dem elfenhaften Volk einer anderen Welt, älter, als sich irgendwer in Hayn erinnern kann. Neugierig und etwas zerstreut, mit Kerzen, die auf Bücherstapeln heruntergebrannt sind. Das rote Leuchten im "
      "Turmfenster ist die einzige Magie, die die meisten Stadtbewohner je sehen."),
     ("Ah, a student. Mind the books. And the floor. And that.", "Ah, ein Schüler. Pass auf die Bücher auf. Und den Boden. Und darauf.")),
    ("CH-HALDOR", ("Hermann", "Hermann"), ("The smith", "Der Schmied"), ("The forge", "Die Schmiede"),
     ("Hermann sells weapons and armour, buys pelts, and will teach anyone with five pelts and some iron how to make a pair of bracers.",
      "Hermann verkauft Waffen und Rüstungen, kauft Felle und bringt jedem, der fünf Felle und etwas Eisen hat, bei, wie man Armschienen macht."),
     ("Pelts. Not scraps. Pelts.", "Felle. Keine Fetzen. Felle.")),
]

OTHERS = [
    (("The innkeeper", "Der Wirt"), ("Runs the Golden Acorn. Bed, food and a place to come back to.", "Führt die Goldene Eichel. Bett, Essen und ein Ort, zu dem man zurückkehrt.")),
    (("The storekeeper", "Der Krämer"), ("Potions, rope, lamps and bags, on the square.", "Tränke, Seile, Lampen und Taschen, am Platz.")),
    (("The woodcutter", "Der Holzfäller"), ("At the forest edge, with something to say about the wolves.", "Am Waldrand, mit etwas zu den Wölfen zu sagen.")),
    (("The merchant", "Der Händler"), ("Waiting at the Dais for someone to see his cart to Frankfurt.", "Wartet am Dais auf jemanden, der seinen Karren nach Frankfurt bringt.")),
    (("The wounded scout", "Der verwundete Kundschafter"), ("Found on the road, past the ambush.", "Auf der Straße zu finden, hinter dem Hinterhalt.")),
    (("Townsfolk", "Stadtbewohner"), ("Guards, vendors, a baker, a miller, children, a bard in the inn, and a dog that chases the cat.", "Wachen, Händler, ein Bäcker, ein Müller, Kinder, ein Barde im Gasthaus und ein Hund, der die Katze jagt.")),
]


def people(ctx):
    t = ctx.t
    rows = []
    for k, (img, name, role, where, text, line) in enumerate(PEOPLE):
        body = f'<p class="job-role" style="font-size:1rem;color:var(--glyph)">{T(ctx, role)}</p><p>{T(ctx, text)}</p>{tags(ctx, [where])}'
        rows.append(feature(ctx, img, None, name, body, flip=k % 2 == 1, extra=quote(ctx, line, name)))
    others = "".join(f'<div class="mode"><h3>{T(ctx, a)}</h3><p>{T(ctx, b)}</p></div>' for a, b in OTHERS)
    return section(f"""
<p class="lede" style="margin-bottom:64px">{t("Short, grounded and a little dry: the people who run Hayn and send you out of it.",
                     "Kurz, bodenständig und ein wenig trocken: die Leute, die Hayn am Laufen halten und dich hinausschicken.")}</p>
{"".join(rows)}
<h2 style="margin-top:80px">{t("Also in town", "Außerdem in der Stadt")}</h2>
<div class="modes">{others}</div>""")


def creatures(ctx):
    t = ctx.t
    return section(f"""
{catalog(ctx, [
    (ctx.pick("ACT-CR-01", "CR-01", "KA-05"), ("Grey wolf", "Grauer Wolf"), ("Packs of two or three that flank you, and give up the chase if you run far enough. Level 2–3.",
                                           "Rudel zu zweit oder dritt, die dich flankieren und aufgeben, wenn du weit genug läufst. Stufe 2–3.")),
    ("CR-01", ("Dark wolf", "Dunkler Wolf"), ("The deep-wood variant: packs of three, a harder bite and a howl that strengthens the pack. Level 4.",
                                             "Die Variante aus dem tiefen Wald: Rudel zu dritt, ein härterer Biss und ein Heulen, das das Rudel stärkt. Stufe 4.")),
    (ctx.pick("ACT-CR-02", "CR-02", "KA-07"), ("The Alpha", "Der Alpha"), ("Charcoal fur, a heavy mane, a torn ear. The first boss of the vertical slice. Level 5, elite.",
                                         "Kohlschwarzes Fell, eine schwere Mähne, ein zerrissenes Ohr. Der erste Boss der Vertical Slice. Stufe 5, Elite.")),
    ("CR-03", ("Wild boar", "Wildschwein"), ("Alone, and charges in a straight line you can see coming. Level 3.",
                                           "Allein unterwegs, und greift in einer geraden Linie an, die du kommen siehst. Stufe 3.")),
    ("CR-04", ("Red deer", "Rothirsch"), ("A stag and a hind. Harmless, and part of what makes the forest feel alive.",
                                         "Ein Hirsch und eine Hirschkuh. Harmlos, und Teil dessen, was den Wald lebendig wirken lässt.")),
    ("CR-08", ("Brown bear", "Braunbär"), ("Not in the vertical slice for certain. If it comes, it lives deep in the spruce.",
                                          "In der Vertical Slice noch nicht sicher. Wenn er kommt, lebt er tief im Fichtenwald.")),
])}
<p class="lede" style="margin-top:56px">{t("Past the wolves, bandits wait on the road east, and the dead of an old wolf-cult guard the barrow beneath the hill.",
                                         "Hinter den Wölfen lauern Banditen auf der Straße nach Osten, und die Toten eines alten Wolfskults bewachen das Hügelgrab unter dem Hügel.")}</p>""")


PAGES = {
    "characters/index.html": dict(
        title=("People of Hayn", "Die Leute von Hayn"), kicker=("Characters", "Figuren"),
        lede=("A captain, four guild masters, a smith, and the town around them.",
              "Ein Hauptmann, vier Gildenmeister, ein Schmied und die Stadt um sie herum."),
        banner="KA-02", body=people),
    "characters/creatures.html": dict(
        title=("Creatures", "Kreaturen"), kicker=("Characters", "Figuren"),
        lede=("Realistic animals first. The Wolfwood is dangerous because it is real.",
              "Zuerst realistische Tiere. Der Wolfwood ist gefährlich, weil er echt ist."),
        banner="KA-05", body=creatures),
}
