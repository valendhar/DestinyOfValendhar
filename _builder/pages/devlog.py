"""DevLog: videos of the project at its different stages, newest first.

To add a video, put a new entry at the top of VIDEOS with its Loom share ID (the part after /share/ in the link),
a title and a line in English and German, and its aspect ratio (Loom's oEmbed gives the width and height).
"""
from components import section

VIDEOS = [
    dict(loom="fc35adab12c64f4795c0f056c6a3b894", ratio="4 / 3", minutes=("1½ minutes", "1½ Minuten"), when=("November 2026", "November 2026"),
         title=("Gameplay bootcamp: joining the guilds", "Gameplay-Bootcamp: den Gilden beitreten"),
         text=("Each of the four guilds now has a dialog where you ask to join, and joining is what unlocks its job. A new bar of "
               "four job buttons fills in as you join: one for the Paladin, the Ranger, the White Mage and the Elementalist. Click one "
               "and you switch jobs on the spot, and the main hotbar swaps in that job's skills, which made it easy to check that "
               "every job carries the right abilities.",
               "Jede der vier Gilden hat jetzt einen Dialog, in dem du um Aufnahme bittest, und erst der Beitritt schaltet ihren Job "
               "frei. Eine neue Leiste mit vier Job-Knöpfen füllt sich, während du beitrittst: je einer für Paladin, Ranger, Weißmagier "
               "und Elementarist. Ein Klick wechselt den Job sofort, und die Hauptleiste tauscht die Fähigkeiten dieses Jobs ein, "
               "so ließ sich leicht prüfen, dass jeder Job die richtigen Fähigkeiten mitbringt.")),
    dict(loom="73aadce009fd426cb5bf49760992f193", ratio="4 / 3", minutes=("3 minutes", "3 Minuten"), when=("November 2026", "November 2026"),
         title=("Gameplay bootcamp: jobs, cursors and selection", "Gameplay-Bootcamp: Jobs, Mauszeiger und Auswahl"),
         text=("Three systems that make the town readable and the hero flexible. The cursor now changes as it passes over people: "
               "a merchant, a trainer or a guard each shows their own, and someone with a quest for you shows whether it is new, "
               "under way or ready to hand in, so you know who to talk to before you click. Clicking a person puts a selection "
               "ring at their feet. And the job system is in: a character can switch between the jobs they have unlocked, so the "
               "same hero can be a Paladin today and a Ranger tomorrow.",
               "Drei Systeme, die die Stadt lesbar und die Spielfigur wandelbar machen. Der Mauszeiger ändert sich jetzt über "
               "Personen: Händler, Ausbilder oder Wache zeigen jeweils ihren eigenen, und wer eine Quest für dich hat, zeigt, ob sie "
               "neu, in Arbeit oder abgabebereit ist, damit du weißt, mit wem du sprechen solltest, bevor du klickst. Ein Klick auf "
               "eine Person legt einen Auswahlring zu ihren Füßen. Und das Job-System ist da: Eine Figur kann zwischen den Jobs "
               "wechseln, die sie freigeschaltet hat, sodass derselbe Held heute Paladin und morgen Ranger sein kann.")),
    dict(loom="6844cb63b5f64c5aa861ddb8af9ee488", ratio="4 / 3", minutes=("2 minutes", "2 Minuten"), when=("November 2026", "November 2026"),
         title=("Gameplay bootcamp: the first quest", "Gameplay-Bootcamp: die erste Quest"),
         text=("A testing ground built next to the town, where each gameplay system is tried out on its own before it goes into the "
               "real world. This first greybox area tests quests: the player takes on a task, the objectives track each step, and the "
               "quest completes. Small and plain on purpose, so that what works here can later be placed in Hayn with confidence.",
               "Ein Testgelände neben der Stadt, auf dem jedes Gameplay-System für sich ausprobiert wird, bevor es in die echte Welt "
               "kommt. Dieser erste Greybox-Bereich testet Quests: Die Spielfigur nimmt eine Aufgabe an, die Ziele verfolgen jeden "
               "Schritt, und die Quest wird abgeschlossen. Bewusst klein und schlicht, damit das, was hier funktioniert, später mit "
               "Sicherheit in Hayn eingebaut werden kann.")),
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
