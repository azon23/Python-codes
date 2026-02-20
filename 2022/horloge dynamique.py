from turtle import*
from time import *

t = Turtle()
setup(600,500) #construit une fenêtre de 600 pixels de largeur et de 500 pixels de hauteur.
bgcolor("white")# la couleur du fond (background)
dot(10,'black') # la l'épaisseur et la couleur du point au ncentre du cercle
up()
goto(0,-170) # la création d'un cercle de 180 pixels | coordonnée du curseur au départ
down()
ht()

color('black') # la couleur du cercle
pensize(6)
circle(170) #la construction d'un cercle de 180 pixels
ht()


t.penup() #pour enlever les traits qui relie le point aux heures
t.home()
t.left(90) # 90 degrés pour mettre les chiffres dans l'odre
#pour faire les heures
for i in range(12):
    t.right(360/12) # change la longueur entre les heures
    t.forward(150)# change la taille du cercle des heures
    t.write((i+1)) #pour que les heurs commence par 1 allant a 12
    t.goto(0,0)
    ht()
ht()

class aiguille:
    def __init__(self, quelle, epaisseur, taille): # on a définit par une fonction def les paramètre pour créer les aiguille d'une horloge
        self.tortue= Pen() # paramètre qui aide à déssiner les aiguilles
        self.epaisseur= epaisseur # définit l'épaisseur des différents aiguilles
        self.taille= taille # définit la taille des différentes aiguilles
        self.valeur_temps= {'h':3, 'm':4, 's':5 }[quelle] # définit
        self.denominateur= {'h':12, 'm':60, 's':60}[quelle]


    def tracer(self):#
        self.tortue.reset()
        self.tortue.speed(0)
        self.tortue.pensize(self.epaisseur)
        self.tortue.setheading(450-(360*localtime()[self.valeur_temps]/self.denominateur))
        self.tortue.forward(self.taille)

def main():
    h = aiguille('h', 4, 60)
    m = aiguille('m', 2, 90)
    s = aiguille('s', 0, 120)
    while True:
        h.tracer()
        m.tracer()
        s.tracer()
        sleep(1)

main()
