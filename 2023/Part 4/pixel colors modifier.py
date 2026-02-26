from PIL import Image


def défi_1():
    canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\duck.jpg")
    print(canard.size)
    pixels = canard.load()
    for x in range(2):
        for i in range(canard.width):
            pixels[i,x] = (0,0,255)
    canard.show()


def défi_2():
    canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\duck.jpg")
    print(canard.size)
    pixels = canard.load()
    for x in range(5):
        for i in range(canard.width):
            pixels[i,x] = (0,255,0)
            pixels[i,397-x] = (0,255,0)
        for i in range(canard.height):
            pixels[x,i] = (0,255,0)
            pixels[327-x, i] = (0,255,0)
    canard.show()


def défi_3():
    canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\duck.jpg")
    print(canard.size)
    pixels = canard.load()
    for l in range(canard.width):
        for h in range(canard.height):
            if pixels[l,h][0] >= 230 and pixels[l,h][1] >= 230 and pixels[l,h][2] >= 230:
                pixels[l,h] = (0,0,255)
    canard.show()


def défi_4():
    canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\duck.jpg")
    new = Image.new("RGB", (canard.width , canard.height))

    canard_px = canard.load()
    new_px = new.load()
    l = 328
    h = 398

    for l in range(l):
        for h in range(h):
            new_px[l,h] = canard_px[327-l, 397-h]
            new_px[327-l,397-h] = canard_px[l, h]

    new.show()


def défi_5():
    canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\duck.jpg")
    new = Image.new("RGB", (canard.width , canard.height))

    canard_px = canard.load()
    new_px = new.load()
    l = 328
    h = 398

    for l in range(l):
        for h in range(h):
            new_px[l-99,h] = canard_px[l, h]

    new.show()


canard = Image.open(r"C:\Users\HP\Documents\Files\scripts\Web Projects\The chosen one 2\img\no.png")
pixels = canard.load()
for l in range(canard.width):
    for h in range(canard.height):
        if pixels[l,h][0] <= 20 and pixels[l,h][1] <= 20 and pixels[l,h][2] <= 20:
            pixels[l,h] = (0,0,255)
canard.show()