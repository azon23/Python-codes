from turtle import*
from time import *
import turtle

user_hour = int(input("Entrez l'heure : "))
user_minute = int(input("Entrez la minute : "))

t=turtle.Turtle()
setup(600,500) #construit une fenêtre de 600 pixels de largeur et de 500 pixels de hauteur.
bgcolor("white")# la couleur du fond (background)
dot(10,'black') # la l'épaisseur et la couleur du point au ncentre du cercle
up()
goto(0,-170) # la création du'un cercle de 180 pixels
down()

color('black') # la couleur du cercle
circle(170) #la construction d'un cercle de 180 pixels


t.penup() #pour enlever les traits qui relie le point aux heures
t.home()
t.left(90) # 90 degrés pour mettre les chiffres dans l'odre
#pour faire les heures
for i in range(12):
    t.right(360/12) # change la longueur entre les heures
    t.forward(140)# change la taille du cercle des heures
    t.write((i+1)) #pour que les heurs commence par 1 allant a 12
    t.goto(0,0)

def draw_hour_arm(hour):
    t.penup()
    t.home() #Cette fonction est utilisée pour déplacer la tortue à l’origine
    t.left(90)
    t.right(hour*30)
    t.pendown()
    t.pensize(6)
    t.forward(70)

def draw_minute_arm(minute):
    t.penup()
    t.home()#Cette fonction est utilisée pour déplacer la tortue à l’origine
    t.left(90)# trouner à droite de 270
    t.right(minute*6)
    t.pendown()#c'est l’état par défaut de la tortue
    t.pensize(3)
    t.forward(110)

draw_hour_arm(user_hour)
draw_minute_arm(user_minute)

done()