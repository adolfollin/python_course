# Databricks notebook source
import math
minutos = int(input('¿Cuántos minutos desea estar en el estacionamiento?: '))

while(minutos < 0):
    if minutos == 0:
        break
    elif minutos < 0:
        minutos = int(input('El valor no puede ser negativo, porfavor ingrese un valor positiivo ¿Cuántos minutos desea pasar?: '))
    else:
        pass


if minutos == 0:
  print('Fin de la sesión')
else: 
  if minutos <= 60:
    tarifa = 25
  elif (minutos > 60) & (minutos < 60*8):
    tarifa = 25 + (math.ceil((minutos - 60)/60))*15
  else:
    tarifa = 25 + (math.ceil((minutos - 60)/60))*15 + 200
  
  print('Su tarifa es de ', tarifa, ' pesos')
