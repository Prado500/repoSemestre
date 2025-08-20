

import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px

from wordcloud import WordCloud #Instalar esta libreria con anaconda navigator clase 03

import seaborn as sns

import missingno as msno

#Carga de los datos en un DataFrame
#df = pd.read_csv("C:\\Users\\Alejandro Ostos\\Documents\\Universidades\\UniversidadDeIbague\\2025B\\MachineLearning\\BaseDatosJuegoUTF-16.csv")

df = pd.read_csv("C:/Users/Alejandro Ostos/Documents/Universidades/UniversidadDeIbague/2025B/MachineLearning/Clase02/BaseDatosJuegoUTF-16.csv", encoding="utf-16")

df.head()  # Muestra las primeras filas del DataFrame

## Se usa header = none cuando el archivo no tiene encabezado

df = pd.read_csv( 'BaseDatosJuegoUTF-8.csv', header=None)
df.head(2)

## La primera entrega que vamos a hacer es la limpieza de una base de datos

#Mostramos los ultimos registros del data frame

df.tail()

#Probar con jupyter

#Veo la dimension del df

df.shape

# Solicito informacion del df
df.info()

df.info(memory_usage = 'deep')

df.head()

#Nos saltamos la primera fila
df = pd.read_csv( 'BaseDatosJuegoUTF-8.csv', encoding = 'utf8', skiprows = 1)

# Configuramos el uso de memoria

df = pd.read_csv( 'BaseDatosJuegoUTF-8.csv', encoding = 'utf8', skiprows = 1, low_memory=False)


df.info()

# Me muestra informacion estadistica de la base de datos (de sus columnas).

df.describe()

df['edad'].value_counts() # Entrega un maximo a la izquierda y un minimo a la derecha Me de dice la frecuencia de datos de edad 31 hay 25

##importacion de matplotlib

#Bins es el ancho de las barras azules

df.hist(bins = 20, figsize=(12, 8))
plt.show()

##importacion de plotly
# Se obtienen solo las columnas numericas
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Se crea un histograma interactivo para cada columna numerica

for col in numeric_cols:
    fig = px.histogram(df, x=col, nbins=20, title=f'Histograma de {col}')
    fig.update_layout(
        xaxis_title=col,
        yaxis_title='Frecuencia',
        autosize=True
    )
    
    fig.show()

# WORD CLOUD

# Se combinan todos los nombres en una cadena de caracteres gigante, necesaria para graficar un word Cloud.

names = df["Nombre"].tolist()
len(names)

# Se toma la lista de nombres (names) y se une en una sola cadena, separando cada elemento por un espacio

names_as_one_string = " ".join(names)
names_as_one_string

#Importacion de word cloud

plt.figure(figsize=(20,20))
plt.imshow(WordCloud().generate(names_as_one_string))


# Si quisiera calcular la masa, qe es la relacion entre el peso y la altura, elimino la cedula

df = df.drop(["Cedula"], axis="columns")
df.head()

# Elimino la dara que no necesito

columns_to_drop=["edad", "Sexo"]
df1 = df.drop(columns_to_drop, inplace=False, axis = 1)
df1.head()

df1 = df[["Altura", "peso"]].copy()
print(df1.head())



correlation = df1.corr()
print(correlation)

print("Hell yeah")

# MODIFICO EL NOMBRE DE LA VARIABLE

df.rename(columns = {"NOMBRE" : "NOMBRE COMPLETO"})

# Verifico datos que no se hayan rellenado

print(df.isnull().any())

#
print(df.isnull().any().any())


df.isna()


##sumo el numero de variables para las cuales faltan datos

df.isnull().sum()

#  muestro el numero

df.isnull().sum().sum()

#Importacion de seaborn
sns.heatmap(df.isna())

## se traspone

sns.heatmap(df.isna()).transpose()

# Importacion de missingno

msno.bar(df)

# porcentaje de faltantes

print("Amount of missing values in - ")
for column in df.columns:
    percentage_missing = np.mean(df[column].isna())
    print(f"{column} : {round(round(percentage_missing * 100))} %")
    
# El metodo dropna() es usado para eliminar filas (axis = 0) o columnas (axis = 1)


df = df.dropna(tresh = count_row/2, axis = 1) # si en la columna de un dato, si no esta lleno en al menos la mitad del numero de las columnas, no se toma.
df.head()