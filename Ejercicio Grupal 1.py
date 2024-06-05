#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_player = int(input('How many are you? '))
name_player = input('Say your name: ')

attempt = 5
for i in range(5):
    user_input = int(input('Enter word: '))

    if user_input == #palabras ocultas:
        print('You won!')
        break
    else:
        print(f'Try again! {attempt} left.')
        attempt -= 1
        continue


# In[39]:


import json
import random

with open("palabras.json") as f:
    data = json.loads(f.read())
    
num_players = 0
lista1 = []

while True:
    num_players = int(input("¿cuántos jugadores hay? "))
    lista1 = input("Inserta los nombres con espacio: ").split()
    if len(lista1) == num_players:
        print('Verdad')
        break
    else:
        print('El número de jugadores debe corresponder al número de nombres')

diccionario = {}

for i in range(len(lista1)):
    diccionario[lista1[i]] = 0
print(diccionario)

while True: 
    num = random.randint(0, 10)
    print(num)
    print('La pista es: ', data[num]['pista'])
    contador = 0

    while contador < len(lista1):
        oportunidades = 0
        while oportunidades < 3:
            print('Bienvenido,', lista1[contador])
            respuesta = input("¿Qué es? ")
            if respuesta == data [num]["palabra"]:
                diccionario[lista1[contador]] += 1
                print('Felicidades')
                break
            else:
                print('Sigue intentandolo')
            #diccionario[lista1[contador]] = 0
            oportunidades += 1
        contador += 1
    ronda = input('¿Quieres seguir jugando? Responde con un si o no: ')
    if ronda.lower() == 'si':
        print('continuamos jugando')
    else:
        print(diccionario)
        break


# In[ ]:




