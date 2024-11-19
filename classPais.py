from classContinente import Continente

class Pais(Continente):
    def __init__(self):
        super().__init__()
        self._moneda_oficial = ""
        self._idioma_oficial = ""
        self._poblacion = 0

    def get_moneda_oficial(self):
        return self._moneda_oficial

    def set_moneda_oficial(self, moneda):
        self._moneda_oficial = moneda

    def get_idioma_oficial(self):
        return self._idioma_oficial

    def set_idioma_oficial(self, idioma):
        self._idioma_oficial = idioma

    def get_poblacion(self):
        return self._poblacion

    def set_poblacion(self, poblacion):
        self._poblacion = poblacion

    def mostrar_informacion_pais(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Superficie: {self.get_superficie()} km²")
        print(f"Población: {self.get_poblacion()}")
        print(f"Moneda oficial: {self.get_moneda_oficial()}")
        print(f"Idioma oficial: {self.get_idioma_oficial()}")
