"""
JORDI RIULAS
22/11/2020
EJERCICIO H4CK#3 R3C4P: CASO 2
"""
"""
ENUNCIADO:
Crear una función llamada
add_startups_ecosystem() que no
acepta ningún parámetro pero puede
iterar las N veces necesarias,
añadiendo una startup (que
introducirá el usuario) en cada
iteración hasta que el usuaria no
quiera añadir ninguna más (Por
ejemplo: introduce el valor 0 para
finalizar.)
"""

#definición de funciones y objetos

def display_ecosystem(lista_startups):
  for startup in lista_startups:
    print (startup)
  return

def add_startups_ecosystem():
  new_startup = input ("INTRODUZCA NOMBRE STARTUP o 0 para SALIR: ")
  print ("NUEVA STARTUP: ",new_startup)
  while new_startup != "0": 
    new_startup = input ("INTRODUZCA NUEVA STARTUP ? o 0 para SALIR: ")
    print ("NUEVA STARTUP:",new_startup)
    startups.append(new_startup)
  print ("LISTA DE STARTUPS: ", startups)
  return


#inicialización de variables
startups = []

#ejecución de programa
add_startups_ecosystem()
display_ecosystem(startups)
