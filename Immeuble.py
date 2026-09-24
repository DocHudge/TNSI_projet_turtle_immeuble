from turtle import *
import random
import math

largeur = 140
hauteur = 60

x1 = 0
y1 = 0

couleur1 = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])

color("black", couleur1)

#j'ai fait de la merde avec les couleurs je repush après c'est la D là

def etage0():
    pendown()
    begin_fill()

    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    forward(largeur)
    left(90)
    forward(hauteur)

    end_fill()


def fenetre(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()

    for i in range(4):
        forward(30)
        left(90)

    end_fill()

    penup()
    goto(x + 15, y)
    setheading(90)
    pendown()
    forward(30)

    penup()
    goto(x, y + 15)
    setheading(0)
    pendown()
    forward(30)


def porte(x, y):
    penup()
    goto(x, y)
    setheading(90)
    pendown()

    begin_fill()

    forward(40)

    centre_x = x + 15
    centre_y = y + 40

    for angle in range(180, -1, -10):
        px = centre_x + 15 * math.cos(math.radians(angle))
        py = centre_y + 15 * math.sin(math.radians(angle))
        goto(px, py)

    goto(x + 30, y)

    goto(x, y)

    end_fill()


def porte_fenetre(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()

    for i in range(2):
        forward(30)
        left(90)
        forward(50)
        left(90)

    end_fill()

    penup()
    goto(x + 15, y)
    setheading(90)
    pendown()
    forward(50)


def balcon(x, y):
    penup()
    goto(x - 5, y)
    setheading(0)
    pendown()

    forward(40)

    penup()
    goto(x - 5, y)
    setheading(90)
    pendown()
    forward(12)

    penup()
    goto(x - 5, y + 12)
    setheading(0)
    pendown()
    forward(40)

    for i in range(6):
        penup()
        goto(x - 5 + i * 8, y)
        setheading(90)
        pendown()
        forward(12)

penup()
goto(x1, y1)
setheading(0)
etage0()

penup()
goto(x1, y1 + hauteur)
setheading(0)
etage0()

#porte gauche
porte(x1 + 20, y1)

#gauche mon roh
porte_fenetre(x1 + 20, y1 + hauteur + 5)
balcon(x1 + 15, y1 + hauteur + 5)

fenetre(x1 + 90, y1 + hauteur + 15)


done()