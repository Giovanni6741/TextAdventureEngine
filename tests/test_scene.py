import pytest
from textadventure.scene import Scene

def test_scene_enter_not_implemented():
    scene = Scene()
    with pytest.raises(NotImplementedError):
        scene.enter(None, None)
