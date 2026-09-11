from turtle import *
import random
largeur = 140
hauteur = 60
x1 = 0
y1 = 0
goto (x1, y1)
couleur1 = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
def etage0():
    pendown()
    begin_fill()
    fillcolor(couleur1)

    pencolor(couleur1)
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)
    forward(largeur)
    left(90)    
    forward(hauteur)
    

etage0()
goto (x1, y1 + hauteur)
setheading(0)
etage0()
done()