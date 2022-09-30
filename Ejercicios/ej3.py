# Databricks notebook source
tupla = (1,'hola', True, None, 10.5)
lista_de_tupla = list(tupla)
diccionario = dict(zip(range(1,6), lista_de_tupla))
print(diccionario)
