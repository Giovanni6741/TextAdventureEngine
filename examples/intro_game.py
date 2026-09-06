from textadventure import Scene, GameEngine, Parser, State


class Intro(Scene):
    def enter(self, state, parser):
        print("\n=== INTRO ===")
        print("Ti svegli in una stanza buia. Una porta è davanti a te.")
        print("Comandi disponibili: apri porta, esci")

        command = input("> ")
        return parser.parse(command, state)


class Stanza(Scene):
    def enter(self, state, parser):
        print("\n=== STANZA ===")
        print("La porta si apre. Entri in una stanza illuminata da una torcia.")
        print("C'è un tavolo con un oggetto misterioso.")
        print("Comandi disponibili: guarda oggetto, esci")

        command = input("> ")
        return parser.parse(command, state)


class Oggetto(Scene):
    def enter(self, state, parser):
        print("\n=== OGGETTO ===")
        print("È una piccola chiave antica. Potrebbe aprire qualcosa...")
        print("Comandi disponibili: esci")

        command = input("> ")
        return parser.parse(command, state)


class AdventureParser(Parser):
    def parse(self, command, state):
        cmd = command.strip().lower()

        if cmd in ("exit", "quit", "esci"):
            print("Hai deciso di terminare l'avventura.")
            return None

        if cmd == "apri porta":
            return state.scenes["stanza"]

        if cmd == "guarda oggetto":
            return state.scenes["oggetto"]

        print("Comando non riconosciuto.")
        return state.scenes["intro"]


class AdventureState(State):
    def __init__(self):
        super().__init__()
        self.scenes = {}


def main():
    state = AdventureState()

    # Creazione delle scene
    intro = Intro()
    stanza = Stanza()
    oggetto = Oggetto()

    # Registrazione delle scene nello stato
    state.scenes = {
        "intro": intro,
        "stanza": stanza,
        "oggetto": oggetto,
    }

    parser = AdventureParser()
    engine = GameEngine(intro, state, parser)
    engine.run()


if __name__ == "__main__":
    main()
