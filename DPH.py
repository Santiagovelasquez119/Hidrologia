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
    plt.title('Curva de estacionalidad: El Jordán 1981-2023')
    plt.xlabel('Año')
    plt.ylabel(r'Caudal$[m^{3}/s]$')
    plt.grid(ls='--')
    plt.plot(fecha2, caudal, marker='.', color='b', ls='', label='Caudal medio diario')
    plt.legend()
    plt.show()

def QMD_Anualxmes():
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

    QMD_anual = pd.DataFrame(0, columns=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'i'], index=tiempo)
    for e in dataf.values:
        mes = e[0].month
        año = e[0].year
        if mes == 1:
            QMD_anual['Enero'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 2:
            QMD_anual['Febrero'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 3:
            QMD_anual['Marzo'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 4:
            QMD_anual['Abril'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 5:
            QMD_anual['Mayo'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 6:
            QMD_anual['Junio'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 7:
            QMD_anual['Julio'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 8:
            QMD_anual['Agosto'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 9:
            QMD_anual['Septiembre'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 10:
            QMD_anual['Octubre'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 11:
            QMD_anual['Noviembre'][año] += e[1]
            QMD_anual['i'][año] += 1
        elif mes == 12:
            QMD_anual['Diciembre'][año] += e[1]
            QMD_anual['i'][año] += 1


#-------Abrir el archivo--------------------

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

dia_incio = 1
dia_fin = 31
tiempo = list(range(dia_incio, dia_fin + 1))

QMD_anual = pd.DataFrame(0, columns=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                                         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'i'], index=tiempo)
for e in dataf.values:
    mes = e[0].month
    dia = e[0].day
    if mes == 1:
        QMD_anual['Enero'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 2:
        QMD_anual['Febrero'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 3:
        QMD_anual['Marzo'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 4:
        QMD_anual['Abril'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 5:
        QMD_anual['Mayo'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 6:
        QMD_anual['Junio'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 7:
        QMD_anual['Julio'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 8:
        QMD_anual['Agosto'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 9:
        QMD_anual['Septiembre'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 10:
        QMD_anual['Octubre'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 11:
        QMD_anual['Noviembre'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
    elif mes == 12:
        QMD_anual['Diciembre'][dia] += e[1]/42
        QMD_anual['i'][dia] += 1
#---------------------

print('------------------------------------')
#print(QMD_anual)
print('------------------------------------')

def graficarQMD_mes(meses:str):
    plt.figure()
    plt.grid(ls='--')
    plt.title(f'Curva de duración de {meses}, Estación: El jordán')
    plt.xlabel('Día')
    plt.ylabel(r'Caudal medio diario $[m^{3}/s]$')
    plt.plot(tiempo, QMD_anual[meses], marker='.', color='b', ls='-')
    plt.show()
    plt.savefig(f'CurvaDuracion{meses}.png', dpi=300)
#print(graficarQMD_mes('Febrero'))
print(Graficar())























