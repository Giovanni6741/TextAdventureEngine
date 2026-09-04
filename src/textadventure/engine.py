class GameEngine:
    def __init__(self, initial_scene, state, parser):
        self.scene = initial_scene
        self.state = state
        self.parser = parser

    def run(self):
        # Finché esiste una scena, il gioco continua
        while self.scene is not None:
            # Esegui la scena corrente
            next_scene = self.scene.enter(self.state, self.parser)

            # Aggiorna la scena corrente
            self.scene = next_scene

        # Quando self.scene diventa None, il ciclo termina
        return
