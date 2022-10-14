# Databricks notebook source
def solucion_funcion_cuadratica(a, b, c):
    x1 = (-b + (((b**2)-4*a*c)**(1/2)))/(2*a)
    x2 = (-b - ((b**2)-4*a*c)**(1/2))/(2*a)
    return x1, x2

# COMMAND ----------

solucion_funcion_cuadratica(4,3,-22)
