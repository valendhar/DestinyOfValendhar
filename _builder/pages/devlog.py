"""DevLog: videos of the project, sorted into series (categories), each series oldest first.

To add a video:
1. python _Docs/Tools/devlog_thumb.py <loom link>   (saves its thumbnail as DL-<first 8 of the id> and prints its length)
2. add an entry at the END of VIDEOS: the Loom id, its series (a key of SERIES), its length, the month, a short title
   (the series name is shown beside it, so don't repeat it) and a line in English and German.
A new series is one more entry in SERIES and one line in site_map.py under DevLog. The pages, the tabs, the grid and
the "Latest" page follow by themselves.
"""
from html import escape

from components import section

SERIES = {
    "greyboxing": dict(
        path="devlog/greyboxing.html", name=("Town greyboxing", "Greyboxing der Stadt"),
        lede=("Hayn blocked out in Unreal Engine, before anything is modeled.", "Hayn in der Unreal Engine als Blöcke angelegt, bevor etwas modelliert wird."),
        text=("Simple blocks for every building, street, wall and gate, walked through to check the town's size and feel. Each "
              "part picks up where the last one stopped.",
              "Einfache Blöcke für jedes Gebäude, jede Gasse, Mauer und jedes Tor, zu Fuß abgelaufen, um Größe und Gefühl der "
              "Stadt zu prüfen. Jeder Teil macht dort weiter, wo der letzte aufgehört hat.")),
    "gameplay": dict(
        path="devlog/gameplay.html", name=("Gameplay greyboxing", "Gameplay-Greyboxing"),
        lede=("The game's systems blocked out and tested before they go into the town.",
              "Die Systeme des Spiels als Rohbau angelegt und getestet, bevor sie in die Stadt kommen."),
        text=("Greyboxing for how the game plays rather than how it looks: on the Bootcamp, a plain test map next to the town, "
              "quests, jobs and guilds are built and tried out one at a time, and only what works moves into Hayn.",
              "Greyboxing dafür, wie sich das Spiel spielt, nicht wie es aussieht: Auf dem Bootcamp, einer schlichten Testkarte "
              "neben der Stadt, werden Quests, Jobs und Gilden einzeln gebaut und ausprobiert, und nur was funktioniert, "
              "kommt nach Hayn.")),
}

# oldest first; the newest is the last one
VIDEOS = [
    dict(loom="69c90e95a88d42f2b42c090bd647b8b0", series="greyboxing", ratio="4 / 3", minutes=("2½ min", "2½ Min."), when=("November 2026", "November 2026"),
         title=("The first walk through the town", "Der erste Gang durch die Stadt"),
         text=("The first walk through Hayn in Unreal Engine: simple blocks for every building, the streets, the wall and the gates, "
               "to check that the town has the right size and feels right before anything is modeled.",
               "Der erste Gang durch Hayn in der Unreal Engine: einfache Blöcke für jedes Gebäude, die Gassen, die Mauer und die Tore, "
               "um zu prüfen, ob die Stadt die richtige Größe hat und sich richtig anfühlt, bevor etwas modelliert wird.")),
    dict(loom="35b0e525d46b45db979834cd7fd38fc8", series="greyboxing", ratio="4 / 3", minutes=("2½ min", "2½ Min."), when=("November 2026", "November 2026"),
         title=("Timber frames and trees", "Fachwerk und Bäume"),
         text=("The greybox one step further, recorded just before the town's design changed: the first timber-framed buildings "
               "stand in the streets, simple trees mark the green, and the player walks through it all with the game's interface on screen. "
               "The next update brings the stone wall and the new gates.",
               "Das Greyboxing einen Schritt weiter, aufgenommen kurz bevor sich das Design der Stadt geändert hat: Die ersten "
               "Fachwerkhäuser stehen in den Gassen, einfache Bäume markieren die Grünflächen, und die Spielfigur geht mit der "
               "Spieloberfläche durch alles hindurch. Das nächste Update bringt die Steinmauer und die neuen Tore.")),
    dict(loom="6844cb63b5f64c5aa861ddb8af9ee488", series="gameplay", ratio="4 / 3", minutes=("2 min", "2 Min."), when=("November 2026", "November 2026"),
         title=("The first quest", "Die erste Quest"),
         text=("A testing ground built next to the town, where each gameplay system is tried out on its own before it goes into the "
               "real world. This first greybox area tests quests: the player takes on a task, the objectives track each step, and the "
               "quest completes. Small and plain on purpose, so that what works here can later be placed in Hayn with confidence.",
               "Ein Testgelände neben der Stadt, auf dem jedes Gameplay-System für sich ausprobiert wird, bevor es in die echte Welt "
               "kommt. Dieser erste Greybox-Bereich testet Quests: Die Spielfigur nimmt eine Aufgabe an, die Ziele verfolgen jeden "
               "Schritt, und die Quest wird abgeschlossen. Bewusst klein und schlicht, damit das, was hier funktioniert, später mit "
               "Sicherheit in Hayn eingebaut werden kann.")),
    dict(loom="73aadce009fd426cb5bf49760992f193", series="gameplay", ratio="4 / 3", minutes=("3 min", "3 Min."), when=("November 2026", "November 2026"),
         title=("Jobs, cursors and selection", "Jobs, Mauszeiger und Auswahl"),
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
    dict(loom="fc35adab12c64f4795c0f056c6a3b894", series="gameplay", ratio="4 / 3", minutes=("1½ min", "1½ Min."), when=("November 2026", "November 2026"),
         title=("Joining the guilds", "Den Gilden beitreten"),
         text=("Each of the four guilds now has a dialog where you ask to join, and joining is what unlocks its job. A new bar of "
               "four job buttons fills in as you join: one for the Paladin, the Ranger, the White Mage and the Elementalist. Click one "
               "and you switch jobs on the spot, and the main hotbar swaps in that job's skills, which made it easy to check that "
               "every job carries the right abilities.",
               "Jede der vier Gilden hat jetzt einen Dialog, in dem du um Aufnahme bittest, und erst der Beitritt schaltet ihren Job "
               "frei. Eine neue Leiste mit vier Job-Knöpfen füllt sich, während du beitrittst: je einer für Paladin, Ranger, Weißmagier "
               "und Elementarist. Ein Klick wechselt den Job sofort, und die Hauptleiste tauscht die Fähigkeiten dieses Jobs ein, "
               "so ließ sich leicht prüfen, dass jeder Job die richtigen Fähigkeiten mitbringt.")),
    dict(loom="4cf242cf300d44aa8edab4b84bb31e00", series="gameplay", ratio="4 / 3", minutes=("2½ min", "2½ Min."), when=("November 2026", "November 2026"),
         title=("The Paladin's trial and quest markers", "Die Prüfung des Paladins und Quest-Markierungen"),
         text=("The first job now has to be earned. The Paladin guild sets a short chain of trial quests, one leading to the next, and "
               "finishing it is what teaches you the Paladin job. Along with it come quest markers above people's heads, so you can read "
               "the town at a glance: one marker shows who has a new quest for you, and a different one shows who is waiting for you to "
               "hand a finished quest in.",
               "Den ersten Job muss man sich jetzt verdienen. Die Paladin-Gilde stellt eine kurze Kette von Prüfungsquests, eine führt "
               "zur nächsten, und erst wer sie abschließt, lernt den Job des Paladins. Dazu kommen Quest-Markierungen über den Köpfen der "
               "Leute, damit man die Stadt auf einen Blick lesen kann: Eine Markierung zeigt, wer eine neue Quest für dich hat, eine andere, "
               "wer darauf wartet, dass du eine erledigte Quest abgibst.")),
]


def thumb_id(v):
    return "DL-" + v["loom"][:8].upper()


def part_no(v):
    return [x["loom"] for x in VIDEOS if x["series"] == v["series"]].index(v["loom"]) + 1


def card(ctx, v, show_series=False):
    """One video as a card. Without JavaScript it is a link to the video on Loom; site.js turns it into a button that
    opens the viewer on this page. Everything the viewer shows travels in data- attributes."""
    t = ctx.t
    s = SERIES[v["series"]]
    title = t(*v["title"])
    label = t(*s["name"]) if show_series else t(f"Part {part_no(v)}", f"Teil {part_no(v)}")
    img = ctx.img_src(thumb_id(v)) if ctx.has(thumb_id(v)) else ""
    pic = f'<img src="{img}" alt="" loading="lazy" decoding="async" width="640" height="368">' if img else '<span class="dl-noimg"></span>'
    return (f'<li class="dl-card" id="v-{v["loom"][:8]}"><a class="dl-open" href="https://www.loom.com/share/{v["loom"]}" target="_blank" rel="noopener" '
            f'data-loom="{v["loom"]}" data-title="{escape(title)}" data-label="{escape(label)}" '
            f'data-meta="{escape(t(*v["when"]) + ", " + t(*v["minutes"]))}" data-text="{escape(t(*v["text"]))}" data-ratio="{v["ratio"]}">'
            f'<span class="dl-thumb">{pic}<span class="dl-play" aria-hidden="true"></span><span class="dl-len">{t(*v["minutes"])}</span></span>'
            f'<span class="dl-label">{label}</span><span class="dl-title">{title}</span></a></li>')


def viewer(ctx):
    t = ctx.t
    return (f'<dialog class="dl-viewer" aria-labelledby="dl-v-title"><div class="dl-v-frame"></div>'
            f'<div class="dl-v-text"><p class="dl-v-label"></p><h2 id="dl-v-title"></h2><p class="dl-v-meta"></p><p class="dl-v-body"></p>'
            f'<p class="dl-v-links"><a class="text-link dl-v-loom" target="_blank" rel="noopener">{t("Watch on Loom", "Auf Loom ansehen")}</a></p>'
            f'<div class="dl-v-nav"><button type="button" class="dl-v-prev">{t("Previous part", "Voriger Teil")}</button>'
            f'<button type="button" class="dl-v-next">{t("Next part", "Nächster Teil")}</button></div></div>'
            f'<button type="button" class="dl-v-close" aria-label="{t("Close", "Schließen")}">×</button></dialog>')


def latest(ctx):
    t = ctx.t
    v = VIDEOS[-1]
    s = SERIES[v["series"]]
    newest = f"""<article class="devlog-entry dl-latest">
  <div class="devlog-video" style="aspect-ratio:{v['ratio']}">
    <iframe src="https://www.loom.com/embed/{v['loom']}" title="{t(*v['title'])}" loading="eager"
      allow="fullscreen; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
  </div>
  <div class="devlog-text">
    <p class="kicker"><a href="{ctx.url(s['path'])}">{t(*s['name'])}</a>, {t(f'part {part_no(v)}', f'Teil {part_no(v)}')}</p>
    <h2>{t(*v['title'])}</h2>
    <p>{t(*v['text'])}</p>
    <p class="dl-meta">{t(*v['when'])}, {t(*v['minutes'])}</p>
  </div>
</article>"""
    rows = []
    for key, s in SERIES.items():
        vids = [x for x in VIDEOS if x["series"] == key]
        if not vids:
            continue
        n = len(vids)
        count = t(f"{n} part" + ("s" if n != 1 else ""), f"{n} Teil" + ("e" if n != 1 else ""))
        rows.append(f"""<section class="dl-row">
  <div class="dl-row-head"><h2><a href="{ctx.url(s['path'])}">{t(*s['name'])}</a></h2><span class="dl-count">{count}</span></div>
  <p class="dl-row-text">{t(*s['text'])}</p>
  <ol class="dl-grid">{"".join(card(ctx, x) for x in vids)}</ol>
</section>""")
    intro = t("Short videos from the work itself, as the game takes shape: the newest first, then every series from its start.",
              "Kurze Videos aus der Arbeit selbst, während das Spiel Gestalt annimmt: das neueste zuerst, dann jede Reihe von Anfang an.")
    return section(f'<p class="devlog-intro">{intro}</p>{newest}<h2 class="dl-all">{t("All series", "Alle Reihen")}</h2>{"".join(rows)}{viewer(ctx)}')


def series_page(key):
    def body(ctx):
        s = SERIES[key]
        vids = [x for x in VIDEOS if x["series"] == key]
        return section(f'<p class="devlog-intro">{ctx.t(*s["text"])}</p><ol class="dl-grid dl-grid-big">{"".join(card(ctx, x) for x in vids)}</ol>{viewer(ctx)}')
    return body


PAGES = {
    "devlog/index.html": dict(
        title=("DevLog", "DevLog"),
        lede=("The project at its different stages, on video.", "Das Projekt in seinen verschiedenen Phasen, im Video."),
        banner=None, body=latest),
}
for _k, _s in SERIES.items():
    PAGES[_s["path"]] = dict(title=_s["name"], lede=_s["lede"], banner=None, body=series_page(_k))
