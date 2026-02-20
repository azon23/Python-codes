import os
from tkinter import *
from pyperclip import copy

def switch():
    if binary_display.cget('state') == 'disabled':
        left_frame.grid(row=0, column=1, sticky='w')
        right_frame.grid(row=0, column=0, sticky='w')
        binary_display.config(state='normal')
        decimal_display.config(state='disabled')
    elif binary_display.cget('state') == 'normal':
        left_frame.grid(row=0, column=0, sticky='w')
        right_frame.grid(row=0, column=1, sticky='w')
        binary_display.config(state='disabled')
        decimal_display.config(state='normal')

def to_binary(decimal):
    bits = 32
    binary = ''
    for n in range(bits-1, -1, -1):
        if decimal // 2**n == 1:
            binary += '1'
            decimal -= 2**n
        else:
            binary += '0'

    binary_display.delete('1.0', 'end-1c')
    binary_display.insert('1.0', int(binary))

def to_decimal(binary):
    binary_len = len(str(binary))
    reversed_binary = str(binary)[::-1]
    decimal = 0
    for n in range(binary_len-1, -1, -1):
        decimal += int(reversed_binary[n])*2**n

    decimal_display.delete('1.0', 'end-1c')
    decimal_display.insert('1.0', int(decimal))

def convert():
    if binary_display.cget('state') == 'disabled':
        number = decimal_display.get("1.0", 'end-1c')
        binary_display.config(state='normal')
        to_binary(int(number))
        binary_display.config(state='disabled')
    elif decimal_display.cget('state') == 'disabled':
        number = binary_display.get("1.0", 'end-1c')
        decimal_display.config(state='normal')
        to_decimal(int(number))
        decimal_display.config(state='disabled')

def copy_content():
    if binary_display.cget('state') == 'disabled':
        binary_display.config(state='normal')
        copy(binary_display.get("1.0", 'end-1c'))
        binary_display.config(state='disabled')
    elif decimal_display.cget('state') == 'disabled':
        decimal_display.config(state='normal')
        copy(decimal_display.get("1.0", 'end-1c'))
        decimal_display.config(state='disabled')

#########################################################
abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)
bg_color = '#251b3c'

# config
root = Tk()
root.title('Convertisseur binaire')
#root.iconbitmap(fr"{rel_path}\pyramid.ico")
root.state('zoomed')
root.minsize(707, 450)
root.config(background=bg_color)

############## TITLE ##############################################################################

win_title = Label(root, text='Convertisseur binaire', font=('Roboto', 50, 'bold'), bg=bg_color, fg='White')
win_title.pack()

############## MIDDLE FRAME ##########################################################################
main_frame = Frame(root, bg=bg_color)
input_frame = Frame(main_frame, bg=bg_color)
left_frame = Frame(input_frame, bg=bg_color)
right_frame = Frame(input_frame, bg=bg_color)


left_label = Label(left_frame, text='Décimal', font=('Roboto', 25, 'bold'), bg=bg_color, fg='White')
left_label.pack(anchor='w', padx=10)
decimal_display = Text(left_frame, font=('Roboto', 30), width=35, border=5, relief='flat', height=5)
decimal_display.pack(fill='both', expand=YES, padx=10)

right_label = Label(right_frame, text='Binaire', font=('Roboto', 25, 'bold'), bg=bg_color, fg='White')
right_label.pack(expand=YES, anchor='w', padx=10)
binary_display = Text(right_frame, font=('Roboto', 30), width=35, border=5, relief='flat', state='disabled', height=5)
binary_display.pack(fill='both', expand=YES, padx=10)

left_frame.grid(row=0, column=0)
right_frame.grid(row=0, column=1)

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
input_frame.pack()

############## LOWER FRAME ###############################################################

btn_frame = Frame(main_frame, bg=bg_color)

switch_btn = Button(btn_frame, text='Changer', font=('Roboto', 30), bg="#084550", fg="White", width=15, command=switch)
switch_btn.grid(row=0, column=1, padx=5, sticky='nsew')#pack(expand=True, side='left', padx=5)
copy_btn = Button(btn_frame, text='Copier', font=('Roboto', 30), bg="#084550", fg="White", width=15, command=copy_content)
copy_btn.grid(row=0, column=2, padx=5, sticky='nsew')#pack(expand=True, side='right', padx=5)
convert_btn = Button(btn_frame, text='Convertir', font=('Roboto', 30), bg="#084550", fg="White", width=15, command=convert)
convert_btn.grid(row=0, column=3, padx=5, sticky='nsew')#pack(expand=True, side='right', padx=5)

btn_frame.rowconfigure(0, weight=1)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)
btn_frame.columnconfigure(4, weight=1)

btn_frame.pack(expand=True, pady=10)
main_frame.pack(expand=YES)
root.mainloop()