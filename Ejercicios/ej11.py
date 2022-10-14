# Databricks notebook source
import pandas as pd

df1 = pd.read_csv("/dbfs/FileStore/shared_uploads/adolfo.cruz@kof.com.mx/athlete_events.csv")

# COMMAND ----------

df1.head(3)

# COMMAND ----------

print('Competidor más veterano con medalla: ')
df2 = df1[['Name', 'Age', 'Medal']].dropna()
df2[(df2.Age == df2.Age.max())]

# COMMAND ----------

print('Competidor más joven con medalla oro: ')
df2[df2.Medal == 'Gold'].sort_values('Age').head(7)

# COMMAND ----------

print('Competidor más ganador de la historia: ')
df2[['Name', 'Medal']].groupby('Name').count().reset_index().sort_values('Medal', ascending=False).head()

# COMMAND ----------

print('Guarda csv: ')
df1[df1.Name == 'Michael Fred Phelps, II'].to_csv('mayor_ganador_historia.csv')
