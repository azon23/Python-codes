class Point():
    def __init__(self, x, y):
        self.abscisse = x
        self.ordonnee = y

    def deplacement(self, dx, dy):
        self.abscisse = self.abscisse + dx
        self.ordonnee = self.ordonnee + dy


import ascii_magic
from PIL import Image
import sys
import os
def ascii_ART(image_path):
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
    try:
        image = image_path
        if image == "exit" or image == "quit":
            return
        
        print("\nQuel type d'image ASCII voulez-vous faire générer ? Tapez 1 ou 2\n1- ASCII de symboles\n2-ASCII en couleur")
        asciiType = str(input("\nVotre choix : ")) # demande à l'utilisateur de faire un choix d'ascii

        if asciiType == "1":
            symbol_ascii(image) # image est une variable qui contient le chemin de l'image
        elif asciiType == "2":
            color_ascii(image)
        elif asciiType == "exit" or asciiType == "quit":
            return
        else:
            print("Veuillez entrer un choix valide")
            return
    except Exception:
        print("\n\t\t***\nL'image choisi ne peut pas être utilisé.\nVeuillez choisir une autre image...\n\t\t***".upper())


abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

ascii_ART(fr"{rel_path}\Ressources\thinking man.jpg")
# ascii_ART(fr"{rel_path}\Ressources\dog.png")
# ascii_ART(fr"{rel_path}\Ressources\plant.png")
# ascii_ART(fr"{rel_path}\Ressources\desert_portal.png")
# ascii_ART(fr"{rel_path}\Ressources\rainbow dogs.png")
# ascii_ART(fr"{rel_path}\Ressources\pomme.jpg")
# ascii_ART(fr"{rel_path}\Ressources\yt1s_logo.png")
# ascii_ART(fr"{rel_path}\Ressources\luffy.png")