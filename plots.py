import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


########## FUNCION GRAFICO DE BARRAS ##########
def bar_plot(df,x,y):
  # Ordenamos los valores
  df.sort_values(x, inplace=True)
  
  # Estilo del gráfico al de seaborn 
  sns.set()

  # Ttamaño del gráfico 
  plt.figure(figsize=(12,8))

  # Creamos el gráfico de barras 
  plt.barh(y, x, data=df)

  # Añadimos la línea vertical de la media
  plt.axvline(df[x].mean(), ls='--', c='r')

  plt.show()





########## FUNCION GRAFICO DE PUNTOS ##########
def scatter_plot(df, x, y, text=None, color=None):

  # Creamos el scatter plot con plotly
  fig = px.scatter(df, x, y, text=text, color=color, width=800, height=500)

  # Añadimos la linea horizontal
  fig.add_shape(type='line', 
                x0 = df[x].mean(),
                y0 = df[y].min(),
                y1 = df[y].max(), 
                x1 = df[x].mean())

  # Añadimos la línea vertical
  fig.add_shape(type='line', 
                x0 = df[x].min(),
                y0 = df[y].mean(),
                y1 = df[y].mean(), 
                x1 = df[x].max())
  
  # Especificamos dónde irán los nombres de los valores
  fig.update_traces(textposition='top center')
  fig.show()





########## FUNCION GRAFICO 3D ##########
def scatter_plot3D(df, x, y, z, text=None, color=None):

  # Crear el gráfico 3D
  fig = px.scatter_3d(df, x, y, z, text=text, color=color)

  # Establecer un tamaño del gráfico
  fig.update_layout(autosize=False, 
                    width=800,
                    height=800)
  
  fig.show()





