import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Oscar Flores Nc = 1389
# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de Ecommerce con 4 elementos por lista

amz = ['Amazon', 310, True, 1994]
ali = ['Aliexpress', 150, True, 2010]
ml  = ['Mercado Libre', 108, True, 1999]
ebg = ['eBay', 133, False, 1995]
shk = ['Shopee', 200, True, 2015]

# Creamos una lista de listas (conformando la tabla)
lista_ecommerce = [amz, ali, ml, ebg, shk]

# A cada columna le ponemos su nombre
df_ecommerce = pd.DataFrame(lista_ecommerce,
                            columns=["Nombre", "Usuarios", "Envio_Gratis", "Año"])

print(df_ecommerce)

df_ecommerce.to_csv("T_linea.csv", index=False)

# Crear gráficas de líneas
# X = Nombre en el Eje Horizontal
# Y = Usuarios en el Eje Vertical

plt.plot(df_ecommerce["Nombre"], df_ecommerce["Usuarios"])
plt.title("Grafica T_linea 1389")
plt.xlabel("Nombre de T_linea")
plt.ylabel("Usuarios activos en millones")
plt.show()

# Crear gráfica de puntos

plt.scatter(df_ecommerce["Nombre"], df_ecommerce["Usuarios"])
plt.title("Grafica T_linea 1389")
plt.xlabel("Nombre de T_linea")
plt.ylabel("Usuarios activos en millones")
plt.show()

# Crear gráfica de barras

plt.bar(df_ecommerce["Nombre"], df_ecommerce["Usuarios"])
plt.title("Grafica T_linea 1389")
plt.xlabel("Nombre de T_linea")
plt.ylabel("Usuarios activos en T_linea")
plt.show()

# Ordenar la gráfica de barras de manera descendente
# De la grande a la pequeña

df_ecommerce_ordenar = df_ecommerce.sort_values('Usuarios', ascending=False)

plt.bar(df_ecommerce_ordenar["Nombre"], df_ecommerce_ordenar["Usuarios"])
plt.title("Grafica T_linea 1389")
plt.xlabel("Nombre de T_linea")
plt.ylabel("Usuarios activos en millones")
plt.show()

# Colorear la gráfica de barras

df_ecommerce_ordenar = df_ecommerce.sort_values('Usuarios', ascending=False)

plt.bar(df_ecommerce_ordenar["Nombre"], df_ecommerce_ordenar["Usuarios"],
        color=['b', 'g', 'c', 'm', 'y'])

plt.title("Grafica T_linea 1389")
plt.xlabel("Nombre de Ecommerce")
plt.ylabel("Usuarios activos en millones")
plt.show()

# Gráfica de pie

plt.pie(df_ecommerce["Usuarios"], labels=df_ecommerce["Nombre"],
        autopct='%1.1f%%')

plt.title("Grafica T_linea 1389")
plt.show()