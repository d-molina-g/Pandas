import pandas as pd
import numpy as np

#Creación del Dataframe

data = np.array([ ['','Col1','Col2'], ['Fila1',2,22], ['Fila2',33,44]])
print(data)

print("DataFrame")
print("\n")

#Creación especificando posiciones (para datos, columnas y filas)
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

#Otra menera más simple
df = pd.DataFrame(np.array([[1,2,3],[4,None,6],[7,8,9]]))
print("\n")
print(df)


#Creación de una Serie
print("\n")
series = pd.Series({"Argentina":"Buenos Aires",
					"Chile":"Santiago de Chile",
					"Colombia":"Bogotá",
					"Perú":"Lima"})
print("Serie:")
print(series)
print(series["Argentina"])

print("Forma del DataFrame:")
print(df.shape)

print("Forma de la Serie")
print(series.shape)

print("Altura del DataFrame:")
print(len(df.index))

#Estadisticas del DataFrame
print("\n")

print(df.describe())
#Lanza la media de todas las columnas
print(df.mean()) 
#Lanza la correlación de todas las columnas
print(df.corr())
#Lanza el número de valores No nulos
print(df.count())

#df.max()
#df.min()
#df.median() - Mediana
#df.std() - Desviación estandar

print("Valor especifico - Fila - Columna")
#Seleccionar valor de una fila y columna en especifico
print(df.iloc[0][2])
print("Valores de una fila (indice) en especifico")
print(df.loc[2])
#o con 
print(df.iloc[2,:])



print("Archivos")
#Lectura de archivos

#df = pd.read_csv('train.csv')
print("Limpieza")
#Verificar los datos nulos
#Nos arroja una matriz booleana ... False si no es Null, True si lo es
print(df.isnull())
print("Suma de los nulos por columna")
#Suma de los datos nulos
print(df.isnull().sum())

print("\n")
print("DataFrame: ", df)

#Borra la fila que tenga valores Nulos
#df = df.dropna() 
#print("DataFrame: ", df)

#Reemplaza los valores perdidos por la media
print("Reemplaza los valores Nulos por la media")
df=df.fillna(100)
print(df)
