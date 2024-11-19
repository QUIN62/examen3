from classPais import Pais

class Corea(Pais):
    def __init__(self):
        super().__init__()
        self._lider_actual = ""

    def get_lider_actual(self):
        return self._lider_actual

    def set_lider_actual(self, lider_actual):
        self._lider_actual = lider_actual

    def informacion_corea(self):
        self.mostrar_informacion_pais()
        print(f"Líder actual: {self.get_lider_actual()}")
