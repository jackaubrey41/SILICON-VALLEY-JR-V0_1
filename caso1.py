"""
JORDI RIULAS
22/11/2020
EJERCICIO H4CK#3 R3C4P: CASO 1
"""
"""
ENUNCIADO:
Generar una función llamada
display_ecosystem() que permita
listar por consola las startups del
ecosistema Silicon Valley.
"""

#definición de funciones y objetos

def display_ecosystem(lista_startups):
  for startup in lista_startups:
    print (startup)
  return

#inicialización de variables
startups = ["Happee","Linbits","BMT"]

#ejecución de programa
display_ecosystem(startups)
