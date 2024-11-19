from classPais import Pais

class Tonga(Pais):
    def __init__(self):
        super().__init__()
        self._monarca_actual = ""

    def get_monarca_actual(self):
        return self._monarca_actual

    def set_monarca_actual(self, monarca):
        self._monarca_actual = monarca

    def informacion_tonga(self):
        self.mostrar_informacion_pais()
        print(f"Monarca actual: {self.get_monarca_actual()}")
