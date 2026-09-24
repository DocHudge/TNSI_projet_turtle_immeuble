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


def porte():
    penup()
    goto(x1 + 55, y1)
    setheading(0)
    pendown()
    begin_fill()

    forward(30)
    left(90)
    forward(60)
    left(90)
    forward(30)
    left(90)
    forward(60)

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

#tkt c'est de la frappe mon roh
penup()
goto(x1, y1)
etage0()

penup()
goto(x1, y1 + hauteur)
setheading(0)
etage0()

porte()

fenetre(x1 + 20, y1 + hauteur + 15)
fenetre(x1 + 90, y1 + hauteur + 15)

done()