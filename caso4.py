"""
JORDI RIULAS
22/11/2020
EJERCICIO H4CK#3 R3C4P: CASO 4
"""
"""
ENUNCIADO:

Adaptar las funciones de
display_ecosystem() y
add_startups_ecosystem() para
que funcionen con el nuevo modelo
de datos.
La primera preguntará al usuario si
quiere mostrar un ecosistema en
particular o todos a la vez..
Para la segunda, modificarla para que
acepte un parámetro que será el
ecosistema al que añadir las nuevas
start ups. Indicar al usuario el
ecosistema al que se añadirán las
nuevas startups.
"""

#inicialización de variables

startups_silicon_valley = []
startups_matadepera_valley = []
startups_liver_valley = []

#creación de variables globales
# world es un dicionario con clave nombre ecosistema y valor lista de startups
# esta estructura no permitirá añadir nuevso ecosistemas
# accederemos a la lista mediante la clave

world = {
  "Silicon Valley" : startups_silicon_valley,
  "Matadepera Valley" : startups_matadepera_valley,
  "Livers Valley" : startups_liver_valley
}


#definición de funciones y objetos

def display_ecosystem():
  option_print = input ("\n PRINT ONE ECOSYSTEM (0) or WORLD (1): ")
  if option_print == "0":
    option_ecosystem = input ("SELECT TO PRINT: Silicon Valley (0), Matadepera Valley(1), Livers valey (2): ")
    if option_ecosystem == "0":
        print(world["Silicon Valley"])
    elif option_ecosystem == "1":
        print(world["Matadepera Valley"])
    elif option_ecosystem == "2":
        print(world["Livers Valley"])
    else:
      print ( "SALGO 0")
  else:
    print (world)

  
  return

def add_startups_ecosystem(startups_list):
  new_startup = input ("INTRO NEW STARTUP FOR ECOSYSTEM OR 0 TO EXIT: ")
  while new_startup != "0": 
    startups_list.append(new_startup)
    print ("NEW STARTUP ADDED: ",new_startup)
    #preguntamos por la siguiente startup si no hemos salido con 0
    new_startup = input ("INTRO NEW STARTUP OR 0 TO EXIT: ")
  return

#CABECERA
print ("*** WELLCOME TO WORLD STARTUPS DATA BASE *** \n")
#print("ECOSYSTEMS REGISTERED:","\n",world.keys(),"\n")

"""
EJECUCIÓN DEL PROGRAMA
"""

#test añadir a un ecosistema
#add_startups_ecosystem(world["Silicon Valley"])

#recorremos las listas de startups del diciconario
#para cada elemento del diccionario:  ecosystem = [startups_list]
for ecosystemx,startups_listx in world.items():
  print("ECOSYSTEM", ecosystemx ,":")
  add_startups_ecosystem(startups_listx)

# imprimir ecosystem
display_ecosystem()
