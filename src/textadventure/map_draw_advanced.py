class AdvancedMapDraw:
    """
    Minimappa ASCII avanzata:
    - icone ASCII avanzate
    - heatmap
    - wireframe
    - zoom
    - radar (cerchi concentrici)
    - colori ANSI
    - cornice
    """

    RADAR_COLORS = {
        0: "\033[36m",      # Ciano (giocatore)
        1: "\033[32m",      # Verde
        2: "\033[33m",      # Giallo
        3: "\033[38;5;208m",# Arancione
        4: "\033[31m",      # Rosso
    }

    RESET = "\033[0m"

    def __init__(self, game_state, show_coords=False, wireframe=False, zoom=None, radar=False):
        self.state = game_state
        self.show_coords = show_coords
        self.wireframe = wireframe
        self.zoom = zoom
        self.radar = radar

    def _get_radar_color(self, x, y):
        """Colora la cella in base alla distanza dal giocatore."""
        px, py = getattr(self.state, "player_pos", (None, None))
        if px is None:
            return ""

        dist = int(((x - px)**2 + (y - py)**2)**0.5)

        if dist in self.RADAR_COLORS:
            return self.RADAR_COLORS[dist]
        return self.RADAR_COLORS[4]  # rosso per distanze grandi

    def draw(self):
        if not self.state.map:
            return "[Mappa vuota]"

        # --- ZOOM ---
        if self.zoom is not None and getattr(self.state, "player_pos", None):
            px, py = self.state.player_pos
            min_x = px - self.zoom
            max_x = px + self.zoom
            min_y = py - self.zoom
            max_y = py + self.zoom
        else:
            xs = [p[0] for p in self.state.map]
            ys = [p[1] for p in self.state.map]
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)

        content = []

        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):

                if (x, y) in self.state.map:

                    # wireframe
                    if self.wireframe:
                        symbol = self._get_wireframe_symbol(x, y)
                    else:
                        symbol = self._get_icon(x, y)

                        # giocatore
                        if getattr(self.state, "player_pos", None) == (x, y):
                            symbol = "\033[36m@\033[0m"

                        # porte
                        symbol += self._get_doors(x, y)

                else:
                    symbol = "\033[90m·\033[0m"

                # --- RADAR COLOR ---
                if self.radar:
                    color = self._get_radar_color(x, y)
                    symbol = color + symbol + self.RESET

                if self.show_coords:
                    symbol = f"{symbol}({x},{y})"

                row.append(symbol)

            content.append(" ".join(row))

        width = max(len(line) for line in content)
        top = "+" + "-" * width + "+"
        bottom = "+" + "-" * width + "+"

        framed = [top] + [f"|{line.ljust(width)}|" for line in content] + [bottom]

        return "\n".join(framed)
