from textadventure.engine import GameEngine
from textadventure.scene import Scene
from textadventure.state import State
from textadventure.parser import Parser

class DummyScene(Scene):
    def __init__(self, next_scene=None):
        self.next_scene = next_scene

    def enter(self, state, parser):
        return self.next_scene

def test_engine_runs_until_none():
    # Scena 1 → Scena 2 → None
    scene2 = DummyScene(None)
    scene1 = DummyScene(scene2)

    engine = GameEngine(scene1, State(), Parser())
    engine.run()

    # Il motore deve fermarsi con scene = None
    assert engine.scene is None
