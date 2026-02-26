import os
from time import sleep
from tkinter import *
from random import choice

abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)
bg_color = '#0c4d97'
font = ('Roboto', 20)

sign = "X"
player_1 = ""
player_2 = ""
player = player_1
############## PLAYING WINDOW ##################################################
def game_window():
    def mark_a1():
        sign = globals()['sign']
        a1.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if a1 in combi:
                                clicked_case_index = combi.index(a1)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == a1['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == a1['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        



        
    def mark_a2():
        sign = globals()['sign']
        a2.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if a2 in combi:
                                clicked_case_index = combi.index(a2)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == a2['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == a2['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_a3():
        sign = globals()['sign']
        a3.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if a3 in combi:
                                clicked_case_index = combi.index(a3)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == a3['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == a3['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_b1():
        sign = globals()['sign']
        b1.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if b1 in combi:
                                clicked_case_index = combi.index(b1)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == b1['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == b1['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_b2():
        sign = globals()['sign']
        b2.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if b2 in combi:
                                clicked_case_index = combi.index(b2)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == b2['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == b2['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_b3():
        sign = globals()['sign']
        b3.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if b3 in combi:
                                clicked_case_index = combi.index(b3)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == b3['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == b3['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_c1():
        sign = globals()['sign']
        c1.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if c1 in combi:
                                clicked_case_index = combi.index(c1)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == c1['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == c1['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_c2():
        sign = globals()['sign']
        c2.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if c2 in combi:
                                clicked_case_index = combi.index(c2)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == c2['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == c2['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        



    def mark_c3():
        sign = globals()['sign']
        c3.config(text=sign, state='disabled')
        playable = False
        for place in cases:
            if place['text'] == "":
                playable = True
                break

        if sign == 'X':
            globals()['sign'] = 'O'
            globals()['player'] = globals()['player_2']
            check_winner()
                    
            if playable == True:
                if globals()['player_2'] == "L'ordinateur":
                    played = False

                    # Attaque
                    for combi in winning_combi:
                        case1, case2, case3 = combi
                        if case1['text'] == "O" and case1['text'] == case2['text'] and case3['text'] == "":
                            case3.invoke()
                            played = True
                            break
                        elif case1['text'] == "O" and case1['text'] == case3['text'] and case2['text'] == "":
                            case2.invoke()
                            played = True
                            break
                        elif case2['text'] == "O" and case2['text'] == case3['text'] and case1['text'] == "":
                            case1.invoke()
                            played = True
                            break


                    # Défense
                    if played == False:
                        for combi in winning_combi:
                            if c3 in combi:
                                clicked_case_index = combi.index(c3)
                                combi.pop(clicked_case_index)
                                case1, case2 = combi
                                if case1['text'] == c3['text'] and case2['text'] == "":
                                    case2.invoke()
                                    played = True
                                elif case2['text'] == c3['text'] and case1['text'] == "":
                                    case1.invoke()
                                    played = True
                                else:
                                    pass
                                    
                                combi.insert(clicked_case_index, a1)
                                if played == True:
                                    break
                
                    if played == False:
                        while True:
                            case = choice(cases)
                            if case['text'] == "":
                                case.invoke()
                                break
            else:
                check_winner()
                if "gagné" not in display['text']:
                    display['text'] = "Match nul !"
        else:
            globals()['sign'] = 'X'
            globals()['player'] = globals()['player_1']
            check_winner()
            if playable == False and "gagné" not in display['text']:
                display['text'] = "Match nul !"
        
        


    def check_winner():
        def combi():
            empty=''
            if a1['text']!=empty and a2['text']!=empty and a3['text']!=empty and a1['text']==a2['text']==a3['text']:
                return a1, a2, a3
            elif b1['text']!=empty and b2['text']!=empty and b3['text']!=empty and b1['text']==b2['text']==b3['text']:
                return b1, b2, b3
            elif c1['text']!=empty and c2['text']!=empty and c3['text']!=empty and c1['text']==c2['text']==c3['text']:
                return c1, c2, c3
            elif a1['text']!=empty and b1['text']!=empty and c1['text']!=empty and a1['text']==b1['text']==c1['text']:
                return a1, b1, c1
            elif a2['text']!=empty and b2['text']!=empty and c2['text']!=empty and a2['text']==b2['text']==c2['text']:
                return a2, b2, c2
            elif a3['text']!=empty and b3['text']!=empty and c3['text']!=empty and a3['text']==b3['text']==c3['text']:
                return a3, b3, c3
            elif a1['text']!=empty and b2['text']!=empty and c3['text']!=empty and a1['text']==b2['text']==c3['text']:
                return a1, b2, c3
            elif a3['text']!=empty and b2['text']!=empty and c1['text']!=empty and a3['text']==b2['text']==c1['text']:
                return a3, b2, c1
        
        if display['text'] != "Match nul !":
            if globals()['sign'] == "X" and globals()['player_1'] == "Vous":
                display['text'] = ""
            else:
                display['text'] = f"{globals()['player']} joue... ({globals()['sign']})"
        
        if combi() != None:
            for case in combi():
                # vars_dict = globals()
                case.config(background='Red')
                if globals()['player'] == globals()['player_1']:
                    display['text'] = f"{globals()['player_2']} a gagné !"
                else:
                    if globals()['player_1'] == "Vous":
                        display['text'] = f"Vous avez gagné !"
                    else:
                        display['text'] = f"{globals()['player_1']} a gagné !"
            
            for case in cases:
                case.config(state=DISABLED)

        # display.after(200, check_winner)

    #########################################################
    # config
    root = Tk()
    root.title('Tic Tac Toe with master AI')
    #root.iconbitmap(fr'{rel_path}')
    root.state('zoomed')
    #root.minsize(weight, height)
    root.config(background=bg_color)

    ############## FRAME #####################################""
    frame = Frame(root, bg=bg_color)
    font = ('Roboto', 70, 'bold')

    a1 = Button(frame, command=mark_a1)
    a1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
    a2 = Button(frame, command=mark_a2)
    a2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
    a3 = Button(frame, command=mark_a3)
    a3.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

    b1 = Button(frame, command=mark_b1)
    b1.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
    b2 = Button(frame, command=mark_b2)
    b2.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
    b3 = Button(frame, command=mark_b3)
    b3.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

    c1 = Button(frame, command=mark_c1)
    c1.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
    c2 = Button(frame, command=mark_c2)
    c2.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
    c3 = Button(frame, command=mark_c3)
    c3.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

    winning_combi = [
            [a1, a2, a3],
            [b1, b2, b3],
            [c1, c2, c3],
            [a1, b1, c1],
            [a2, b2, c2],
            [a3, b3, c3],
            [a1, b2, c3],
            [c1, b2, a3]
        ]

    frame.pack(expand=YES, anchor='nw', fill='both')

    cases = [ a1, a2, a3, b1, b2, b3, c1, c2, c3 ]
    for case in cases:
        case.config(text='', font=font, bg="#7da0ff", fg='White', width=7, height=1, borderwidth=0,
                    disabledforeground=('White'))

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    ############## DISPLAY ##############################################################################

    def replay():
        if globals()['player_1'] == "Vous" and globals()['player_2'] == "L'ordinateur":
            globals()['sign'] = "X"
            globals()['player'] = globals()['player_1']
        root.destroy()
        game_window()

    
    def new():
        root.destroy()
        globals()['sign'] = "X"
        globals()['player_1'] = ""
        globals()['player_2'] = ""
        globals()['player'] = player_1
        select_mode()
        
    
    lower_frame = Frame(root, bg=bg_color)

    newParty = Button(lower_frame, text='Nouvelle partie', font=('Roboto', 30, 'bold'), bg='#042447', borderwidth=0, fg='White', width=12, command=new)
    newParty.grid(column=0, row=0, sticky='w', padx=5)

    display = Label(lower_frame, text='', font=('Roboto', 40, 'bold'), bg=bg_color, fg='White')
    display.grid(column=1, row=0, sticky='nsew', padx=5)

    replay_btn = Button(lower_frame, text='Rejouer', font=('Roboto', 30, 'bold'), bg='#042447', borderwidth=0, fg='White', width=12, command=replay)
    replay_btn.grid(column=2, row=0, sticky='e', padx=5, )
    
    lower_frame.pack(pady=10, expand=YES, anchor='nw', fill='both')

    lower_frame.columnconfigure(0, weight=1)
    lower_frame.columnconfigure(1, weight=5)
    lower_frame.columnconfigure(2, weight=1)

    ########################################################################################
    check_winner()
    root.mainloop()

############## ASKING WINDOW ###############################################################
def ask_for_players_name():
    def validate(event=None):
        globals()['player_1'] = player1_input.get()
        globals()['player_2'] = player2_input.get()
        globals()['player'] = player1_input.get()
        win.destroy()
        game_window()

    # config
    win = Tk()
    win.title('Who are playing ?')
    #root.iconbitmap(fr'{rel_path}')
    win.geometry('450x200')
    #root.minsize(weight, height)
    win.config(background=bg_color)
    win.bind('<Return>', validate)

    main_frame = Frame(win, bg=bg_color)
    player1_frame = Frame(main_frame, bg=bg_color)
    player2_frame = Frame(main_frame, bg=bg_color)

    player1_label = Label(player1_frame, text='Joueur 1 :', font=font, bg=bg_color, fg='White')
    player1_label.pack(expand=YES, side='left')
    player1_input = Entry(player1_frame, font=font)
    player1_input.pack(expand=YES, side='right', padx=5)

    player2_label = Label(player2_frame, text='Joueur 2 :', font=font, bg=bg_color, fg='White')
    player2_label.pack(expand=YES, side='left')
    player2_input = Entry(player2_frame, font=font)
    player2_input.pack(expand=YES, side='right', padx=5)

    validate_btn = Button(main_frame, text='Jouer', font=font, bg="#042447", borderwidth=0, fg='White', width=10, command=validate)
    validate_btn.pack(side='bottom')

    player1_frame.pack(pady=5)
    player2_frame.pack(pady=5)
    main_frame.pack(expand=YES)
    win.mainloop()

def select_mode():
    def ia_mode(event=None):
        globals()['player_1'] = "Vous"
        globals()['player_2'] = "L'ordinateur"
        globals()['player'] = "Vous"
        win.destroy()
        game_window()
    
    def player_mode(event=None):
        win.destroy()
        ask_for_players_name()

    # config
    win = Tk()
    win.title('Who are playing ?')
    #root.iconbitmap(fr'{rel_path}')
    win.geometry('450x200')
    #root.minsize(weight, height)
    win.config(background=bg_color)
    win.bind('1', ia_mode)
    win.bind('2', player_mode)

    main_frame = Frame(win, bg=bg_color)
    buttons_frame = Frame(main_frame, bg=bg_color)

    title = Label(main_frame, text='Sélectionnez le mode :', font=font, bg=bg_color, fg='White')
    title.pack(expand=YES, side='top')

    ai_mode_btn = Button(buttons_frame, text='Contre IA', font=font, bg="#042447", borderwidth=0, fg='White', width=10, command=ia_mode)
    ai_mode_btn.pack(side='left', padx=5)

    player_mode_btn = Button(buttons_frame, text='1vs1', font=font, bg="#042447", borderwidth=0, fg='White', width=10, command=player_mode)
    player_mode_btn.pack(side='right', padx=5)

    buttons_frame.pack(pady=10)
    main_frame.pack(expand=YES)
    win.mainloop()

select_mode()