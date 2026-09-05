class Parser:
    def parse(self, command: str, state):
        """
        Interpreta il comando dell'utente.
        Deve restituire una scena oppure None.
        La logica reale sarà implementata dal gioco.
        """
        action = command.strip().lower()

        # Esempio di comportamento minimale
        if action in ("exit", "quit", "esci"):
            return None

        # Il gioco vero sostituirà questa parte
        if hasattr(state, "default_next_scene"):
            return state.default_next_scene

        return None
