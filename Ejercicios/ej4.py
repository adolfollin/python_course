# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC 1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo?

# COMMAND ----------

mi_edad = 24/2
print('Mi edad es: ', mi_edad)

# COMMAND ----------

# MAGIC %md
# MAGIC 2.- A un tercio de la edad de mi hermana la disminuyo en 15 años. Tengo 6 años. ¿Qué edad tiene?

# COMMAND ----------

mi_edad = 6
edad_de_mi_hermana= (mi_edad + 15)*3
print('La edad de mi hermana es: ', edad_de_mi_hermana)

# COMMAND ----------

# MAGIC %md
# MAGIC 3.-Determina quién es más grande

# COMMAND ----------

if mi_edad <= edad_de_mi_hermana:
    print('Mi hermana es mayor')
else:
    print('Yo soy mayor')
