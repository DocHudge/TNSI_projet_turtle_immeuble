from turtle import *
import random
import math

largeur = 140
hauteur = 60

x1 = -600
y1 = -85

speed(0)


pencolor("black")


"""Un seul bâtiment mais maintenant il est random au moins"""


def route (x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    fillcolor("grey")
    begin_fill()

    forward(2000)
    right(90)
    forward(5)
    right(90)
    forward(2000)
    right(90)
    forward(5)

    end_fill()

def ciel(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    fillcolor("#B3E9FF")
    begin_fill()

    forward(2000)
    left(90)
    forward(700)
    left(90)
    forward(2000)
    left(90)
    forward(700)

    end_fill()

def niveau(x, y):
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

#le balcon est joli maintenant
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

def toit_plat(x, y):
    penup()
    goto(x - 10, y)
    setheading(0)
    pendown()

    fillcolor(couleur_toit)
    begin_fill()

    goto(x + largeur + 10, y)
    goto(x + largeur + 10, y + 10)
    goto(x - 10 + largeur + 10, y + 10)
    goto(x - 10, y)

    end_fill()


#NE PAS TOUCHER CA CASSE LE CODE 

"""
#ça faut pas y toucher ça fonctionne pour faire un immeuble correct

niveaux = random.randint(1, 4)

for i in range(niveaux):
    niveau(x1, y1 + i * hauteur)

toit(x1, y1 + niveaux * hauteur)

positions = [x1 + 15, x1 + 55, x1 + 95]

position_porte = random.choice(positions)
porte(position_porte, y1)

for position in positions:
    if position != position_porte:
        fenetre(position, y1 + 15)

for niveau_actuel in range(1, niveaux):
    y = y1 + niveau_actuel * hauteur + 5

    for position in positions:
        ouverture = random.choice(["fenetre", "porte_fenetre"])

        if ouverture == "fenetre":
            fenetre(position, y + 10)
        else:
            porte_fenetre(position, y)
            balcon(position, y)
"""
ciel(-1000, -85)
route(-1000, -85)
for i in range(6):
    niveaux = random.randint(1, 4)
    couleur_facade = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
    couleur_porte = random.choice(["brown"])
    couleur_vitre = "cyan"
    couleur_toit = random.choice(["darkgrey", "grey", "brown"])

    for i in range(niveaux):
        niveau(x1, y1 + i * hauteur)

    toits = [toit, toit_plat]
    choix_toit = random.choice(toits)
    choix_toit(x1, y1 + niveaux * hauteur)

    positions = [x1 + 15, x1 + 55, x1 + 95]

    position_porte = random.choice(positions)
    porte(position_porte, y1)

    for position in positions:
        if position != position_porte:
            fenetre(position, y1 + 15)

    for niveau_actuel in range(1, niveaux):
        y = y1 + niveau_actuel * hauteur + 5

        for position in positions:
            ouverture = random.choice(["fenetre", "porte_fenetre"])

            if ouverture == "fenetre":
                fenetre(position, y + 10)
            else:
                porte_fenetre(position, y)
                balcon(position, y)
    penup()

    x1 += 220
    goto(x1 +260, y1)
done()