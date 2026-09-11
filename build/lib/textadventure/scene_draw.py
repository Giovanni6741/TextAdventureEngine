class SceneDraw:
    """
    Disegna una stanza ASCII con bordi squadrati.
    """

    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height

    def draw(self):
        top = "+" + "-" * self.width + "+"
        middle = "|" + " " * self.width + "|"
        return "\n".join([top] + [middle for _ in range(self.height)] + [top])
