# Ejercicios de profundización [Python]
#EL propósito de este ejercicio es que el alumno ponga sus habilidades de SQL junto con otras adqueridas a lo largo del curso como ser dibujado de gráficos con matplotlib y análisis de datos con numpy. Este es un caso típico de análisis de datos

import sqlite3
import numpy as np
import matplotlib.pyplot as plt

#Funciones

def fetch():
  conn = sqlite3.connect('heart.db')
  c = conn.cursor()

  c.execute('SELECT pulso FROM sensor')
  data = c.fetchall()

  conn.commit()
  # Cerrar la conexión con la base de datos
  conn.close()

  return data


def show(data):
  fig = plt.figure()
  fig.suptitle('Ritmo Cardiaco', fontsize=16)
  ax = fig.add_subplot()

  ax.plot(data, c='darkgreen', label='Ritmo')
  ax.legend()
  ax.grid()
  ax.set_ylabel("Pulso")
  ax.set_xlabel("Número de Pulsación")
  plt.show()
  print("Fin del Plot")


def estadistica(data):
    # Calcular el promedio de todos los elementos
    promedio = "{:.2f}".format(np.mean(data)) #aqui guardamos el dato solamente con 2 dciamles dspues de la coma
    print('El Promedio de las pulsaciones es: ', promedio)
    minimo = np.min(data)
    print('La minima de las pulsaciones es: ', minimo)
    maximo = np.max(data)
    print('El maximo de las pulsaciones es: ', maximo)
    desvio_estandar = "{:.2f}".format(np.std(data)) #aqui guardamos el dato solamente con 2 dciamles dspues de la coma
    print('El desvio estandar de las pulsaciones es: ', desvio_estandar)

    return (promedio, desvio_estandar)


def regiones(data, promedio, desvio_estandar):
  
  data = np.asanyarray(data)
  
  x1 = []
  y1 = []

  x2 = []
  y2 = []

  x3 = []
  y3 = []

  for i in range(len(data)):
    if data[i] <= (float(promedio) - float(desvio_estandar)):
      x1.append(i)
      y1.append(data[i])
    elif data[i] >= (float(promedio) + float(desvio_estandar)):
      x2.append(i)
      y2.append(data[i])
    else:
      x3.append(i)
      y3.append(data[i])
        
  
  fig = plt.figure()
  fig.suptitle('Comparacion de Ritmo Cardiaco', fontsize=16)    # colocamos el titulo
  ax1 = fig.add_subplot(2, 2, 1) # indica filas, columnas y la posicion del grafico
  ax2 = fig.add_subplot(2, 2, 2)
  ax3 = fig.add_subplot(2, 2, 3)
    
  ax1.scatter(x1,y1, marker='.', label= 'Pulsaciones Bajas', c='darkcyan')
  ax1.set_facecolor('whitesmoke')
  ax1.grid('solid')
  ax1.legend()
    
    
  ax2.scatter(x2,y2, marker='.', label= 'Pulsaciones Altas', c='darkred')
  ax2.set_facecolor('whitesmoke')
  ax2.grid('solid')
  ax2.legend()
    
    
  ax3.scatter(x3,y3, marker='.', label= 'Pulsaciones Medias', c='darkgreen')
  ax3.set_facecolor('whitesmoke')
  ax3.grid('solid')
  ax3.legend()
  plt.show()  

  '''fig = plt.figure()
  ax = fig.add_subplot()

  ax.plot(x1,y1, c='darkcyan', label='Pulsaciones Bajas')
  ax.plot(x2,y2, c='darkred', label='Pulsaciones Altas')
  ax.plot(x3, y3, c='darkgreen', label='Pulsaciones Medias')
  ax.legend()
  ax.grid()
  plt.show()'''
  fig = plt.figure()
  fig.suptitle('Comparacion de Ritmo Cardiaco', fontsize=16)    # colocamos el titulo
  ax1 = fig.add_subplot(2, 2, 1) # indica filas, columnas y la posicion del grafico
  ax2 = fig.add_subplot(2, 2, 2)
  ax3 = fig.add_subplot(2, 2, 3)

  ax1.plot(x1,y1, c='darkcyan', label='Pulsaciones Bajas')
  ax1.set_facecolor('whitesmoke')
  ax1.grid('solid')
  ax1.legend()
    
    
  ax2.plot(x2,y2, c='darkred', label='Pulsaciones Altas')
  ax2.set_facecolor('whitesmoke')
  ax2.grid('solid')
  ax2.legend()
    
    
  ax3.plot(x3, y3, c='darkgreen', label='Pulsaciones Medias')
  ax3.set_facecolor('whitesmoke')
  ax3.grid('solid')
  ax3.legend()
  plt.show() 

if __name__ == "__main__":
  # Leer la DB
  data = fetch()
  print(data)

  # Data analytics
  show(data)
  promedio, desvio_estandar = estadistica(data)
  regiones(data, promedio, desvio_estandar)



