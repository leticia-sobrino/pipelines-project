'''
En este archivo lo que tenemos que realizar es importar nuestros daos limpios y analizados 
para que cuando se ejecute en 'python3 main.py' en la terminal ejecute los datos limpios que has obtenido
tanto de la Api de las ofertas de empleo como de el dataset de Airbnb de Madrid.
La terminal no puede imprimir las graficas por lo que no hace falta meter aqui sus funciones respectivas.

'''


###################################
####  API MADRID HOTEL OFFERS  ####
###################################

# Dataframe final limpio y utilizado en el analisis final

import pandas as pd 

df_clean = pd.read_csv('api_clean.csv')
df_clean



# CALUCLO DE LA MEDIA DE LAS OFERTAS DE HOTELES PARA PODER COMPARAR EN EL ANALISIS CON EL DATAFRAME

df_clean["TotalPrice"] = df_clean["TotalPrice"].astype(float)
df_clean["TotalPrice"]

df_clean["TotalPrice"].mean()





###################################
#####  DATASET AIRBNB MADRID  #####
###################################

# Dataframe general de 2019

df_2019 = pd.read_csv('df_2019.csv')
df_2019



# Dataframe limpio de septiembre de 2019 y utilizado en el analisis final

df_SPT_19 = pd.read_csv('df_SPT_19.csv')
df_SPT_19


# CALCULO DE LA MEDIA DE LOS PRECIOS DE SEPT. 2019 PARA PODER COMPARAR EN EL ANALISIS CON LA API
# LE QUITAMOS EL SIMBOLO DEL DOLAR
df_SPT_19["P_SPT2019"] = df_SPT_19["P_SPT2019"].str.replace('$', '')

df_SPT_19["P_SPT2019"]

df_SPT_19["P_SPT2019"] = df_SPT_19["P_SPT2019"].astype(float)
df_SPT_19["P_SPT2019"]

df_SPT_19["P_SPT2019"].mean()
