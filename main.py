from classTonga import Tonga
from classCorea import Corea
from classEstado import Estado

# Crear objetos
tonga = Tonga()
tonga.set_nombre("Tonga")
tonga.set_superficie(720)
tonga.set_poblacion(109000)
tonga.set_moneda_oficial("Pa'anga")
tonga.set_idioma_oficial("Inglés y tongano")
tonga.set_monarca_actual("Tupou VI")

corea = Corea()
corea.set_nombre("Corea del Norte")
corea.set_superficie(97480)
corea.set_poblacion(26200000)
corea.set_moneda_oficial("Won norcoreano")
corea.set_idioma_oficial("Coreano")
corea.set_lider_actual("Kim Jong Un")

estado = Estado()
estado.set_nombre("Hidalgo")
estado.set_superficie(29900)
estado.set_poblacion(3006000)
estado.set_moneda_oficial("Peso mexicano")
estado.set_idioma_oficial("Español")
estado.set_presidente_actual("Claudia Sheinbaum")
estado.set_platillo("Barbacoa de borrego")
estado.set_nombre_patrimonio("Acueducto del Padre Tembleque")

# Mostrar información
print("Información de Tonga:\n")
tonga.informacion_tonga()

print("\nInformación de Corea del Norte:\n")
corea.informacion_corea()

print("\nInformación del Estado de Hidalgo:\n")
estado.mostrar_informacion_estado()
