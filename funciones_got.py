import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2
def importarArchivos(personajes, episodios, casas):
    lPersonajes = []
    dEpisodios ={}
    framesP = pd.read_csv(personajes)
    for i in range(len(framesP)):
        lPersonajes.append(dict(framesP.ix[i]))

    framesE = pd.read_csv(episodios)
    for i in range(len(framesE)):
        dEpisodios[i+1]= dict(framesE.ix[i])

    familias = list(pd.read_csv(casas)["Casas nobles"])

    return lPersonajes, dEpisodios, familias

# 3
def imprimirEstadisticasXCasa (personajes, casa= "Stark"):
    casa = casa.capitalize()
    masI = ""
    tiemposparaP = []
    tiemposparaM = []
    for per in personajes:
        if casa in per["Aliado a Casa"]:
            calcularTiempoTotal(per)
            tiemposparaP.append(per["Total Tiempo"])
    for t in tiemposparaP:
        t = tiempoPromedio(t, 1)
        tiemposparaM.append(t)
    mayorT = max(tiemposparaM)
    tTotalM = transforTstring(mayorT)

    for per in personajes:
        if casa in per["Aliado a Casa"]:
            if per["Total Tiempo"] == tTotalM:
                masI += per["Personaje"]

    tiempoT = sumaMinutos(tiemposparaP)
    promedioT = tiempoPromedio(tiempoT, len(tiempoT))
    vivos, muertos = contarVivosYMuertos(personajes, casa)

    estadistica = "Estadisticas de la casa: " + casa
    personasvivas = "Personajes vivos: " + str(vivos)
    personasmuertas = "Personajes muertos: " + str(muertos)
    tiempo = "Tiempo total promedio: {} Segundos ".format(promedioT)
    personajemas = "Personaje mas importante: " + str(masI)
    escrito = [estadistica, "\n"+"-"*25+"\n", personasvivas, "\n", personasmuertas, "\n", tiempo, "\n", personajemas]
    with open("Reporte" + casa + ".txt", "w") as f:
        f.writelines(escrito)

    print(estadistica+"\n"+personasvivas+"\n"+personasmuertas+"\n"+tiempo+"\n"+personajemas)

# 4
def mostrarEpisodioMasVisto(episodios):
    lEpis = ordenarEpisodios(episodios, "Espectadores USA")
    temp1 = [epi for epi in lEpis if epi["Temporada"]==1]
    temp2 = [epi for epi in lEpis if epi["Temporada"]==2]
    temp3 = [epi for epi in lEpis if epi["Temporada"]==3]
    temp4 = [epi for epi in lEpis if epi["Temporada"]==4]

    temp1 = sorted(temp1, key=lambda k: k["Espectadores USA"], reverse=True)
    temp2 = sorted(temp2, key=lambda k: k["Espectadores USA"], reverse=True)
    temp3 = sorted(temp3, key=lambda k: k["Espectadores USA"], reverse=True)
    temp4 = sorted(temp4, key=lambda k: k["Espectadores USA"], reverse=True)
    d1 = temp1[0]
    d2 = temp2[0]
    d3 = temp3[0]
    d4 = temp4[0]

    titulo = ("""Nro\t\tNombre\t\t\t\tRating\t\t\tEspectadores (M)\tTemporada\n{}""".format("-" * 75))
    t1 = ("""{}\t\t{}\t\t{}\t\t\t\t{}\t\t\t\t{}""".format(d1["Episodio nro"], d1["Titulo"][:14], d1["Rating"],
                                                            d1["Espectadores USA"], d1["Temporada"]))
    t2 = ("""{}\t\t{}\t\t{}\t\t\t\t{}\t\t\t\t\t{}""".format(d2["Episodio nro"], d2["Titulo"][:14], d2["Rating"],
                                                            d2["Espectadores USA"], d2["Temporada"]))
    t3 = ("""{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t\t{}""".format(d3["Episodio nro"], d3["Titulo"][:14], d3["Rating"],
                                                            d3["Espectadores USA"], d3["Temporada"]))
    t4 = ("""{}\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t\t{}""".format(d4["Episodio nro"], d4["Titulo"][:14], d4["Rating"],
                                                            d4["Espectadores USA"], d4["Temporada"]))

    with open("reporteEpisodios.txt", "w") as f:
        f.write(titulo+"\n"+t1+"\n"+t2+"\n"+t3+"\n"+t4)

    print(titulo+"\n"+t1+"\n"+t2+"\n"+t3+"\n"+t4)

# 5
def mostrarTiempoTotal(personajes):
    pconT = {}
    listaP = []
    listaT = []
    for per in personajes:
        listaP.append(per["Personaje"])
        tiempoU = per["Total Tiempo"].split(":")
        listaT.append(int(tiempoU[0]))
    pconT["Personajes"]= listaP
    pconT["Total Tiempo"] = listaT

    datosconT = (pd.DataFrame(pconT)).ix[0:14]
    plt.bar(np.arange(15),datosconT["Total Tiempo"])
    plt.title('Tiempo (minutos) por Personaje')
    plt.xticks(np.arange(15), datosconT["Personajes"], rotation = 50)
    plt.show()

# 6
def mostrarEspectadores(episodios):
    lEpis = ordenarEpisodios(episodios, "Espectadores USA")
    temporadas = ["T1","T2","T3","T4"]
    porcentajes = []
    temp1 = sum([epi["Espectadores USA"] for epi in lEpis if epi["Temporada"] == 1])
    temp2 = sum([epi["Espectadores USA"] for epi in lEpis if epi["Temporada"] == 2])
    temp3 = sum([epi["Espectadores USA"] for epi in lEpis if epi["Temporada"] == 3])
    temp4 = sum([epi["Espectadores USA"] for epi in lEpis if epi["Temporada"] == 4])
    totalT = [temp1, temp2, temp3, temp4]
    totalSuma = sum(totalT)
    for tiempo in totalT:
        porcentaje = (float("{:.2f}".format(tiempo/totalSuma)))*100
        porcentajes.append(porcentaje)

    plt.pie(porcentajes, labels= temporadas,autopct="%1.0f%%", shadow=True, counterclock =False)
    plt.title("Cantidad de Espectadores Totales en cada Temporada", )
    plt.legend()
    plt.show()

# 7
def mostrarVivosvsMuertos(personajes):
    listaF = importarFamilias()
    lVivos = []
    lMuertos = []
    for casa in listaF:
        TuplaVyM = contarVivosYMuertos(personajes,casa)
        lVivos.append(TuplaVyM[0])
        lMuertos.append(TuplaVyM[1])

    plt.bar(np.arange(len(listaF)),lVivos,0.35, label = "Alive")
    plt.bar(np.arange(len(listaF))+0.35,lMuertos,0.35, label = "Deceased")
    plt.title('Vivos vs Muertos por Casa')
    plt.xticks(np.arange(len(listaF)) + 0.35 / 2, listaF)
    plt.legend()
    plt.show()

# FUNCIONES ANTIGUAS
# LISTA DE FAMILIAS
def importarFamilias(familiasFile= "datos/familias.csv"):
    with open(familiasFile, "r") as f:
        familias = (f.read()).split("\n")
        familias.remove("Casas nobles")

    return familias

# C. ORDENAR EPISODIOS
def ordenarEpisodios(d, criterio=""):
    if criterio in d[1]:
        listEpisodios = d.values()
        listaOrdenada = sorted(listEpisodios, key = lambda k: k[criterio], reverse = True)
        return listaOrdenada
    else:
        return []

# D. CALCULAR TIEMPO TOTAL
def calcularTiempoTotal(p):
    duraciones = [p['Tiempo en T1'], p['Tiempo en T2'], p['Tiempo en T3'], p['Tiempo en T4']]
    p['Total Tiempo'] = sumaMinutos(duraciones)

# E. CONTAR VIVOS Y MUERTOS
def contarVivosYMuertos(lista, casa= "" ):
    vivos, muertos = 0, 0
    if casa == "":
        for personaje in lista:
            if personaje['Estado'] == 'Vivo':
                vivos += 1
            elif personaje['Estado'] == 'Muerto':
                muertos += 1
    elif casa != "":
        for personaje in lista:
            if casa in personaje['Aliado a Casa']:
                if personaje['Estado'] == 'Vivo':
                    vivos += 1
                elif personaje['Estado'] == 'Muerto':
                    muertos += 1
    return vivos, muertos

# (SUMA DE TIEMPO EN FORMATO Min:Seg)
def sumaMinutos(lista):
    duraciones = []
    minExtras = 0
    for duracion in lista:
        list = duracion.split(":")
        duraciones.extend(list)
    minutos = [int(numero) for numero in duraciones[::2]]
    segundos = [int(numero) for numero in duraciones[1::2]]

    segundosT = sum(segundos)

    if segundosT >= 60:
        if segundosT % 60 == 0:
            minExtras = segundosT / 60
            segundosT = '00'
        elif segundosT % 60 != 60:
            minExtras = segundosT // 60
            segundosT = segundosT % 60
            if segundosT < 10:
                segundosT = "0"+str(segundosT)
    minutosT = str(int(sum(minutos) + minExtras))
    segundosT = str(segundosT)
    return (minutosT+":"+segundosT)

# TIEMPO PROMEDIO EN SEGUNDOS
def tiempoPromedio(tiempo, cantidad):
    tiempoT = tiempo.split(":")
    tiempoSeg = (int(tiempoT[0]) * 60) + int(tiempoT[1])
    promedio = float("{:.2f}".format(tiempoSeg/cantidad))
    return promedio

# TRASNFORMAR SEGUNDOS INT A TIEMPO STR FORMATO Min:Seg
def transforTstring(segundos):
    min = str(int(segundos//60))
    seg = str(int(segundos%60))
    if seg=="0":
        seg ="00"
    elif len(seg)==1:
        seg="0"+seg
    stringF = min+":"+seg
    return stringF

# OBTENER EL MAYOR ENTRE VARIOS VALORES
def obtenerMayor(n1,n2,n3,n4):
    list = [n1,n2,n3,n4]

    return max(list)

# SELECCIONAR CASA POR NÚMERO
def seleccionarCasa(numcasa):
    x =""
    if numcasa == "1":
        x = "Baratheon"
    elif numcasa == "2":
        x = "Greyjoy"
    elif numcasa == "3":
        x = "Lannister"
    elif numcasa == "4":
        x = "Stark"
    elif numcasa == "5":
        x = "Tully"
    elif numcasa == "6":
        x = "Bolton"
    elif numcasa == "7":
        x = "Tyrell"
    elif numcasa == "8":
        x = "Targaryen"
    elif numcasa == "9":
        x = ""
    elif numcasa == "" or numcasa == "\n":
        x = "Stark"
    else:
        print("Ingreso No Válido")

    return x