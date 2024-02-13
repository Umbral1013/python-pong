#!/usr/bin/python3

"""Nombre del programador: Umbral1013
Nombre del programa: Derrota al dragón de las cien vidas.
Fecha de creación: 08/02/2024.
Descripción del programa: Juego sencillo que consiste en eliminar al
    dragón de las cien vidas con cuatro armas.
"""

import os
import time
import random

def golpesAcertados(num_golpe, num_veces_golpea):
    """Calcula cuántos golpes van a atinar tomando en cuenta el número 
    de golpe (o sea, el turno actual) y las veces que puede golpear el 
    arma. """
    aciertos = 0
    i = 0
    while i < num_veces_golpea:
        num_al_azar = random.randint(0, 101)
        if 0 < num_al_azar < probabilidadAcierto(num_golpe):
            aciertos += 1
        i += 1
    return aciertos
    
def calcularDanno(ataque, num_veces_golpea, num_golpe):
    """ Si se llama a golpesAcertados por separado, la probabilidad 
    cambia. Calcula el daño que inflige el arma en el turno actual. """
    acertados = golpesAcertados(num_golpe, num_veces_golpea)
    
    danno = acertados * ataque
    return danno
        
def probabilidadAcierto(num_golpe):
    """Calcula la probabilidad que tiene el arma de asestar al menos un 
    golpe. """
    probabilidad = 0
    if num_golpe == 0:
        probabilidad = 80
    elif num_golpe == 1:
        probabilidad = 70
    elif num_golpe == 2:
        probabilidad = 60
    elif num_golpe == 3:
        probabilidad = 50
    elif num_golpe == 4:
        probabilidad = 40
    elif num_golpe == 5:
        probabilidad = 30
    return probabilidad
    
def establecerDanno(arma):
    """ Establece las características del arma en uso. """
    ataque = 0
    golpes_posibles = 0
    if arma == 1:
        ataque = 5
        golpes_posibles = 4
    elif arma == 2:
        ataque = 15
        golpes_posibles = 2
    elif arma == 3:
        ataque = 30
        golpes_posibles = 1
    elif arma == 4:
        ataque = 50
        golpes_posibles = 1
    return (ataque, golpes_posibles)
    
def ayuda():
    print("-- Información del juego --")
    print("Tienes cuatro armas a tu disposición.\n")
    print("El arma más débil es el montón de piedras, mientras que el arma más")
    print("poderosa es el arco sagrado. La primera arma que uses tiene solo el")
    print("80% de probabilidades de acertar, en cambio, la última que uses")
    print("tiene el 30% de probabilidad de acertar.")
    print("\nElige tus armas sabiamente.")
    input("Oprime cualquier tecla para continuar...")

def mostrarInfo(salud_dragon, probabilidad_golpear, turnos_restantes):
    print("@@@ SALUD DEL DRAGÓN: " + str(salud_dragon) + " @@@")
    print("@@@ TURNOS RESTANTES: " + str(turnos_restantes) + " @@@")
    print("=============================")
    print("@@@ ELIGE TU ARMA @@@")
    print("[1] Montón de piedras")
    print("\t05 daño")
    print("\tPuede golpear 4 veces")
    #print("\tPuede ser usado 3 veces")
    print("\t"
        + str(probabilidad_golpear)
        + "% de acertar al menos un golpe")
    print("-----------------------------")
    print("[2] Espada")
    print("\t15 daño")
    print("\tPuede golpear 2 veces")
    #print("\tPuede ser usado 3 veces")
    print("\t"
        + str(probabilidad_golpear)
        + "% de acertar al menos un golpe")
    print("-----------------------------")
    print("[3] Explosivos")
    print("\t30 daño")
    print("\tPuede golpear 1 vez")
    #print("\tPuede ser usado 2 veces")
    print("\t"
        + str(probabilidad_golpear)
        + "% de acertar al menos un golpe")
    print("-----------------------------")
    print("[4] Arco sagrado")
    print("\t50 daño")
    print("\tPuede golpear 1 vez")
    #print("\tPuede ser usado 1 vez")
    print("\t"
        + str(probabilidad_golpear)
        + "% de acertar al menos un golpe")
    print("-----------------------------")

def juego():
    num_turnos = 5
    vida_dragon = 100
    turno_actual = 0
    # Se acaba si el dragón se queda sin vidas o se acaban los turnos.
    while (turno_actual < num_turnos) and (vida_dragon >= 0):
        turnos_restantes = num_turnos - turno_actual
        prevision_danno = probabilidadAcierto(turno_actual)
        os.system("clear")
        mostrarInfo(vida_dragon, prevision_danno, turnos_restantes)
        eleccion_arma = int(input(">>> Elige tu arma: "))
        atq = establecerDanno(eleccion_arma)[0]
        gol = establecerDanno(eleccion_arma)[1]
        danno = calcularDanno(atq, gol, turno_actual)
        print("¡¡Le has quitado " + str(danno) + " vidas al dragón!!")
        time.sleep(3)
        vida_dragon -= danno
        turno_actual += 1
    
    if vida_dragon > 0:
        print("Agotado, te das cuenta de la verdad: Has usado todas tus")
        print("herramientas y no has podido acabar con el dragón")
        print("Decides correr, mejor prevenir que lamentar.")
        print("\nDERROTA")
    else:
        print("Tras una ardua batalla, el dragón se retira indignado,")
        print("haciendo notar que has interrumpido su sueño")
        print("- ¡La gente ya no tiene respeto!, sobre todo usted,")
        print("   amigo mío. Me voy, iré a un lugar más tranquilo.")
        print("\nVICTORIA")
    input("Presiona cualquier tecla para continuar... ")

ejecutar = 1 
while ejecutar != 0:
    os.system("clear")
    print("/ \-------------------------------------------, ")
    print("\_,|                                          | ")
    print("   |    DERROTA AL DRAGÓN DE LAS CIEN VIDAS   | ")
    print("   |  ,-----------------------------------------")
    print("   \_/________________________________________/ ")
    print("\n## Menú principal ##")
    print("[1] Jugar")
    print("[2] Ayuda")
    print("[3] Créditos")
    print("[4] Salir del juego")
    opcion = input(">>> Elige una opcion: ")
    
    if opcion == "1":
        juego()
    elif opcion == "2":
        ayuda()
    elif opcion == "3":
        print("Escrito por Umbral1013.")
        print("8 de febrero del 2024.")
        input("Presiona una tecla para continuar...")
    elif opcion == "4":
        ejecutar = 0
        print("¡Hasta pronto, aventurero!")

input("El programa ha terminado. Presiona una tecla para continuar.")

"""NOTAS:
Quizá para hacerlo más difícil podría reducir el daño que hacen las 
armas, o cambiar la probabilidad de ciertos ataques... No se, quizá 
después veo eso.
Falta implementar lo del número de usos máximos de las armas.
"""
