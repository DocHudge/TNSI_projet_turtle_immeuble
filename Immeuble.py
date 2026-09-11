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

penup()
goto(x1, y1)
etage0()

penup()
goto(x1, y1 + hauteur)
setheading(0)
etage0()

done()
