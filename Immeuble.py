from turtle import *
import random
import math

largeur = 140
hauteur = 60

x1 = -70
y1 = -85


couleur_facade = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
couleur_porte = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "brown", "white"])
couleur_vitre = "cyan"
couleur_toit = "saddlebrown"

pencolor("black")

""" J'ai fait qu'un immeuble simple qui est pas généré aléatoirement pour l'instant
 mais déjà j'ai rattrapé mon retard et c'est moins moche alors je m'en contente."""
def niveau(x, y):
    """Dessine un niveau. j'ai bien prototypé comme un grand"""
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    fillcolor(couleur_facade)
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

    fillcolor(couleur_vitre)
    begin_fill()

    for i in range(4):
        forward(30)
        left(90)

    end_fill()

    #putain de barrière qui est moins moche normalement
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

    fillcolor(couleur_porte)
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

    fillcolor(couleur_vitre)
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


def toit(x, y):
    penup()
    goto(x - 10, y)
    setheading(0)
    pendown()

    fillcolor(couleur_toit)
    begin_fill()

    goto(x + largeur + 10, y)
    goto(x + largeur / 2, y + 45)
    goto(x - 10, y)

    end_fill()


#ça fonctionne bien maintenant
niveau(x1, y1)
niveau(x1, y1 + hauteur)
toit(x1, y1 + 2 * hauteur)

porte(x1 + 20, y1)
fenetre(x1 + 60, y1 + 15)
fenetre(x1 + 100, y1 + 15)

porte_fenetre(x1 + 20, y1 + hauteur + 5)
balcon(x1 + 20, y1 + hauteur + 5)
fenetre(x1 + 55, y1 + hauteur + 15)
fenetre(x1 + 90, y1 + hauteur + 15)

done()