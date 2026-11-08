"""DevLog: videos of the project at its different stages, newest first.

To add a video, put a new entry at the top of VIDEOS with its Loom share ID (the part after /share/ in the link),
a title and a line in English and German, and its aspect ratio (Loom's oEmbed gives the width and height).
"""
from components import section

VIDEOS = [
    dict(loom="35b0e525d46b45db979834cd7fd38fc8", ratio="4 / 3", minutes=("2½ minutes", "2½ Minuten"), when=("November 2026", "November 2026"),
         title=("Greyboxing, part two", "Greyboxing, Teil zwei"),
         text=("The greybox one step further, recorded just before the town's design changed: the first timber-framed buildings "
               "stand in the streets, simple trees mark the green, and the player walks through it all with the game's interface on screen. "
               "The next update brings the stone wall and the new gates.",
               "Das Greyboxing einen Schritt weiter, aufgenommen kurz bevor sich das Design der Stadt geändert hat: Die ersten "
               "Fachwerkhäuser stehen in den Gassen, einfache Bäume markieren die Grünflächen, und die Spielfigur geht mit der "
               "Spieloberfläche durch alles hindurch. Das nächste Update bringt die Steinmauer und die neuen Tore.")),
    dict(loom="69c90e95a88d42f2b42c090bd647b8b0", ratio="4 / 3", minutes=("2½ minutes", "2½ Minuten"), when=("November 2026", "November 2026"),
         title=("Initial town greyboxing", "Erstes Greyboxing der Stadt"),
         text=("The first walk through Hayn in Unreal Engine: simple blocks for every building, the streets, the wall and the gates, "
               "to check that the town has the right size and feels right before anything is modeled.",
               "Der erste Gang durch Hayn in der Unreal Engine: einfache Blöcke für jedes Gebäude, die Gassen, die Mauer und die Tore, "
               "um zu prüfen, ob die Stadt die richtige Größe hat und sich richtig anfühlt, bevor etwas modelliert wird.")),
]


def devlog(ctx):
    t = ctx.t
    items = []
    for n, v in enumerate(VIDEOS):
        title = t(*v["title"])
        items.append(f"""<article class="devlog-entry">
  <div class="devlog-video" style="aspect-ratio:{v['ratio']}">
    <iframe src="https://www.loom.com/embed/{v['loom']}" title="{title}" loading="{'eager' if n == 0 else 'lazy'}"
      allow="fullscreen; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
  </div>
  <div class="devlog-text">
    <p class="kicker">{t(*v['when'])} · {t(*v['minutes'])}</p>
    <h2>{title}</h2>
    <p>{t(*v['text'])}</p>
    <p><a class="text-link" href="https://www.loom.com/share/{v['loom']}" target="_blank" rel="noopener">{t("Watch on Loom", "Auf Loom ansehen")}</a></p>
  </div>
</article>""")
    intro = t("Short videos from the work itself, as the game takes shape. The newest comes first.",
              "Kurze Videos aus der Arbeit selbst, während das Spiel Gestalt annimmt. Das neueste steht oben.")
    return section(f'<p class="devlog-intro">{intro}</p>' + "".join(items))


PAGES = {
    "devlog/index.html": dict(
        title=("DevLog", "DevLog"), kicker=("DevLog", "DevLog"),
        lede=("The project at its different stages, on video.", "Das Projekt in seinen verschiedenen Phasen, im Video."),
        banner=None, body=devlog),
}
