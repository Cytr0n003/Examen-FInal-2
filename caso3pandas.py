#Caso 3:
#Escribir una función en Python que reciba un dataframe de Pandas con los ingresos y gastos de una empresa por meses y devuelva un 
#diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos. El diagrama debe tener una leyenda identificando la 
#línea de los ingresos y la de los gastos, un título con el nombre "Evolución de ingresos y gastos" y el eje y debe empezar en 0
import pandas as pd
import matplotlib.pyplot as plt

class Ventas:
  def __init__(self,datos):
    self.__datos = datos
    self.__titulo = 'Evolución de ingresos y gastos'
  def graficar(self):
    fig,ax = plt.subplots()
    self.__datos.plot(kind='line',ax=ax)
    ax.set_ylabel('Ingresos y gastos')
    ax.set_xlabel('Años')
    plt.grid(True)
    ax.set_title(self.__titulo)
    plt.show()

datos = {'Meses':['Ene','Feb','Mar','Abr'],
         'Gatos':[8976,7456,8789,8345],
         'Ingresos':[9976,8456,9789,8345]}
df = pd.DataFrame(datos).set_index('Meses')

#crear un objeto
objeto = Ventas(df)
objeto.graficar()