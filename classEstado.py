from classMexico import Mexico

class Estado(Mexico):
    def __init__(self):
        super().__init__()
        self._platillo_tipico = ""

    def get_platillo(self):
        return self._platillo_tipico

    def set_platillo(self, platillo):
        self._platillo_tipico = platillo

    def mostrar_informacion_estado(self):
        self.mostrar_informacion_mexico()
        print(f"Platillo típico: {self.get_platillo()}")
