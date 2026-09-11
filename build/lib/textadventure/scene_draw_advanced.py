class AdvancedSceneDraw:
    """
    Disegno avanzato della stanza in ASCII:
    - bordi squadrati
    - porte (N, S, E, W)
    - oggetti
    - posizione del giocatore
    """

    def __init__(self, width=20, height=8, doors=None, objects=None, player_pos=None):
        self.width = width
        self.height = height
        self.doors = doors or set()        # es: {"N", "S"}
        self.objects = objects or {}       # es: {(5, 3): "O"}
        self.player_pos = player_pos       # es: (10, 4)

    def draw(self):
        lines = []

        # riga superiore
        top = "+" + "-" * self.width + "+"
        if "N" in self.doors:
            mid = self.width // 2
            top = "+" + "-" * mid + " " + "-" * (self.width - mid - 1) + "+"
        lines.append(top)

        # righe centrali
        for y in range(self.height):
            row = []
            for x in range(self.width):
                char = " "

                # oggetto
                if (x, y) in self.objects:
                    char = self.objects[(x, y)]

                # giocatore
                if self.player_pos == (x, y):
                    char = "@"

                row.append(char)

            line = "|" + "".join(row) + "|"

            # porta Ovest/Est
            if "W" in self.doors and y == self.height // 2:
                line = " " + line[1:]
            if "E" in self.doors and y == self.height // 2:
                line = line[:-1] + " "

            lines.append(line)

        # riga inferiore
        bottom = "+" + "-" * self.width + "+"
        if "S" in self.doors:
            mid = self.width // 2
            bottom = "+" + "-" * mid + " " + "-" * (self.width - mid - 1) + "+"
        lines.append(bottom)

        return "\n".join(lines)
