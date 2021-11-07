# AVANCE FINAL PROYECTO FUNDAMENTOS DE PROGRAMACION - GARCIA COX MILTON, QIU ZHANG WILLIAM 23/08/2017
from funciones_got import*

lPersonajes, dEpisodios, familias = "", "", ""
strMenu = ("\n"+"~"*80)+"""\nMenú principal – Reportes de Juego de Tronos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1.	Importar datos de personajes, episodios y casas nobles.
    2.	Imprimir estadísticas para cada casa noble.
    3.	Imprimir episodio más visto en cada temporada.
    4.	Mostrar gráfico de barras de tiempo total que aparece cada personaje en la serie.
    5.	Mostrar gráfico de pastel de cantidad de espectadores totales en cada temporada.
    6.	Mostrar gráfico de barras de cantidad de personajes vivos vs muertos para cada casa noble.
    7.	Salir."""

casasSTR = """Casas nobles Disponibles
1. Baratheon
2. Greyjoy
3. Lannister
4. Stark
5. Tully
6. Bolton
7. Tyrell
8. Targaryen
9. Regresar al Menú Principal"""

opcion =""
while opcion != "7":
    numcasa = "0"
    x = ""
    print(strMenu)
    opcion = input("\nIngrese una Opción: ")

    if opcion == "1":
        print("--" * 40)
        print("\t~Importar datos de personajes, episodios y casas nobles.")
        lPersonajes, dEpisodios, familias = importarArchivos("datos/personajes.csv", "datos/episodios.csv",
                                                             "datos/familias.csv")
        for per in lPersonajes:
            calcularTiempoTotal(per)
        print("\t\tDatos Importados correctamente")

    elif opcion =="2":
        while numcasa != "":
            print("--" * 40)
            print("\t~Elegir casa para mostrar las estadísticas")
            print(casasSTR)
            numcasa = input("\nSeleccione la Casa Noble: ")
            numcasa = seleccionarCasa(numcasa)
            if numcasa == "":
                break
            print("--" * 40)
            print("\t~Estadisticas para la Casa", numcasa)
            imprimirEstadisticasXCasa(lPersonajes, numcasa)
            print("--" * 40)

    elif opcion =="3":
        print("\t~Episodios más vistos por Temporada")
        print("-" * 75)
        mostrarEpisodioMasVisto(dEpisodios)

    elif opcion =="4":
        print("\t~Tiempo Total de cada personaje en la serie")
        print("-" * 75)
        mostrarTiempoTotal(lPersonajes)

    elif opcion == "5":
        print("\t~Cantidad de Espectadores Totales en cada Temporada")
        print("-" * 75)
        mostrarEspectadores(dEpisodios)

    elif opcion == "6":
        print("\t~Cantidad de Personajes Vivos vs Muertos para cada Casa Noble")
        print("-" * 75)
        mostrarVivosvsMuertos(lPersonajes)

    elif opcion =="7":
        print("\t~Gracias por su Visita\n"+"~"*80)

    else:
        print("Opcion Inválida")