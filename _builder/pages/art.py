"""Art: key art, views and maps, interiors, and a media page that is still to come."""
from components import section


def key_art(ctx):
    t = ctx.t
    swatches = [
        ("#F1E9D8", t("Lime plaster", "Kalkputz")), ("#1F1A15", t("Black beams", "Schwarze Balken")),
        ("#7A2E22", t("Oxblood beams", "Ochsenblutbalken")), ("#7A3A26", t("Clay tile", "Tonziegel")),
        ("#E2A63E", t("Autumn sun", "Herbstsonne")), ("#8FD3EA", t("Portal rune", "Portalrune")),
    ]
    sw = "".join(f'<li><span class="swatch" style="background:{c}"></span><span class="sw-name">{n}</span>'
                 f'<span class="sw-hex">{c}</span></li>' for c, n in swatches)
    return section(f"""
<div class="intro" style="margin-bottom:64px">
  <div class="prose">
    <p class="big">{t("Semi-realistic painted concept art, in the quality of a modern fantasy RPG: real proportions and materials, "
                      "a painterly finish, never cartoony and never a photograph.",
                      "Halbrealistische, gemalte Konzeptkunst in der Qualität eines modernen Fantasy-Rollenspiels: echte Proportionen "
                      "und Materialien, ein malerischer Abschluss, nie comichaft und nie ein Foto.")}</p>
    <p>{t("The default light is late afternoon in early autumn: a warm low sun, long shadows, cool blue shade, chimney smoke and "
          "the first golden leaves in the beeches. Dawn mist and lantern-lit nights are the alternates.",
          "Das Standardlicht ist später Nachmittag im Frühherbst: eine warme, tiefe Sonne, lange Schatten, kühle blaue Schatten, "
          "Kaminrauch und die ersten goldenen Blätter in den Buchen. Morgennebel und laternenbeleuchtete Nächte sind die Alternativen.")}</p>
  </div>
  <div><ul class="swatches swatches-3">{sw}</ul></div>
</div>
{ctx.gallery([
    ("KA-01", t("The main street at golden hour", "Die Hauptgasse zur goldenen Stunde")),
    ("KA-02", t("Market day around the fountain", "Markttag am Brunnen")),
    ("KA-03", t("Arrival at the Rune Portal", "Ankunft am Runenportal")),
    ("KA-04", t("The forge", "Die Schmiede")),
    ("KA-05", t("Wolves at the forest edge", "Wölfe am Waldrand")),
    ("KA-06", t("Inside the Wolfwood", "Im Wolfwood")),
    ("KA-07", t("The wolf den", "Der Wolfsbau")),
    ("KA-08", t("Hayn at night", "Hayn bei Nacht")),
    ("KA-09", t("Misty dawn at the mill pond", "Nebliger Morgen am Mühlteich")),
], "gallery-2")}""")


def views(ctx):
    t = ctx.t
    return section(f"""
<h2>{t("From above", "Von oben")}</h2>
{ctx.gallery([
    ("BE-01", t("Aerial from the south-east", "Luftbild von Südosten")),
    ("BE-02", t("From the north-west, over the forest", "Von Nordwesten, über den Wald")),
], "gallery-2")}
<h2 style="margin-top:72px">{t("Around the town", "Rund um die Stadt")}</h2>
{ctx.gallery([
    ("VW-01", t("From the watchtower, looking south", "Vom Wachturm nach Süden")),
    ("VW-02", t("The square and the town hall", "Der Platz und das Rathaus")),
    ("VW-03", t("Through the west postern", "Durch die Westpforte")),
    ("VW-04", t("The Paladin training yard", "Der Paladin-Übungsplatz")),
    ("VW-05", t("Hunters' Lodge and archery range", "Jägerhütte und Bogenschießplatz")),
    ("VW-06", t("Herbalist's garden and spring shrine", "Kräutergarten und Quellschrein")),
    ("VW-07", t("Elwyn's tower courtyard", "Der Hof von Elwyns Turm")),
    ("VW-08", t("The road out of town", "Die Straße aus der Stadt")),
    ("VW-09", t("The farmstead and fields", "Der Bauernhof und die Felder")),
    ("VW-10", t("From the forest ridge", "Vom Waldkamm")),
], "gallery-2 gallery-169")}
<h2 style="margin-top:72px">{t("Maps", "Karten")}</h2>
{ctx.gallery([
    ("TD-02", t("Painted map of Hayn", "Gemalte Karte von Hayn")),
    ("TD-04", t("Painted map of the Wolfwood", "Gemalte Karte des Wolfwoods")),
    ("TD-05", t("Layout grid of Hayn", "Lageplan von Hayn mit Raster")),
], "gallery-2")}""")


def interiors(ctx):
    t = ctx.t
    return section(ctx.gallery([
        ("IT-01", t("The inn taproom", "Die Gaststube")),
        ("IT-02", t("The forge", "Die Schmiede")),
        ("IT-03", t("The council chamber", "Der Ratssaal")),
        ("IT-04", t("Watch room and armoury", "Wachstube und Waffenkammer")),
        ("IT-05", t("A town kitchen and living room", "Küche und Stube eines Stadthauses")),
        ("IT-06", t("Bedroom and attic", "Schlafkammer und Dachboden")),
        ("IT-07", t("The bakery", "Die Bäckerei")),
        ("IT-08", t("The herbalist's workroom", "Die Werkstatt der Kräuterkundigen")),
        ("IT-09", t("The mage tower study", "Die Studierstube im Magierturm")),
        ("IT-10", t("Inside the Hunters' Lodge", "In der Jägerhütte")),
        ("IT-11", t("The barracks", "Die Kaserne")),
        ("IT-12", t("The chapel", "Die Kapelle")),
        ("IT-13", t("The general store", "Der Krämerladen")),
        ("IT-14", t("The inn cellar", "Der Gasthauskeller")),
        ("IT-15", t("The watermill", "Die Wassermühle")),
    ], "gallery-3 gallery-169"))


def media(ctx):
    t = ctx.t
    return section(f"""<div class="stub"><p class="kicker">{t("Coming later", "Kommt später")}</p>
<h2>{t("Screenshots and video", "Screenshots und Videos")}</h2>
<p>{t("In-engine screenshots and a trailer will appear here once the vertical slice is playable. Until then, everything on this "
      "site is concept art.",
      "Screenshots aus der Engine und ein Trailer erscheinen hier, sobald die Vertical Slice spielbar ist. Bis dahin ist alles auf "
      "dieser Seite Konzeptkunst.")}</p>
<a class="btn btn-ghost" href="{ctx.url('art/index.html')}">{t("See the concept art", "Zur Konzeptkunst")}</a></div>""")


PAGES = {
    "art/index.html": dict(
        title=("Key Art", "Key Art"), kicker=("Art", "Kunst"),
        lede=("Painted concept art for Hayn and the Wolfwood.", "Gemalte Konzeptkunst für Hayn und den Wolfwood."),
        banner="KA-08", body=key_art),
    "art/views.html": dict(
        title=("Views & Maps", "Ansichten & Karten"), kicker=("Art", "Kunst"),
        lede=("The town from the air, from its streets, and on the map.", "Die Stadt aus der Luft, aus ihren Gassen und auf der Karte."),
        banner="VW-02", body=views),
    "art/interiors.html": dict(
        title=("Interiors", "Innenräume"), kicker=("Art", "Kunst"),
        lede=("Behind the doors you can open.", "Hinter den Türen, die sich öffnen lassen."),
        banner="IT-05", body=interiors),
    "media/index.html": dict(
        title=("Media", "Medien"), kicker=("Media", "Medien"),
        lede=("Screenshots and video from the game itself, once there is something to show.",
              "Screenshots und Videos aus dem Spiel selbst, sobald es etwas zu zeigen gibt."),
        banner="KA-03", body=media),
}
