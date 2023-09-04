#coding=utf8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Graficar():
    caudal = np.array(eljordan['Valor'])
    fecha2 = []
    for e in fecha:
        fecha2.append(pd.to_datetime(e, format='%d-%m-%y'))
    plt.figure()
    plt.title('Serie histórica: El Jordán 1981-2023')
    plt.xlabel('Año')
    plt.ylabel(r'Caudal medio diario $[m^{3}/s]$')
    plt.grid(ls='--')
    plt.plot(fecha2, caudal, marker='.', color='b', ls='')
    plt.legend()
    plt.savefig('CauCuenca.png',dpi=300)
    plt.show()

path = 'ELJORDAN_1903-2022_QMD.xlsx'
eljordan = pd.read_excel(path)
#------------------------------------------
caudal = np.array(eljordan['Valor'])
fecha = eljordan['Fecha']
fecha2 = []
for e in fecha:
    fecha2.append(pd.to_datetime(e, format='%d-%m-%y'))
dataf = pd.DataFrame(columns=['Fecha', 'QMD'])
dataf['Fecha'] = fecha2
dataf['QMD'] = caudal

anio_incio = 1981
anio_fin = 2022
tiempo = list(range(anio_incio, anio_fin + 1))

Graficar()