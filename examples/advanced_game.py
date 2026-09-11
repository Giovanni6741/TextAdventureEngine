from textadventure import (
    GameEngine,
    Scene,
    Parser,
    State,
    AdvancedSceneDraw,
    AdvancedMapDraw,
)


# ============================
#  SCENE PERSONALIZZATE
# ============================

class Entrance(Scene):
    def enter(self, state, parser):
        print("\n=== INGRESSO ===")
        print("Ti trovi all'ingresso di un antico dungeon.")
        print("Comandi: guarda stanza, mappa, avanti, inventario, esci")

        cmd = input("> ")
        return parser.parse(cmd, state)


class Corridor(Scene):
    def enter(self, state, parser):
        print("\n=== CORRIDOIO ===")
        print("Un lungo corridoio illuminato da torce.")
        print("Comandi: guarda stanza, mappa, avanti, indietro, inventario, esci")

        cmd = input("> ")
        return parser.parse(cmd, state)


class TreasureRoom(Scene):
    def enter(self, state, parser):
        print("\n=== SALA DEL TESORO ===")
        print("Una stanza piena di monete d'oro.")
        print("Comandi: guarda stanza, mappa, prendi oro, indietro, inventario, esci")

        cmd = input("> ")
        return parser.parse(cmd, state)


# ============================
#  PARSER AVANZATO
# ============================

class AdventureParser(Parser):
    def parse(self, command, state):
        cmd = command.strip().lower()

        # movimento
        if cmd == "avanti":
            if state.player_pos == (0, 0):
                state.player_pos = (1, 0)
                return state.scenes["corridor"]
            if state.player_pos == (1, 0):
                state.player_pos = (1, 1)
                return state.scenes["treasure"]

        if cmd == "indietro":
            if state.player_pos == (1, 1):
                state.player_pos = (1, 0)
                return state.scenes["corridor"]
            if state.player_pos == (1, 0):
                state.player_pos = (0, 0)
                return state.scenes["entrance"]

        # inventario
        if cmd == "prendi oro":
            state.inventory.append("Monete d'oro")
            print("Hai preso delle monete d'oro.")
            return state.scenes["treasure"]

        # HUD / MAPPA / STANZA
        if cmd == "inventario":
            print("\n=== INVENTARIO ===")
            for item in state.inventory:
                print(f"- {item}")
            return state.scenes[state.current_scene]

        if cmd == "mappa":
            print("\n=== MINIMAPPA ===")
            drawer = AdvancedMapDraw(
                state,
                radar=True,
                zoom=2,
                wireframe=False,
            )
            print(drawer.draw())
            return state.scenes[state.current_scene]

        if cmd == "guarda stanza":
            print("\n=== STANZA ===")
            drawer = AdvancedSceneDraw(
                width=30,
                height=10,
                doors={"N", "E"},
                objects={(5, 3): "O"},
                player_pos=(10, 5),
            )
            print(drawer.draw())
            return state.scenes[state.current_scene]

        # uscita
        if cmd in ("esci", "exit", "quit"):
            print("Hai deciso di terminare l'avventura.")
            return None

        print("Comando non riconosciuto.")
        return state.scenes[state.current_scene]


# ============================
#  STATO DI GIOCO
# ============================

class AdventureState(State):
    def __init__(self):
        super().__init__()
        self.scenes = {}
        self.player_pos = (0, 0)
        self.inventory = []

        # mappa del dungeon
        self.map = {
            (0, 0): "Start",
            (1, 0): "Corridoio",
            (1, 1): "Tesoro",
        }

        # heatmap dei pericoli
        self.danger = {
            (0, 0): 0,
            (1, 0): 1,
            (1, 1): 2,
        }


# ============================
#  MAIN
# ============================

def main():
    state = AdventureState()

    entrance = Entrance()
    corridor = Corridor()
    treasure = TreasureRoom()

    state.scenes = {
        "entrance": entrance,
        "corridor": corridor,
        "treasure": treasure,
    }

    parser = AdventureParser()
    engine = GameEngine(entrance, state, parser)
    engine.run()


if __name__ == "__main__":
    main()
