#coding=utf8
import pandas as pd
import matplotlib.pyplot as plt

def curvaDuracion(mes,nommes:str):
    cantdatos = len(mes)
    maximo = mes[nommes].max()
    minimo = mes[nommes].min()
    rango = maximo-minimo
    intervalos = 20
    incrementos = rango/intervalos
    caudales = [maximo-i*incrementos for i in range(int(maximo//incrementos)+1)]

    frec = pd.DataFrame(columns=['Frecuencia'], index=caudales)
    frec['Frecuencia'] = 0
    frec['Acumulado'] = 0

    for i in range(len(caudales)-1):
        for e in mes[nommes].values:
            if caudales[i+1] <= e <= caudales[i]:
                frec['Frecuencia'][caudales[i]] += 1

    frec['%']= (frec['Frecuencia']/(len(mes)))*100
    acum = [frec['%'].values[0]]
    for i in range(len(frec)-1):
        acum.append(acum[i]+frec['%'].values[i+1])
    frec['Acumulado'] = acum
    return [frec['Acumulado'].values, caudales]

def Grafica1x1():
    plt.figure()
    plt.title('Curvas de duración de caudales')
    plt.xlabel('% Excedencia')
    plt.ylabel(r'Caudal medio diario $[m^{3}/2]$')
    plt.plot(curvaDuracion(enero, 'Enero')[0], curvaDuracion(enero, 'Enero')[1], marker='', color='b', ls='-',
             label='Enero')
    plt.plot(curvaDuracion(febrero, 'Febrero')[0], curvaDuracion(febrero, 'Febrero')[1], marker='', color='g', ls='-',
             label='Febrero')
    plt.plot(curvaDuracion(marzo, 'Marzo')[0], curvaDuracion(marzo, 'Marzo')[1], marker='', color='r', ls='-',
             label='Marzo')
    plt.plot(curvaDuracion(abril, 'Abril')[0], curvaDuracion(abril, 'Abril')[1], marker='', color='c', ls='-',
             label='Abril')
    plt.plot(curvaDuracion(mayo, 'Mayo')[0], curvaDuracion(mayo, 'Mayo')[1], marker='', color='m', ls='-', label='Mayo')
    plt.plot(curvaDuracion(junio, 'Junio')[0], curvaDuracion(junio, 'Junio')[1], marker='', color='y', ls='-',
             label='Junio')
    plt.plot(curvaDuracion(julio, 'Julio')[0], curvaDuracion(julio, 'Julio')[1], marker='', color='k', ls='-',
             label='Julio')
    plt.plot(curvaDuracion(agosto, 'Agosto')[0], curvaDuracion(agosto, 'Agosto')[1], marker='', color='#FFD700', ls='-',
             label='Agosto')
    plt.plot(curvaDuracion(septiembre, 'Septiembre')[0], curvaDuracion(septiembre, 'Septiembre')[1], marker='',
             color='#FF00FF', ls='-', label='Septiembre')
    plt.plot(curvaDuracion(octubre, 'Octubre')[0], curvaDuracion(octubre, 'Octubre')[1], marker='', color='#FF0000',
             ls='-', label='Octubre')
    plt.plot(curvaDuracion(noviembre, 'Noviembre')[0], curvaDuracion(noviembre, 'Noviembre')[1], marker='',
             color='#800000', ls='-', label='Noviembre')
    plt.plot(curvaDuracion(diciembre, 'Diciembre')[0], curvaDuracion(diciembre, 'Diciembre')[1], marker='',
             color='#FF4500', ls='-', label='Diciembre')
    plt.legend()
    plt.savefig('CurvasDuracion.png', dpi=600)
    plt.show()

def Grafica_nxn():
    fig, ax = plt.subplots(3,4,sharex = True, sharey=True)
    ax[0,0].set_title('Enero')
    #ax[0,0].set_ylabel(r'Caudal medio diario $[m^{3}/s]$', fontsize=8)
    ax[0,0].plot(curvaDuracion(enero, 'Enero')[0], curvaDuracion(enero, 'Enero')[1], marker='', color='b', ls='-')

    ax[0,1].set_title('Febrero')

    ax[0,1].plot(curvaDuracion(febrero, 'Febrero')[0], curvaDuracion(febrero, 'Febrero')[1], marker='', color='g', ls='-',
             label='Febrero')

    ax[0, 2].set_title('Marzo')

    ax[0,2].plot(curvaDuracion(marzo, 'Marzo')[0], curvaDuracion(marzo, 'Marzo')[1], marker='', color='r', ls='-',
             label='Marzo')

    ax[0, 3].set_title('Abril')

    ax[0,3].plot(curvaDuracion(abril, 'Abril')[0], curvaDuracion(abril, 'Abril')[1], marker='', color='c', ls='-',
             label='Abril')

    ax[1,0].set_title('Mayo')
    ax[1, 0].set_ylabel(r'Caudal medio diario $[m^{3}/s]$', fontsize=10)
    ax[1,0].plot(curvaDuracion(mayo, 'Mayo')[0], curvaDuracion(mayo, 'Mayo')[1], marker='', color='m', ls='-', label='Mayo')

    ax[1, 1].set_title('Junio')

    ax[1,1].plot(curvaDuracion(junio, 'Junio')[0], curvaDuracion(junio, 'Junio')[1], marker='', color='y', ls='-',
             label='Junio')

    ax[1, 2].set_title('Julio')

    ax[1,2].plot(curvaDuracion(julio, 'Julio')[0], curvaDuracion(julio, 'Julio')[1], marker='', color='k', ls='-',
             label='Julio')

    ax[1, 3].set_title('Agosto')

    ax[1,3].plot(curvaDuracion(agosto, 'Agosto')[0], curvaDuracion(agosto, 'Agosto')[1], marker='', color='#FFD700', ls='-',
             label='Agosto')

    ax[2,0].set_title('Septiembre')
    #ax[2, 0].set_ylabel(r'Caudal medio diario $[m^{3}/s]$', fontsize=8)
    ax[2, 0].set_xlabel('% Excedencia')
    ax[2,0].plot(curvaDuracion(septiembre, 'Septiembre')[0], curvaDuracion(septiembre, 'Septiembre')[1], marker='',
          color='#FF00FF', ls='-', label='Septiembre')

    ax[2,1].set_title('Octubre')
    ax[2, 1].set_xlabel('% Excedencia')
    ax[2,1].plot(curvaDuracion(octubre, 'Octubre')[0], curvaDuracion(octubre, 'Octubre')[1], marker='', color='#FF0000',
             ls='-', label='Octubre')

    ax[2,2].set_title('Noviembre')
    ax[2, 2].set_xlabel('% Excedencia')
    ax[2, 2].plot(curvaDuracion(noviembre, 'Noviembre')[0], curvaDuracion(noviembre, 'Noviembre')[1], marker='',
             color='#800000', ls='-', label='Noviembre')

    ax[2,3].set_title('Diciembre')
    ax[2, 3].set_xlabel('% Excedencia')
    ax[2, 3].plot(curvaDuracion(diciembre, 'Diciembre')[0], curvaDuracion(diciembre, 'Diciembre')[1], marker='',
             color='#FF4500', ls='-', label='Diciembre')

    fig.suptitle('Curvas de duración por mes')
    plt.tight_layout()
    plt.savefig('CurvasDuracionmes.png', dpi=300)
    plt.show()

#-------Abrir el archivo--------------------

path = 'ELJORDAN_1903-2022_QMD.xlsx'
eljordan = pd.read_excel(path)
#------------------------------------------
caudal = eljordan['Valor']
fecha = eljordan['Fecha']
fecha2 = []
for e in fecha:
    fecha2.append(pd.to_datetime(e, format='%d-%m-%y'))
dataf = pd.DataFrame(columns=['Fecha', 'QMD'])
dataf['Fecha'] = fecha2
dataf['QMD'] = caudal

enero = pd.DataFrame(columns=['Fecha', 'Enero'])
febrero = pd.DataFrame(columns=['Fecha', 'Febrero'])
marzo = pd.DataFrame(columns=['Fecha', 'Marzo'])
abril = pd.DataFrame(columns=['Fecha', 'Abril'])
mayo = pd.DataFrame(columns=['Fecha', 'Mayo'])
junio = pd.DataFrame(columns=['Fecha', 'Junio'])
julio = pd.DataFrame(columns=['Fecha', 'Julio'])
agosto = pd.DataFrame(columns=['Fecha', 'Agosto'])
septiembre = pd.DataFrame(columns=['Fecha', 'Septiembre'])
octubre = pd.DataFrame(columns=['Fecha', 'Octubre'])
noviembre = pd.DataFrame(columns=['Fecha', 'Noviembre'])
diciembre = pd.DataFrame(columns=['Fecha', 'Diciembre'])


for e in dataf.values:
    mes = e[0].month
    date = e[0]
    agua = e[1]
    if mes == 1:
        enero.loc[len(enero)]=e
    elif mes == 2:
        febrero.loc[len(febrero)]=e
    elif mes == 3:
        marzo.loc[len(marzo)]=e
    elif mes == 4:
        abril.loc[len(abril)]=e
    elif mes == 5:
        mayo.loc[len(mayo)]=e
    elif mes == 6:
        junio.loc[len(junio)]=e
    elif mes == 7:
        julio.loc[len(julio)]=e
    elif mes == 8:
        agosto.loc[len(agosto)]=e
    elif mes == 9:
        septiembre.loc[len(septiembre)]=e
    elif mes == 10:
        octubre.loc[len(octubre)]=e
    elif mes == 11:
        noviembre.loc[len(noviembre)]=e
    elif mes == 12:
        diciembre.loc[len(diciembre)]=e
#---------------------


print(Grafica1x1())

















