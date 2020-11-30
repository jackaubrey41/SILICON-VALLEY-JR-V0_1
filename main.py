"""
ON WORK . NOT FINISHED
JORDI RIULAS
29/11/2020
EJERCICIO H4CK#3 R3C4P: CASO 5
"""
"""
ENUNCIADO:

Al llamar a esta función, el programa
hará lo siguiente:
1. Lanzar un mensaje de
bienvenida.
2. Mostrar un menú con dos
opciones: [1] Mostrar
ecosistemas y [2] Añadir
startups. [0] Salir del programa.
Aseguraros que solo puede
introducir una opción valida.
"""

#inicialización de variables

startups_silicon_valley = ["Happee", "Linbits", "BMT"]
startups_matadepera_valley = ["Lime", "Uber"]
startups_liver_valley = ["Coinbase", "Airbnb"]

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
  option_print = input ("[1]: LOOK ONE ECOSYSTEM\n[2]: LOOK WORLD\n[0]: EXIT\nOPTION: ")
  valid_input0 = False
  while valid_input0 == False : 
    if option_print == "1":
      option_ecosystem = input ("SELECT ECOSYSTEM:\n[1]: Silicon Valley\n[2]: Matadepera Valley\n[3]: Livers Valley\n[0]: EXIT\nOPTION: ")
      valid_input1 = False
      while valid_input1 == False:
        if option_ecosystem == "1":
          print(world["Silicon Valley"])
          valid_input1 = True
        elif option_ecosystem == "2":
          print(world["Matadepera Valley"])
          valid_input1 = True
        elif option_ecosystem == "3":
          print(world["Livers Valley"])
          valid_input1 = True
        elif option_ecosystem == "0":
          print ("EXIT, SEE YOU SOON(1)")
          valid_input1 = True
        else:
          option_ecosystem = input("CHOOSE VALID OPTION(1): ")
          valid_input1 = False
      
      valid_input0 = True
    elif option_print == "2":
      print (world)
      valid_input0 = True
    elif option_print == "0":
      print ("EXIT, SEE YOU SOON(0)")
      valid_input0 = True
    else:
      option_print = input("CHOOSE VALID OPTION(0): ")
      valid_input0 = False
  return



def add_startups_ecosystem(startups_list):
  new_startup = input ("INTRO NEW STARTUP FOR ECOSYSTEM OR 0 TO EXIT: ")
  while new_startup != "0": 
    startups_list.append(new_startup)
    print ("NEW STARTUP ADDED: ",new_startup)
    #preguntamos por la siguiente startup si no hemos salido con 0
    new_startup = input ("INTRO NEW STARTUP OR 0 TO EXIT: ")
  return

"""
EJECUCIÓN DEL PROGRAMA
"""
#CABECERA
print ("*** WELLCOME TO WORLD STARTUPS DATA BASE *** \n")
print ("CHOOSE ONE OPTION: \n")
print ("[1]: LOOK EXISTING WORLD STARTUPS")
print ("[2]: ADD NEW STARTUPS TO WORLD ")
print ("[O]: EXIT ")
option = input("OPTION: ")
#print("ECOSYSTEMS REGISTERED:","\n",world.keys(),"\n")
if option == "1":
  display_ecosystem()
elif option == "2":
#recorremos las listas de startups del diciconario
#para cada elemento del diccionario:  ecosystem = [startups_list]
  for ecosystemx,startups_listx in world.items():
    print("ECOSYSTEM", ecosystemx ,":")
    add_startups_ecosystem(startups_listx)
elif option == "0":
  print ("EXIT, SEE YOU SOON")
else:
  pass