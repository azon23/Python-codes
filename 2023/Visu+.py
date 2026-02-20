import os
from tkinter import *
from PIL import ImageTk, Image

#########################################################
abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)
bg_color = '#202120'
font = ('Calibri', 12)

# config
root = Tk()
root.title('Visu+')
#root.iconbitmap(fr'{rel_path}')
root.state('zoomed')
#root.minsize(weight, height)
root.config(background=bg_color)

############## Image research ##############################################################################
def clear_view():
    for widget in frame.children.values():
        widget.destroy()


def preview(folder):
    clear_view()

    file_number = 0       # compteur = nombres de fichiers
    list = []
    systemfiles = ["Default.rdp", "desktop.ini"]     # fichiers-système à ne pas afficher après l'analyse
    path = folder
    if not folder.endswith("\\"):
        path = folder + "\\"

    for element in os.listdir(path):
        if '.' in element:  # permet d'exclure les dossiers de la recherche(les noms dossiers n'ont pas de points car ils n'ont pas d'extension [ex: 3])
            if element in systemfiles:   # si l'élément est dans la list des fichiers systèmes alors ne pas afficher (passer)
                continue
            elif element[0] == '.':
                continue
            else:   # sinon compter comme un fichier normal à afficher
                file_number += 1
                list.append(element)
        else:
            continue
    print(f"\nIl y {file_number} fichiers dans le dossier '{path}'\n")

    ############## Image formating ##############################################################################
    try:
        def new_image(number, path, name, r, c):
            globals()[f"sub_frame_{number}"] = Frame(frame, bg=bg_color)

            canvas = Canvas(globals()[f"sub_frame_{number}"], bg=bg_color, highlightthickness=1, width=120, height=106)
            canvas.pack(pady=4, expand=YES)

            globals()[f"image_{number}"] = Image.open(fr"{path}")
            print(globals()[f"image_{number}"].size)
            #size_y = 106
            #factor = int(globals()[f"image_{number}"].height/size_y)
            #size_x = int(globals()[f"image_{number}"].height/factor)

            factor_x = round(globals()[f"image_{number}"].width / int(canvas.cget('width')))
            factor_y = round(globals()[f"image_{number}"].height / int(canvas.cget('height')))
            factor = factor_x if factor_x > factor_y else factor_y
            globals()[f"background_{number}"] = ImageTk.PhotoImage(globals()[f"image_{number}"].reduce(factor)) # resize((size_x, size_y))
            print(globals()[f"image_{number}"].reduce(factor).size, factor_x, factor_y, "\n\n")
            canvas.create_image(int(canvas.cget('width'))//2, int(canvas.cget('height'))//2, image=globals()[f"background_{number}"], anchor='center')
            canvas.create_text(129, 122, text=name, font=font, fill='white')

            globals()[f"sub_frame_{number}"].grid(row=r, column=c, sticky='nsew', padx=5, pady=2)

            frame.rowconfigure(r, weight=1)
            frame.columnconfigure(c, weight=1)

            return (int(canvas.cget('width')), int(canvas.cget('height')))

    ############## MIDDLE FRAME ##########################################################################
        count = 1
        row = 1
        column = 0
        for file in list:
            canvas_w = new_image(number=count, path=path+file, name=file, c=column, r=row)
            if column >= root.winfo_screenwidth()//(canvas_w[0] if canvas_w[0]>canvas_w[1] else canvas_w[1]):
                column = -1
                row += 1

            count += 1
            column += 1
    except Exception:
        print("Error at", file)
        pass

search_frame = Frame(root, bg=bg_color)

search_entry = Entry(search_frame, font=("Roboto", 20), width=50, fg='white', bg='#272822', relief='solid', highlightthickness=1)
search_entry.pack(side='left', padx=5, fill='y')
search_button = Button(search_frame, text="Charger", font=("Roboto", 17, "bold"), fg='White', bg='#272822', width=20, command=lambda: preview(search_entry.get()))
search_button.pack(side='right', padx=5)

search_frame.pack(pady=10)

frame = Frame(root, bg=bg_color)
frame.pack(expand=YES, anchor="nw", padx=10, pady=20)

folder = r"C:\Users\HP\Pictures\Fonds d'écrans".replace('"', '')+"\\"
preview(folder=folder)

menu_bar = Menu()
menu_bar.add_command(label='Pictures folder', command=lambda: preview(r"C:\Users\HP\Pictures\\"))
root.config(menu=menu_bar)



root.mainloop()