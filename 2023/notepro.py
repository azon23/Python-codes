import os.path, time
import os
from tkinter import *
from tkinter import messagebox

#########################################################
abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)
box_bg = '#acc8e5'
left_bg = '#219ebc'
right_bg = '#acc8e5'

def ouvrir():
    # config
    root = Tk()
    root.title('Note Pro Max')
    root.minsize(480, 360)
    root.iconbitmap(fr"{rel_path}\ressource\bloc-note.ico")
    root.state('zoomed')
    #root.minsize(weight, height)
    root.config(background=left_bg)

    ############## FRAME GAUCHE ##############################################################################
    active_file_path = ""
    globals()['isSaving'] = False

    # Fonction - Recherche des fichiers
    def scan():
        files = []
        path = rel_path + "\\ressource\\"
        for file in os.listdir(path):
            if file.endswith(".txt"):
                files.append(file)

        return files

    # Fonction - Rafraichissement de la page
    def refresh(files):
        counter = 1
        path = rel_path + "\\ressource\\"

        globals()['all_previews_frame'].destroy()
        
        scrollbar_y = Scrollbar(frame_left, orient=VERTICAL)
    
        globals()['all_previews_frame'] = Listbox(frame_left, bg=left_bg, highlightthickness=0, relief='flat', yscrollcommand=scrollbar_y.set)
        globals()['all_previews_frame'].pack(fill='both')

        scrollbar_y.config(command=globals()['all_previews_frame'].yview)

        for file in files:
            set_preview(file=path+file, number=counter, name=file)
            counter += 1
        
        return files

    def Sauvegarde():
        final = zone_texte.get(1.0, END)
        with open(globals()["active_file_path"], 'w') as fichier1:
            fichier1.write(final[0:-1])
            fichier1.close()

    
    def on_click(event):
        if globals()['isSaving'] == True:
            Sauvegarde()

        id = event.widget['repeatdelay']
        path = globals()[f"file_path_{id}"]
        name = globals()[f"file_name_{id}"]
        date_modif = time.ctime(os.path.getctime(path))

        root_title.config(text=name.replace('.txt', '')[0:34])
        root_time.config(text=str(date_modif))

        with open(path, 'r', encoding='ansi') as file:
            content = file.readlines()
            zone_texte.delete(1.0, END)
            zone_texte.insert(1.0, "".join(content))
            file.close()

        globals()['active_file_path'] = path
        globals()['isSaving'] = True

        refresh(scan())

    # Fonction - Setup des aperçus    
    def set_preview(file, number, name):

        def show_preview(filePath, name):
            with open(filePath, 'r', encoding='ansi') as file:
                content = file.readlines()

                globals()[f'preview_title_{number}'].config(text=name.replace('.txt', ''), textvariable=name)
                
                preview_text = ''
                for i in range(0, 3):
                    try:
                        preview_text += content[i][0:35]
                    except Exception:
                        break
                
                globals()[f'preview_content_{number}'].config(text=preview_text)
                globals()[f'file_path_{number}'] = filePath
                globals()[f'file_name_{number}'] = name
                
                file.close()


        globals()[f'preview_frame_{number}'] = Frame(globals()['all_previews_frame'], bg=left_bg)

        globals()[f'preview_title_{number}'] = Button(globals()[f'preview_frame_{number}'], repeatdelay=number, width=20, font=('Arial Black', 18, 'bold'), height=1, foreground='#404040', activeforeground='white', disabledforeground='white', background=box_bg, activebackground=box_bg, borderwidth=0, anchor='w', justify='left', relief='flat')
        globals()[f'preview_title_{number}'].pack(expand=True, fill='x')
        globals()[f'preview_content_{number}'] = Button(globals()[f'preview_frame_{number}'], repeatdelay=number, width=20, font=('Calibri', 14), height=3, foreground='#202020', activeforeground='white', disabledforeground='white',  background=box_bg, activebackground=box_bg, borderwidth=0, anchor='w', justify='left', relief='flat')
        globals()[f'preview_content_{number}'].pack(expand=True, fill='x')

        globals()[f'preview_title_{number}'].bind("<Button-1>", on_click)
        globals()[f'preview_content_{number}'].bind("<Button-1>", on_click)

        globals()[f'preview_frame_{number}'].pack(padx=15, pady=5, anchor='w')

        show_preview(filePath=file, name=name)


    ##########################################################################################################
    # Fonction - Création d'une nouvelle note
    def add_file():
        def submit(event=None):
            n = entry.get()
            myFile = open(rel_path + "\\ressource\\" + n + ".txt", "w+")
            myFile.close()
            roots.destroy()
            refresh(scan())

        # Boite de dialogue - Nouveau fichier
        roots = Tk()
        roots.title("Nom du fichier")
        roots.geometry("290x75")
        roots.iconbitmap(fr"{rel_path}\ressource\bloc-note.ico")
        roots.bind("<Return>", submit)
        roots.focus_force()

        entry = Entry(roots, width=30)
        entry.pack()
        entry.focus()

        submit_button = Button(roots, text="Soumettre", command=lambda: submit(event=None))
        submit_button.pack()

        root.mainloop()

    ##########################################################################################################
    # Config - frame de gauche
    frame_left = Frame(root, bg=left_bg)

    top_frame = Frame(frame_left, bg=left_bg)

    search_bar = Entry(top_frame, font=('Roboto', 15))
    search_bar.pack(fill='both', side='left', expand=YES)

    signe_plus = PhotoImage(file=fr"{rel_path}\ressource\plus.png")
    new = Button(top_frame, text='+', font=('Arial Black', 15, 'bold'), background=box_bg, image=signe_plus, command=add_file)
    new.pack(side='right')

    def search(e):
        notetext_dict = {}
        path = rel_path + "\\ressource\\"
        for file in os.listdir(path):
            if file.endswith(".txt"):
                with open(path+file, 'r', encoding='ansi') as note:
                    content = note.readlines()
                    notetext_dict[file] = "".join(content)
                    note.close()

        key_word = search_bar.get()
        results = []
        for file in notetext_dict.keys():
            if key_word.lower() in notetext_dict[file].lower():
                results.append(file)
        
        if len(results) != 0:
            refresh(results)
        else:
            root1 = Tk()
            root1.withdraw()
            root1.minsize(480, 360)
            root1.iconbitmap(fr"{rel_path}\ressource\bloc-note.ico")
        
            print("Aucun résultat trouvé.")
            messagebox.showinfo("Message", "Aucun résultat.")                


    loupe = PhotoImage(file=fr"{rel_path}\ressource\loupe.png")
    search_button = Button(top_frame, text='+', font=('Arial Black', 15, 'bold'), background=box_bg, image=loupe, command=search)
    search_button.pack(side='right', padx=5)
    root.bind('<Return>', search)

    top_frame.pack(pady=10, padx=15, fill='x', side='top')

    globals()['all_previews_frame'] = Listbox(frame_left, bg=left_bg)
    globals()['all_previews_frame'].pack(fill='both')

    frame_left.pack(side="left", fill='both')

 
    ###################  FRAME DROITE  #######################################################################
    frame_right = Frame(root, bg=right_bg)
    frame_right_up = Frame(frame_right, bg=right_bg)
    frame_right_up1 = Frame(frame_right_up, bg=right_bg)
    frame_right_up2 = Frame(frame_right_up, bg=right_bg)
    frame_right_down = Frame(frame_right, bg=right_bg)

    #################### menu du haut 
    def delete():
        if os.path.exists(globals()["active_file_path"]):
            os.remove(globals()["active_file_path"])
            globals()['isSaving'] = False
            root1 = Tk()
            root1.withdraw()
            root1.minsize(480, 360)
            root1.iconbitmap(fr"{rel_path}\ressource\bloc-note.ico")
            
            messagebox.showinfo("Fichier supprimé", "Ce fichier a été supprimmé avec succès")
            refresh(scan())
            
        else:
            root2 = Tk()
            root2.withdraw()
            root2.minsize(480, 360)
            root2.iconbitmap(fr"{rel_path}\ressource\bloc-note.ico")
            messagebox.showinfo("Fichier supprimé", "Ce fichier n'existe pas. Il n'a donc pas pu être supprimmé")
        

    root_title = Label(frame_right_up1, font=('Courier', 20, 'italic', 'bold'),  text="", bg=right_bg, fg='Black')
    root_title.pack(side='left', pady=20, padx=10)

    root_time = Label(frame_right_up1, font=('Courier', 16), text="", bg=right_bg, fg='Black')
    root_time.pack(side='right', pady=20)

    border_radius = PhotoImage(file=fr"{rel_path}\ressource\shape.png")
    supprimer = Button(frame_right_up2, text='  Delete  ', font=('Roboto', 14, 'bold'), fg='white', bg=right_bg, activebackground=right_bg, borderwidth=0, image=border_radius, command=delete)
    supprimer.pack(side='right', padx=5, pady=20)

    line = PhotoImage(file=fr"{rel_path}\ressource\separator.png")
    separator = Button(frame_right_down, image=line, bg=right_bg, height=1, anchor='center', borderwidth=0)
    separator.pack(side='top', fill='x', padx=10, pady=20)

    zone_texte = Text(frame_right_down, font=('Dubai', 16), bg=right_bg, fg='Black', borderwidth=0)
    zone_texte.pack(padx=10, pady=10, fill='both', expand=True)

    frame_right_up1.pack(side=LEFT, fill=X, expand=True)
    frame_right_up2.pack(side=RIGHT)
    frame_right_up.pack(side=TOP, fill=X)
    frame_right_down.pack(fill=BOTH, expand=YES)
    frame_right.pack(fill=BOTH, expand=True)

    ##########################################################################################################
    refresh(scan())
    root.mainloop()

ouvrir()
pass

# scrollBar
# after loop
# renommer