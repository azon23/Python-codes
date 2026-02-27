from PIL import Image
import os


def defi_1(image):
    pixels = image.load()
    for x in range(2):
        for i in range(image.width):
            pixels[i,x] = (0,0,255)
    image.show()


def defi_2(image):
    pixels = image.load()
    for x in range(5):
        for i in range(image.width):
            pixels[i,x] = (0,255,0)
            pixels[i,397-x] = (0,255,0)
        for i in range(image.height):
            pixels[x,i] = (0,255,0)
            pixels[327-x, i] = (0,255,0)
    image.show()


def defi_3(image):
    pixels = image.load()
    for l in range(image.width):
        for h in range(image.height):
            if pixels[l,h][0] >= 230 and pixels[l,h][1] >= 230 and pixels[l,h][2] >= 230:
                pixels[l,h] = (0,0,255)
    image.show()


def defi_4(image):
    new = Image.new("RGB", (image.width , image.height))

    canard_px = image.load()
    new_px = new.load()
    l = 328
    h = 398

    for l in range(l):
        for h in range(h):
            new_px[l,h] = canard_px[327-l, 397-h]
            new_px[327-l,397-h] = canard_px[l, h]

    new.show()


def defi_5(image):
    new = Image.new("RGB", (image.width , image.height))

    canard_px = image.load()
    new_px = new.load()
    l = 328
    h = 398

    for l in range(l):
        for h in range(h):
            new_px[l-99,h] = canard_px[l, h]

    new.show()


def defi_6(image):
    pixels = image.load()
    for l in range(image.width):
        for h in range(image.height):
            if pixels[l,h][0] <= 20 and pixels[l,h][1] <= 20 and pixels[l,h][2] <= 20:
                pixels[l,h] = (0,0,255)
    image.show()


abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

image_file = Image.open(fr"{rel_path}\Ressources\duck.jpg")
# print(image.size)


print("\nQuelle fonction voulez-vous appliquer à l'image ?\n1 : Changer la couleur de la bordure supérieur\n2 : Changer la couleur de toute la bordure \n3 : Changer la couleur des pixels blancs\n4 : Inverser l'image\n5 : Découpe origami\n6 : Changer la couleur du contour (pixels noirs)\n\nS : Afficher l'image originale")
asciiType = str(input("\nVotre choix : "))

if asciiType == "1":
    defi_1(image_file)
elif asciiType == "2":
    defi_2(image_file)
elif asciiType == "3":
    defi_3(image_file)
elif asciiType == "4":
    defi_4(image_file)
elif asciiType == "5":
    defi_5(image_file)
elif asciiType == "6":
    defi_6(image_file)
elif asciiType == "S":
    image_file.show()
else:
    print("Veuillez entrer un choix valide")