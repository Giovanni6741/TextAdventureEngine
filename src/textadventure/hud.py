class HUD:
    """
    Mostra una barra HUD con informazioni sullo stato del giocatore.
    """

    def __init__(self, state):
        self.state = state

    def draw(self):
        hp = getattr(self.state, "hp", "?")
        scene = getattr(self.state, "current_scene", "?")
        return f"[HP: {hp}] [Stanza: {scene}]"
