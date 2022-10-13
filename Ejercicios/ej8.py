# Databricks notebook source
num_de_participantes = int(input('¿Cuantás personas participarán?: '))
diccionario = {}
maximo = None
minimo = None
for i in range(num_de_participantes):
    participante = str(input(f'¿Cuál es el nombre del participante {i + 1}?: '))
    numero = int(input(f'Menciona un número participante {i+1}: '))
    diccionario[i+1] = [participante, numero]
    print([participante, numero])
    if maximo == None:
        maximo = numero
    else:
        if numero > maximo:
            maximo = numero
        else:
            pass
    if minimo == None:
        minimo = numero
    else:
        if numero < minimo:
            minimo = numero
        else:
            pass

print('El número más pequeño fue: ', minimo)
print('El número más grande fue ', maximo)
    
