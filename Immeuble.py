from turtle import *

taille = 130
x = 0
y = 0

def carre(x, y, taille):
    down()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(taille)
        right(90)

carre(x, y, taille)