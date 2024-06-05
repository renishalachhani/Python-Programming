import json
import time
# import random


def leer_json():
  with open("palabras.json", "r") as file:
    return json.load(file)



palabras = leer_json()  

#print(type(palabras[0]))

nombres = []

puntuaciones = {}

while True:

  nombre = input("Introduzca su nombre: ")

  if nombre == "fin":

    break

  nombres.append(nombre)

  puntuaciones[nombre] = 0


print(nombres)


#palabra = random.choice(palabras)

for palabra in palabras:

  print(palabra["pista"])

  x = 0

  while True:


    print("Usuario: ", nombres[x], "es su turno")

    tiempo_inicio = time.time()
    usuario_eleccion = input("Introduzca una palabra: ")
    tiempo_fin = time.time()
    limite_tiempo = 5
    

    elapsed_time = tiempo_fin - tiempo_inicio
    if elapsed_time > limite_tiempo:
        print("¡Tiempo agotado,", nombres[x] + "!")
        nombres.append(nombres[x])
        nombres.pop(0)
        break



    if usuario_eleccion == palabra["palabra"]:

      print("Enhorabuena, el usuario: ", nombres[x], "ha acertado la palabra")

      puntuaciones[nombres[x]] += 1

      nombres.append(nombres[x])

      nombres.pop(0)

      #print(nombres)
      break

    else:
      print("Lo siento, el usuario: ", nombres[x], "no ha acertado la palabra")
      nombres.append(nombres[x])
      nombres.pop(0)

      print(nombres)

       
print(puntuaciones)