#coding=utf8
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as mcolor

def Qprom(dataf, doy:int):
    SumQ = 0
    contador = 0
    for e in dataf.values:
        if e[2] == doy:
            SumQ+=e[1]
            contador+=1
    Qprom = SumQ/contador
    return Qprom

def Vprom(dataf, doy:int):
    SumV = 0
    contador = 0
    for e in dataf.values:
        if e[2] == doy:
            SumV+=e[1]*3600*24
            contador+=1
    Vprom = SumV/contador
    return Vprom

#-------Abrir el archivo--------------------

path = 'ELJORDAN_1903-2022_QMD.xlsx'
eljordan = pd.read_excel(path)
#------------------------------------------
meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                             'Septiembre', 'Octubre', 'Noviembre', 'Diciembre',]
caudal = eljordan['Valor']
fecha = eljordan['Fecha']
fecha2 = []
for e in fecha:
    fecha2.append(pd.to_datetime(e, format='%d-%m-%y'))
doy = []
for e in fecha2:
    if e.month == 1:
        doy.append(e.day)
    elif e.month == 2:
        doy.append(e.day+31)
    elif e.month == 3:
        doy.append(59 + e.day)
    elif e.month == 4:
        doy.append(90 + e.day)
    elif e.month == 5:
        doy.append(120 + e.day)
    elif e.month == 6:
        doy.append(151 + e.day)
    elif e.month == 7:
        doy.append(181 + e.day)
    elif e.month == 8:
        doy.append(212 + e.day)
    elif e.month == 9:
        doy.append(243 + e.day)
    elif e.month == 10:
        doy.append(273 + e.day)
    elif e.month == 11:
        doy.append(304 + e.day)
    elif e.month == 12:
        doy.append(334 + e.day)

dataf = pd.DataFrame(columns=['Fecha', 'QMD'])
dataf['Fecha'] = fecha2
dataf['QMD'] = caudal
dataf['Doy']=doy
dataf['Volumen'] = dataf['QMD']*24*3600

num = [i for i in range(1,366)]
Q = []
V = []
for i in range(len(num)):
    Q.append(Qprom(dataf, num[i]))
    V.append(Vprom(dataf, num[i]))
print(V)
VAcum = []
suma = 0
for i in range(len(V)):
    suma+=V[i]
    VAcum.append(suma)
print(VAcum)


fig, ax1 = plt.subplots()
plt.title('Curvas de variación estacional y masa, Estación: El Jordán')
plt.grid(ls='--')
ax1.plot(num, Q)
ax1.set_xlabel('Day of year')
ax1.set_ylabel(r'Caudal $[m^{3}/s]$')
ax1.plot(num,Q, marker='.', ls='-', color='b', label='Curva de estacionalidad')
ax2= ax1.twinx()
ax2.plot(num, VAcum, marker='.', ls='-', color ='g', label='Curva de masa')
plt.ylabel(r'Volumen $[m^{3}]$')
ax1.legend(loc=(0.55,0.02)), ax2.legend(loc=(0.68,0.1))
plt.show()
