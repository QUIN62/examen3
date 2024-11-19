class Continente:
    def __init__(self):
        self._superficie = 0
        self._nombre = ""

    def get_superficie(self):
        return self._superficie

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre
