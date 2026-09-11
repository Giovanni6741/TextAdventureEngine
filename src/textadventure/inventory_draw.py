class InventoryDraw:
    """
    Disegna l'inventario del giocatore in formato ASCII.
    """

    def __init__(self, inventory):
        self.inventory = inventory

    def draw(self):
        if not self.inventory:
            return "[Inventario vuoto]"
        return "\n".join(f"- {item}" for item in self.inventory)
