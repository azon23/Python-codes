# Exemple d'images
'''
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\donald.jpg"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\desert_portal.png"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\pomme.jpg"
"C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\thinking man.jpg"
'''

from PIL import Image
import sys

separator = '\n--------------------------------------------'
def Image_effect():
    path = input("\nCHEMIN DE L'IMAGE: ").replace('"', '').replace("'", "")

    class modifs:
        def purple():
            img = Image.open(fr"{path}")
            largeur_image = img.width   # ou sinon:  largeur, hauteur = img.size
            hauteur_image = img.height
            for y in range(hauteur_image):
                for x in range(largeur_image): 
                    r,v,b = img.getpixel((x,y))
                    n_r = v
                    n_v = b
                    n_b = r
                    img.putpixel((x,y), (n_r,n_v,n_b))
            img.show()

        def blue():
            img = Image.open(fr"{path}")
            largeur_image = img.width   # ou sinon:  largeur, hauteur = img.size
            hauteur_image = img.height
            for y in range(hauteur_image):
                for x in range(largeur_image):
                    r,v,b = img.getpixel((x,y))
                    n_r = b
                    n_v = v
                    n_b = r
                    img.putpixel((x,y),(n_r,n_v,n_b))
            img.show()
        
        def glitch():
            img = Image.open(fr"{path}")
            largeur_image = img.width   # ou sinon:  largeur, hauteur = img.size
            hauteur_image = img.height
            for y in range(hauteur_image):
                for x in range(largeur_image):
                    r,v,b = img.getpixel((x,y))
                    if v > 100 and y > 250:
                        n_v = 0
                    else :
                        n_v = 255
                    img.putpixel((x,y),(r,n_v,b))
            img.show()

        def negatif():
            img = Image.open(fr"{path}")
            largeur_image = img.width   # ou sinon:  largeur, hauteur = img.size
            hauteur_image = img.height
            for y in range(hauteur_image):
                for x in range(largeur_image):
                    r,v,b = img.getpixel((x,y))
                    n_r = 255 - r
                    n_v = 255 - v
                    n_b = 255 - b
                    img.putpixel((x,y),(n_r, n_v, n_b))
            img.show()

        def greyscale():
            img = Image.open(fr"{path}")
            largeur_image = img.width   # ou sinon:  largeur, hauteur = img.size
            hauteur_image = img.height
            for y in range(hauteur_image):
                for x in range(largeur_image):
                    rvb = img.getpixel((x,y))
                    grey = sum(rvb) // len(rvb)
                    img.putpixel((x,y),(grey, grey, grey))
            img.show()


    print("\nEntrez le numéro du filtre à appliquer\n1 : Teinte de bleu\n2 : Teinte de violet\n3 : Noir & Blanc\n4 : Négatif\n5 : Effet glitch")
    print("\nAutres commandes:\n- A : Affiche l'image original\n- C : Changer d'image\n- exit, quit ou E : Fermer le programme")
    while True:
        if f"{path}" == "exit" or f"{path}" == "quit":
            break

        try:
            user_input = input("\nNuméro de filtre: ")
            if user_input == "1":
                modifs.blue()
                print(separator)
            elif user_input == "2":
                modifs.purple()
                print(separator)
            elif user_input == "3":
                modifs.greyscale()
                print(separator)
            elif user_input == "4":
                modifs.negatif()
                print(separator)
            elif user_input == "5":
                modifs.glitch()
                print(separator)
            elif user_input == "A" or user_input == "a":
                img = Image.open(fr"{path}")
                img.show()
                print(separator)
            elif user_input == "C" or user_input == "c":
                path = input("\nEntrez le chemin du fichier: ").replace('"', '').replace("'", "")
            elif user_input == "exit" or user_input == "quit" or user_input == "E" or user_input == "e":
                break
            else:
                print("\nNon pris en charge. Entrez un numéro correct !")
                print(separator)
                continue
        except Exception:
            print("\n\t\t***\nL'image choisi ne peut pas être utilisé.\nVeuillez choisir une autre image...\n\t\t***".upper())
            print(separator)
            Image_effect()
