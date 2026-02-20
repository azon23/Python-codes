import string
from pyperclip import copy
from random import randint, choice
from tkinter import *

def pwd_generator():
    punctuation = r"""-._#"""

    # generateur de mot de passe
    def generate_password():
        pwd_min = 8
        pwd_max = 12
        all_char = string.ascii_letters + punctuation + string.digits
        password = "".join(choice(all_char) for x in range(randint(pwd_min, pwd_max)))
        pwd_input.delete(0, END)
        pwd_input.insert(0, password)
        copy(password)

    # fenetre
    win = Tk()
    win.title('Password generator')
    win.iconbitmap(r"C:\Users\HP\Documents\Files\scripts\Test ressources\ico_bitmap\cat.ico")
    win.minsize(900, 300)
    win.config(background='#4682B4')

    # centrage de la fenêtre à l'affichage
    screen_x = int(win.winfo_screenwidth())
    screen_y = int(win.winfo_screenheight())
    window_x = 800
    window_y = 600
    posX = (screen_x //2) - (window_x // 2)
    posY = (screen_y //2) - (window_y // 2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    win.geometry(geo)

    # frame principale
    frame = Frame(win, bg="#4682B4")

    # image à gauche de la frame principale
    w = 300
    h = 300
    image = PhotoImage(file="C:\\Users\\HP\\Documents\\Files\scripts\\Test ressources\\password.png").subsample(2)
    canvas = Canvas(frame, width=w, height=h, bg='#4682B4', bd=0, highlightthickness=0)
    canvas.create_image(w/2, h/2, image=image)
    canvas.grid(row=0, column=0, sticky=W)

    # sous-frame dans la frame principale à droite de l'image
    right_frame = Frame(frame, bg="#4682B4")

    # contenu (titre, entrée, bouton)
    title = Label(right_frame, text="Password", font=("Arial", 40), bg="#4682B4", fg="white")
    title.pack()
    pwd_input = Entry(right_frame, font=("Arial", 40), bg="#4682B4", fg="white")
    pwd_input.pack()
    btn = Button(right_frame, text="Create", font=("Arial", 30), bg="white", fg="#4682B4", command=generate_password)
    btn.pack(fill=X)

    # right_frame à droite de main frame
    right_frame.grid(row=0, column=1, sticky=W)

    # show main frame
    frame.pack(expand=YES)

    # show window
    win.mainloop()

pwd_generator()