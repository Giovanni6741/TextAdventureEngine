class MapDraw:
    """
    Disegna una minimappa ASCII basata sulle coordinate delle stanze.
    """

    def __init__(self, game_state):
        self.state = game_state

    def draw(self):
        if not self.state.map:
            return "[Mappa vuota]"

        xs = [p[0] for p in self.state.map]
        ys = [p[1] for p in self.state.map]

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        out = []
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                row.append("■" if (x, y) in self.state.map else "·")
            out.append(" ".join(row))

        return "\n".join(out)
