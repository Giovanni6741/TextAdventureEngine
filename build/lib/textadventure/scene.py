class Scene:
    def enter(self, state, parser):
        """
        Metodo principale della scena.
        Deve:
        - mostrare il testo
        - chiedere input
        - usare il parser
        - aggiornare lo stato
        - restituire la scena successiva
        """
        raise NotImplementedError("Ogni scena deve implementare enter()")
