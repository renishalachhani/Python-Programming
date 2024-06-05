#!/usr/bin/env python
# coding: utf-8

# In[56]:


import json
import random
import os

with open("palabras.json") as f:
    data = json.loads(f.read())
    
num_players = 0
lista1 = []

if os.path.isfile("usuarios.json"):
    with open("usuarios.json") as f:
    #data = json.loads(f.read())

while True:
    num_players = int(input("¿cuántos jugadores hay? "))
    lista1 = input("Inserta los nombres con espacio: ").split()
    if len(lista1) == num_players:
        break
    else:
        print('El número de jugadores debe corresponder al número de nombres\n')

        
diccionario = {}

for i in range(len(lista1)):
    diccionario[lista1[i]] = 0
print(diccionario)

contador_rondas = 0

def mover_izquierda(lista1):
    return lista1[1:] + [lista1[0]]

while contador_rondas < 3: 
    num = random.randint(0, 9)
    #print(num)
    print('Estamos en la ronda ', contador_rondas + 1, "\n")
    print('La pista es: ', data[num]['pista'],'\n')
    contador = 0

    while contador < len(lista1):
        oportunidades = 0
        while oportunidades < 1:
            print('Bienvenido,', lista1[contador])
            respuesta = input("¿Qué es? \n")
            if respuesta == data[num]["palabra"]:
                diccionario[lista1[contador]] += 1
                print('Felicidades\n')
                break
            else:
                print('Sigue intentandolo\n')
            #diccionario[lista1[contador]] = 0
            oportunidades += 1
        contador += 1
    #ronda = input('¿Quieres seguir jugando? Responde con un si o no: ')
    #if ronda.lower() == 'si':
        #print('continuamos jugando')
    #else:
        #print(diccionario)
        #break
    contador_rondas += 1
    lista1 = mover_izquierda(lista1)
    print(lista1)
print(diccionario)

sr = json.dumps(diccionario)
json_convertido = json.loads(sr)
with open('usuarios.json', 'w') as f:
    json.dump(json_convertido, f, indent='\t')


# In[ ]:




