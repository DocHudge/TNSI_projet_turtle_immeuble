from turtle import *
import random

largeur = 140
hauteur = 60

x1 = 0
y1 = 0

couleur1 = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])

color("black", couleur1)


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


def rectangle(largeur, hauteur):
    for i in range(2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)


def porte_simple(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()
    rectangle(30, 50)
    end_fill()


def porte_arrondie(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()

    forward(30)
    left(90)
    forward(40)

    left(90)
    circle(15, 180)

    left(90)
    forward(40)

    end_fill()


def fenetre(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()
    rectangle(30, 30)
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


def porte_fenetre(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()
    rectangle(30, 50)
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
    left(90)
    forward(5)
    left(90)
    forward(40)
    left(90)
    forward(5)

    for i in range(5):
        penup()
        goto(x + i * 8, y)
        setheading(90)
        pendown()
        forward(12)

#c'est de la bonne mon roh tkt
penup()
goto(x1, y1)
etage0()

penup()
goto(x1, y1 + hauteur)
setheading(0)
etage0()

porte_arrondie(x1 + 20, y1)

fenetre(x1 + 85, y1 + hauteur + 15)

porte_fenetre(x1 + 25, y1 + hauteur + 5)
balcon(x1 + 20, y1 + hauteur + 5)


done()