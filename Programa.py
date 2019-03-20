#Emiliano Tartarini Rodriguez
#A01372663
#Mision 5

import math
import random
import pygame

ancho=900
alto=900
Blanco=(255,255,255)
VerdeBandera=(27,94,32)
Rojo=(255,0,0)
Azul=(0,0,255)
Negro=(0,0,0)

def dibujoCuadroCirculo():
    pygame.init()
    ventana=pygame.display.set_mode((ancho,alto))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type==pygame.quit():
                termina=True

    ventana.fill(Blanco)
    trazarCuadroCirculos(ventana)
    pygame.quit()

def EstrellaLinea():
    for y in range(0,alto//2,10):
        xFinal=y+410
        colorAleatoreo=generarColor()
        pygame.draw.line(ventana,colorAleatoreo,(alto // 2, y),(xFinal, alto // 2))
    for y in range(0,alto//2,10):
        xFinal=410-y
        colorAleatorio=generarColor()
        pygame.draw.line(ventana,colorAleatorio,(alto // 2, y),(xFinal, alto // 2))
    for y in range(0,alto//2,10):
        xFinal=y+410
        colorAleatoreo=generarColor()
        pygame.draw.line(ventana,colorAleatoreo,(y,ancho//2),(alto//2,xFinal))
    for y in range(0, alto // 2, 10):
        xFinal = alto - y
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio,(alto//2,y+ancho//2),(xFinal, alto // 2))

def DoceCirculos(ventana):
    for alfa in range (30, 370,30):
        angulo= math.radians(alfa)
        x = 160*math.cos(angulo)
        y = 160*math.sin(angulo)
        pygame.draw.circle(ventana,Negro,(int(x+alto//2),int(alto//2-y)),160,1)

def Circulos():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.quit():

        ventana.fill(Blanco)
        dibujarDoceCirculos(ventana)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def PI(n):
    Suma=0

    for denominador in range(1,(n+1)):
        frac=1/denominador**2
        Suma += frac

    Suma=Suma*6
    PI=Suma**0.5
    return PI

def Operaciones():
    calculo=0
    for n1 in range (1,10):
        calculo=calculo*10+n1
        total=calculo*8+n1
        print(calculo,n1,"=",total)
    print()

    operacion2 = 0
    for n2 in range (1, 10):
        Calculo2=calculo2*10+1
        Total2=Calculo2*Calculo2
    print(calculo2,"*",Calculo2,"=",Total2)


def main():
    print("qué quiere hacer")
    print("cuadrados y círculos 1")
    print("parábolas 2")
    print("círculos 3")
    print("Aproximar PI 4")
    print("divisibles de 19 5")
    print("pirámides de números 6")
    print("Salir 0")
    print()
    print("¿Qué hacemos?")

