# map_draw_advanced.py
class AdvancedMapDraw:
    """
    Minimappa avanzata completa:
    - icone ASCII avanzate
    - heatmap
    - wireframe
    - zoom
    - radar
    - colori ANSI
    - cornice
    """

    ICON_MAP = {
        "Start": "⌂",
        "Corridoio": "⌁",
        "Tesoro": "★",
        "Boss": "☠",
        "NPC": "⚑",
        "Shop": "✪",
        "Puzzle": "⌘",
        "Danger": "⚔",
    }

    HEATMAP_COLORS = {
        0: "\033[32m",
        1: "\033[33m",
        2: "\033[38;5;208m",
        3: "\033[31m",
    }

    RADAR_COLORS = {
        0: "\033[36m",
        1: "\033[32m",
        2: "\033[33m",
        3: "\033[38;5;208m",
        4: "\033[31m",
    }

    PLAYER_COLOR = "\033[36m"
    DOOR_COLOR = "\033[90m"
    RESET = "\033[0m"

    def __init__(self, game_state, show_coords=False, wireframe=False, zoom=None, radar=False):
        self.state = game_state
        self.show_coords = show_coords
        self.wireframe = wireframe
        self.zoom = zoom
        self.radar = radar

    # --- porte raw e colorate ---
    def _get_doors_raw(self, x, y):
        return {
            "N": (x, y - 1) in self.state.map,
            "S": (x, y + 1) in self.state.map,
            "W": (x - 1, y) in self.state.map,
            "E": (x + 1, y) in self.state.map,
        }

    def _get_doors(self, x, y):
        raw = self._get_doors_raw(x, y)
        doors = []
        if raw["N"]: doors.append("↑")
        if raw["S"]: doors.append("↓")
        if raw["W"]: doors.append("←")
        if raw["E"]: doors.append("→")
        if doors:
            return self.DOOR_COLOR + "".join(doors) + self.RESET
        return ""

    # --- icona con heatmap (metodo mancante nella tua versione) ---
    def _get_icon(self, x, y):
        room_type = self.state.map.get((x, y), "")
        icon = self.ICON_MAP.get(room_type, "■")
        danger_level = getattr(self.state, "danger", {}).get((x, y), 0)
        color = self.HEATMAP_COLORS.get(danger_level, "\033[37m")
        return color + icon + self.RESET

    # --- simboli wireframe ---
    def _get_wireframe_symbol(self, x, y):
        raw = self._get_doors_raw(x, y)
        symbol = "●"
        if getattr(self.state, "player_pos", None) == (x, y):
            return self.PLAYER_COLOR + "@" + self.RESET

        north = raw["N"]
        south = raw["S"]
        west = raw["W"]
        east = raw["E"]

        if north and south and west and east:
            return "┼"
        if north and south:
            return "│"
        if west and east:
            return "─"
        if north and east:
            return "└"
        if north and west:
            return "┘"
        if south and east:
            return "┌"
        if south and west:
            return "┐"
        return symbol

    # --- radar color per cell ---
    def _get_radar_color(self, x, y):
        px, py = getattr(self.state, "player_pos", (None, None))
        if px is None:
            return ""
        dist = int(((x - px)**2 + (y - py)**2)**0.5)
        return self.RADAR_COLORS.get(dist, self.RADAR_COLORS[4])

    # --- disegno principale ---
    def draw(self):
        if not getattr(self.state, "map", None):
            return "[Mappa vuota]"

        # area visibile (zoom) oppure tutta la mappa
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
                    if self.wireframe:
                        symbol = self._get_wireframe_symbol(x, y)
                    else:
                        symbol = self._get_icon(x, y)
                        if getattr(self.state, "player_pos", None) == (x, y):
                            symbol = self.PLAYER_COLOR + "@" + self.RESET
                        symbol += self._get_doors(x, y)
                else:
                    symbol = "\033[90m·\033[0m"

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
