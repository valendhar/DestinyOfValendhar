"""Navigation tree for the whole site.

Each node: ((english label, german label), path, children)
- path is relative to the language root, e.g. "world/hayn.html"
  (the German copy of every page lives under de/ with the same path)
- a node with children and a path gets a "landing" link plus a dropdown
"""

NAV = [
    (("Home", "Start"), "index.html", []),
    (("The Game", "Das Spiel"), "game/index.html", [
        (("Overview & Pillars", "Überblick & Säulen"), "game/index.html", []),
        (("Combat", "Kampf"), "game/combat.html", []),
        (("The Four Jobs", "Die vier Jobs"), "game/jobs.html", []),
        (("Town Life", "Stadtleben"), "game/town-life.html", []),
    ]),
    (("The Journey", "Die Reise"), "journey/index.html", [
        (("From Portal to Watchtower", "Vom Portal zur Warte"), "journey/index.html", []),
        (("The Quest Chain", "Die Questreihe"), "journey/quests.html", []),
        (("The Alpha", "Der Alpha"), "journey/the-alpha.html", []),
    ]),
    (("World", "Welt"), "world/index.html", [
        (("Valendhar", "Valendhar"), "world/index.html", []),
        (("Hayn", "Hayn"), "world/hayn.html", []),
        (("The Wolfwood", "Der Wolfwood"), "world/wolfwood.html", []),
        (("Road to Frankfurt", "Straße nach Frankfurt"), "world/road.html", []),
    ]),
    (("Characters", "Figuren"), "characters/index.html", [
        (("People of Hayn", "Die Leute von Hayn"), "characters/index.html", []),
        (("Creatures", "Kreaturen"), "characters/creatures.html", []),
    ]),
    (("Art", "Kunst"), "art/index.html", [
        (("Key Art", "Key Art"), "art/index.html", []),
        (("Views & Maps", "Ansichten & Karten"), "art/views.html", []),
        (("Interiors", "Innenräume"), "art/interiors.html", []),
    ]),
    (("Concept Art", "Konzeptkunst"), "concept/index.html", [
        (("Overview", "Überblick"), "concept/index.html", []),
        (("Heroes", "Helden"), "concept/heroes.html", []),
        (("People of Hayn", "Die Leute von Hayn"), "concept/people.html", []),
        (("Creatures & Enemies", "Kreaturen & Gegner"), "concept/creatures.html", []),
        (("Buildings & Landmarks", "Gebäude & Wahrzeichen"), "concept/buildings.html", []),
        (("Props & Interiors", "Requisiten & Innenräume"), "concept/props.html", []),
        (("Wolfwood & Barrow", "Wolfwood & Hügelgrab"), "concept/wolfwood.html", []),
        (("Modular Kit", "Baukasten"), "concept/kit.html", []),
        (("Historical", "Historisch"), "concept/historical.html", []),
        (("Gear & Costumes", "Ausrüstung & Kostüme"), "concept/gear.html", []),
    ]),
    (("DevLog", "DevLog"), "devlog/index.html", [
        (("Latest", "Neuestes"), "devlog/index.html", []),
        (("Town greyboxing", "Greyboxing der Stadt"), "devlog/greyboxing.html", []),
        (("Gameplay greyboxing", "Gameplay-Greyboxing"), "devlog/gameplay.html", []),
    ]),
    (("Media", "Medien"), "media/index.html", []),
]


def all_paths(nodes=NAV):
    """Every page path in nav order, with its breadcrumb trail of (en, de) labels."""
    out = []

    def walk(items, trail):
        for label, path, kids in items:
            if path and path not in [p for p, _ in out]:
                out.append((path, trail + [label]))
            walk(kids, trail + [label])

    walk(nodes, [])
    return out
