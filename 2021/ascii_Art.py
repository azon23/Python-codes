class Point():
    def __init__(self, x, y):
        self.abscisse = x
        self.ordonnee = y

    def deplacement(self, dx, dy):
        self.abscisse = self.abscisse + dx
        self.ordonnee = self.ordonnee + dy# Banque d'images
'''
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\thinking man.jpg"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\dog.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\plant.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\desert_portal.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\rainbow dogs.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\pomme.jpg"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\yt1s_logo.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\luffy.png"
'''

import ascii_magic
from PIL import Image
import sys
def ascii_ART():
    # on définit deux fonctions qui correspondent aux deux types d'ascii qu'on veut générer
    def symbol_ascii(a):
        with Image.open(a) as image:
            image = image.resize((30, 30))
            ascii_char = ' .:-=+*#%@'
            for y in range(image.height):
                line = ""
                for x in range(image.width):
                    rgb = image.getpixel((x, y))
                    grey = sum(rgb) // len(rgb)
                    index = grey * 9 // 255
                    line += ascii_char[index] + "  "
                print(line)

    def color_ascii(a):
        output = ascii_magic.from_image_file(a,columns=148,char="#")
        ascii_magic.to_terminal(output)

    # boucle while pour plus de confort et éviter que la fenêtre du cmd ne se ferme
    while True:
        try:
            image = input("\nEntrez le chemin de l'image: ").replace('"', '')
            if image == "exit" or image == "quit":
                break
            
            print("\nQuel type d'image ASCII voulez-vous faire générer ? Tapez 1 ou 2\n1- ASCII de symboles\n2-ASCII en couleur")
            asciiType = str(input("\nVotre choix : ")) # demande à l'utilisateur de faire un choix d'ascii

            if asciiType == "1":
                symbol_ascii(image) # image est une variable qui contient le chemin de l'image
            elif asciiType == "2":
                color_ascii(image)
            elif asciiType == "exit" or asciiType == "quit":
                break
            else:
                print("Veuillez entrer un choix valide")
                continue
        except Exception:
            print("\n\t\t***\nL'image choisi ne peut pas être utilisé.\nVeuillez choisir une autre image...\n\t\t***".upper())
            continue

ascii_ART()