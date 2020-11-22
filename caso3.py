"""
JORDI RIULAS
22/11/2020
EJERCICIO H4CK#3 R3C4P: CASO 3
"""
"""
ENUNCIADO:

1. Crear una variable llamada
world que permita crear una
relación llave valor, siendo llave
el ecosistema emprendedor y
valor el conjunto de startups de
ese ecosistema.
2. Crear los 3 ecosistemas
siguientes: “Silicon Valley”,
“Matadepera Valley” y “Livers
Valley”.
"""



#definición de funciones y objetos

def display_ecosystem(lista_startups):
  for startup in lista_startups:
    print (startup)
  return

def add_startups_ecosystem(startups):
  new_startup = input ("INTRODUZCA NOMBRE STARTUP DE ECOSISTEMA o 0 para SALIR: ")
  startups.append(new_startup)
  #print ("NUEVA STARTUP: ",new_startup)
  while new_startup != "0": 
    new_startup = input ("INTRODUZCA NUEVA STARTUP ? o 0 para SALIR: ")
    #print ("NUEVA STARTUP:",new_startup)
    startups.append(new_startup)
  print ("LISTA DE STARTUPS DEL ECOSISTEMA: ")
  display_ecosystem (startups) 
  return

#inicialización de variables

startups_silicon_valley = []
startups_matadepera_valley = []
startups_liver_valley = []

#creación de variables globales
world = {
  "Silicon Valley" : startups_silicon_valley,
  "Matadepera Valley" : startups_matadepera_valley,
  "Livers Valley" : startups_liver_valley
}

#ejecución de programa
add_startups_ecosystem(world["Silicon Valley"])
add_startups_ecosystem(world["Matadepera Valley"])
add_startups_ecosystem(world["Livers Valley"])
print (world)
