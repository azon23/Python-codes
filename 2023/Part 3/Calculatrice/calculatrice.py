import os
from tkinter import *
from pyperclip import copy

def send_1(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "1"
        show_result.set(False)
    else:
        display["text"] = text+"1"

def send_2(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "2"
        show_result.set(False)
    else:
        display["text"] = text+"2"

def send_3(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "3"
        show_result.set(False)
    else:
        display["text"] = text+"3"

def send_4(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "4"
        show_result.set(False)
    else:
        display["text"] = text+"4"

def send_5(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "5"
        show_result.set(False)
    else:
        display["text"] = text+"5"

def send_6(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "6"
        show_result.set(False)
    else:
        display["text"] = text+"6"

def send_7(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "7"
        show_result.set(False)
    else:
        display["text"] = text+"7"

def send_8(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "8"
        show_result.set(False)
    else:
        display["text"] = text+"8"

def send_9(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "9"
        show_result.set(False)
    else:
        display["text"] = text+"9"

def send_0(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "0"
        show_result.set(False)
    else:
        display["text"] = text+"0"

def send_dot(event=None):
    text = str(display["text"])
    display["text"] = text+"."
    show_result.set(False)

def send_exp(event=None):
    text = str(display["text"])
    display["text"] = text+"^"
    show_result.set(False)

def l_parenthese(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "("
        show_result.set(False)
    else:
        display["text"] = text+"("


def r_parenthese(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = ")"
        show_result.set(False)
    else:
        display["text"] = text+")"

def sqrt(event=None):
    text = str(display["text"])
    if show_result.get() == True:
        display["text"] = "\u221A"
        show_result.set(False)
    else:
        display["text"] = text+"\u221A"

def addition(event=None):
    text = str(display["text"])
    display["text"] = text+" + "
    show_result.set(False)

def soustraction(event=None):
    text = str(display["text"])
    display["text"] = text+" - "
    show_result.set(False)

def multiplication(event=None):
    text = str(display["text"])
    display["text"] = text+" x "
    show_result.set(False)

def division(event=None):
    text = str(display["text"])
    display["text"] = text+" / "
    show_result.set(False)

def equal(event=None):
    entry = str(display['text'])
    expression = entry


    if "x" in entry:
        entry = entry.replace('x', '*')
    if "^" in entry:
        entry = entry.replace('^', '**')
    if "\u221A" in entry:
        if '(' in entry and entry.index('(') == entry.index('\u221a')+1:
            # 10 + √(20 + 5) + 25
            sqrt_index = entry.index('\u221a')
            l_paren_index = entry.index('(')
            r_paren_index = entry.index(')')
            will_sqrt = entry[l_paren_index:r_paren_index+1] # (20 + 5)
            entry = entry.replace(entry[sqrt_index:r_paren_index+1], "math.sqrt({})".format(will_sqrt)) # 10 + math.sqrt((20+5))(20 + 5) + 25
            """print("sqrt_index : ", sqrt_index)
            print("l_paren_index : ", l_paren_index)
            print("r_paren_index : ", r_paren_index)
            print("will_sqrt : ", will_sqrt)
            print("expression : ", entry)"""
        else:
            var = entry.replace('\u221A', '')
            entry = var.replace(var, 'math.sqrt({})'.format(var))

    try:
        result = eval(str(entry))
        display["text"] = result
        # Ajoute à l'historique
        if empty_histo.get() == True:
            historique.config(state="normal")
            empty_histo.set(False)
            historique.delete(0, END)

        if entry != '()':
            historique.insert(0, "\n\n")
            historique.config(foreground="White", font=("Calibri", 20))
            historique.insert(0, result)
            historique.insert(0, expression + " = ")
    except ZeroDivisionError:
        display["text"] = "Math Error."

    show_result.set(True)

def delete(event=None):
    text = str(display["text"])
    if text[-1] == " ":
        display["text"] = text[:-3]
    else:
        display["text"] = text[:-1]

def delete_all(event=None):
    display["text"] = ""

def copy_result(event=None):
    text = str(display["text"])
    copy(text)


Font = ("Roboto", 30)
abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

root = Tk()
root.title("Calculatrice")
root.iconbitmap(fr"{rel_path}\ressources\calculator.ico")
root.config(borderwidth=0, bg="#202020")
root.state('zoomed')
root.minsize(416, 480)

root.bind("0", send_0)
root.bind("1", send_1)
root.bind("2", send_2)
root.bind("3", send_3)
root.bind("4", send_4)
root.bind("5", send_5)
root.bind("6", send_6)
root.bind("7", send_7)
root.bind("8", send_8)
root.bind("9", send_9)
root.bind(".", send_dot)
root.bind("E", send_exp)
root.bind("e", send_exp)
root.bind("S", sqrt)
root.bind("s", sqrt)
root.bind("(", l_parenthese)
root.bind(")", r_parenthese)
root.bind("+", addition)
root.bind("-", soustraction)
root.bind("*", multiplication)
root.bind("/", division)
root.bind("<Return>", equal)
root.bind("<BackSpace>", delete)
root.bind("<Delete>", delete_all)
root.bind("<Control-C>", copy_result)
root.bind("<Control-c>", copy_result)

display_frame = Frame(root, bg="#202020")

show_result = BooleanVar()
show_result.set(False)
display = Label(display_frame, font=Font, bg="#202020", foreground="White", justify='right', anchor="e", width=5)
display.pack(fill="x", anchor="n", padx=4, pady=60, expand=True)

others_bar = Frame(display_frame, bg="#202020", background='#202020')

parenthese_left = Button(others_bar, text='(', command=l_parenthese)
parenthese_left.grid(column=0, row=0, padx=2, pady=10, sticky="nsew")

parenthese_right = Button(others_bar, text=')', command=r_parenthese)
parenthese_right.grid(column=1, row=0, padx=2, pady=10, sticky="nsew")

square_root = Button(others_bar, text='\u221A', command=sqrt)
square_root.grid(column=2, row=0, padx=2, pady=10, sticky="nsew")

image = PhotoImage(file=fr"{rel_path}\ressources\copy_icon.png")
copy_btn = Button(others_bar, text="", command=copy_result)
copy_btn.config(image=image)
copy_btn.grid(column=3, row=0, padx=2, pady=10, sticky="nsew")

####################################################################
keys_frame = Frame(display_frame, background='#202020')

# Chiffres et égual
key_delete = Button(keys_frame, text="DEL", command=delete)
key_delete.grid(column=0, row=5, padx=2, pady=2, sticky="nsew")
key_exp = Button(keys_frame, text="exp", command=send_exp)
key_exp.grid(column=0, row=4, padx=2, pady=2, sticky="nsew")
key1 = Button(keys_frame, text="1", command=send_1)
key1.grid(column=0, row=3, padx=2, pady=2, sticky="nsew")
key4 = Button(keys_frame, text="4", command=send_4)
key4.grid(column=0, row=2, padx=2, pady=2, sticky="nsew")
key7 = Button(keys_frame, text="7", command=send_7)
key7.grid(column=0, row=1, padx=2, pady=2, sticky="nsew")

key_delete_all = Button(keys_frame, text="AC", command=delete_all)
key_delete_all.grid(column=1, row=5, padx=2, pady=2, sticky="nsew")
key0 = Button(keys_frame, text="0", command=send_0)
key0.grid(column=1, row=4, padx=2, pady=2, sticky="nsew")
key2 = Button(keys_frame, text="2", command=send_2)
key2.grid(column=1, row=3, padx=2, pady=2, sticky="nsew")
key5 = Button(keys_frame, text="5", command=send_5)
key5.grid(column=1, row=2, padx=2, pady=2, sticky="nsew")
key8 = Button(keys_frame, text="8", command=send_8)
key8.grid(column=1, row=1, padx=2, pady=2, sticky="nsew")

key3 = Button(keys_frame, text="3", command=send_3)
key_dot = Button(keys_frame, text=".", command=send_dot)
key_dot.grid(column=2, row=4, padx=2, pady=2, sticky="nsew")
key3.grid(column=2, row=3, padx=2, pady=2, sticky="nsew")       # Hier soir
key6 = Button(keys_frame, text="6", command=send_6)
key6.grid(column=2, row=2, padx=2, pady=2, sticky="nsew")
key9 = Button(keys_frame, text="9", command=send_9)
key9.grid(column=2, row=1, padx=2, pady=2, sticky="nsew")
key_equal = Button(keys_frame, text="=", command=equal)
key_equal.grid(column=2, row=5, padx=2, pady=2, columnspan=2, sticky="nsew")


# Signe d'opérations
addition_key = Button(keys_frame, text="+", command=addition)
addition_key.grid(column=3, row=1, padx=2, pady=2, sticky="nsew")
soustraction_key = Button(keys_frame, text="-", command=soustraction)
soustraction_key.grid(column=3, row=2, padx=2, pady=2, sticky="nsew")
multiplication_key = Button(keys_frame, text="x", command=multiplication)
multiplication_key.grid(column=3, row=3, padx=2, pady=2, sticky="nsew")
division_key = Button(keys_frame, text="/", command=division)
division_key.grid(column=3, row=4, padx=2, pady=2, sticky="nsew")


button_list=[
                key1, key2, key3, key4, key5, key6, key7, key8, key9, key0, key_dot, key_exp,
                key_equal, key_delete, key_delete_all, addition_key, soustraction_key,
                multiplication_key, division_key, parenthese_left, parenthese_right, copy_btn, square_root
            ]

for widget in button_list:
    widget.config(  font=Font, width=4, relief="flat", border=2, borderwidth=0, highlightthickness=0,
                    background="#646770", activebackground="#343740", foreground="White", activeforeground="White"
                )

others_list=[parenthese_left, parenthese_right, square_root, copy_btn]

for widget in others_list:
    widget.config(width=2, relief="flat", bg="#292929", activebackground="#353535" )

key_equal.config(bg="#22a7ff", activebackground="#0061B3")

others_bar.rowconfigure(0, weight=1)
others_bar.columnconfigure(0, weight=2)
others_bar.columnconfigure(1, weight=2)
others_bar.columnconfigure(2, weight=2)
others_bar.columnconfigure(3, weight=1)

keys_frame.rowconfigure(1, weight=1)
keys_frame.rowconfigure(2, weight=1)
keys_frame.rowconfigure(3, weight=1)
keys_frame.rowconfigure(4, weight=1)
keys_frame.rowconfigure(5, weight=1)

keys_frame.columnconfigure(0, weight=1)
keys_frame.columnconfigure(1, weight=1)
keys_frame.columnconfigure(2, weight=1)
keys_frame.columnconfigure(3, weight=1)

others_bar.pack(padx=4, pady=4, expand=True, fill="both")
keys_frame.pack(expand=True, fill="both", padx=4, pady=4)

display_frame.pack(padx=4, pady=4, expand=True, fill="both", side='left')

# Historique
scroll_bar_y = Scrollbar(root, orient="vertical")
scroll_bar_y.pack(fill="y", side='right')
scroll_bar_x = Scrollbar(root, orient="horizontal")
scroll_bar_x.pack(fill="x", side="bottom")

liste = ["Aucun historique."]
histo_var = StringVar()
histo_var.set(liste)

empty_histo = BooleanVar()
empty_histo.set(True)
historique = Listbox(   root, font=("Roboto", 20), bg="#202020", foreground="White", borderwidth=0,
                        highlightthickness=0, justify='right', width=5, listvariable=histo_var, xscrollcommand=scroll_bar_x.set,
                        yscrollcommand=scroll_bar_y.set, activestyle='none', state="disabled", selectbackground="#202020"
                    )

historique.pack(padx=6, pady=6, expand=True, fill="both", side='right')

scroll_bar_y.config(command=historique.yview)
scroll_bar_x.config(command=historique.xview)

# Fenêtre de guide

message_win = Tk()
message_win.title("Guide d'utilisation")
message_win.iconbitmap(fr"{rel_path}\ressources\calculator.ico")
message_win.config(borderwidth=0, bg="#d8d8d8")
message_win.geometry("600x300")
message_win.minsize(600, 300)

tips = """  - Mettez le nombre dont vous voulez obtenir la racine carré entre\n
            parenthèses pour éviter des erreurs de calculs (ex. √(25) ou √(20+5) )\n
            - Vous pouvez utiliser votre clavier et votre souris.\n
            Autres raccourcis: \n
            Egual : 'Entrée'  |  Effacer : 'Backspace'  |  Effacer tout : 'Del'\n
            Exposant : 'e'  |  Racine carré : 's'  |  Copier : 'Control+C'
        """

guide_frame = Frame(message_win, bg='#d8d8d8')

text = Label(guide_frame, font=('Roboto', 12, 'bold'), text=tips, bg='#d8d8d8')
text.pack()

validate = Button(guide_frame, font=('Roboto', 10), text="Fermer", bg='#c0c0c0', relief="groove", command=message_win.destroy)
validate.pack()
validate.focus()

guide_frame.pack(expand=1, pady=10)
message_win.mainloop()

root.mainloop()