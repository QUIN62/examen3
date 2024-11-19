from classPais import Pais
from classPatrimonio import Patrimonio

class Mexico(Pais, Patrimonio):
    def __init__(self):
        Pais.__init__(self)
        Patrimonio.__init__(self)
        self._presidente_actual = ""

    def get_presidente_actual(self):
        return self._presidente_actual

    def set_presidente_actual(self, presidente):
        self._presidente_actual = presidente

    def mostrar_informacion_mexico(self):
        self.mostrar_informacion_pais()
        print(f"Presidente actual: {self.get_presidente_actual()}")
        print(f"Patrimonio: {self.get_nombre_patrimonio()}")
