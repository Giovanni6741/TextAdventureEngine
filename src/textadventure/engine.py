from .scene import Scene
from .parser import Parser
from .state import State

class GameEngine:
    def __init__(self, initial_scene: Scene, state: State, parser: Parser):
        self.scene = initial_scene
        self.state = state
        self.parser = parser

    def run(self):
        """
        Esegue il ciclo principale del gioco.
        Continua finché la scena corrente non restituisce None.
        """
        while self.scene is not None:
            next_scene = self.scene.enter(self.state, self.parser)
            self.scene = next_scene
