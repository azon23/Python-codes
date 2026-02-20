from rich.console import Console
import os

rouge = '\033[91m' # rouge

print("\nDEBUT DE LA PARTIE !!!\n")

def Tableau():
    tableau = f"""
          |     |
       {a1}  |  {a2}  |  {a3}
          |     |
     -----------------
          |     |
       {b1}  |  {b2}  |  {b3}
          |     |
     -----------------
          |     |
       {c1}  |  {c2}  |  {c3}
          |     |
        """
    return tableau

def check_winner():
    empty=' '
    Tableau
    if a1!=empty and a2!=empty and a3!=empty and a1==a2==a3:
        return "a1", "a2", "a3"
    elif b1!=empty and b2!=empty and b3!=empty and b1==b2==b3:
        return "b1", "b2", "b3"
    elif c1!=empty and c2!=empty and c3!=empty and c1==c2==c3:
        return "c1", "c2", "c3"
    elif a1!=empty and b1!=empty and c1!=empty and a1==b1==c1:
        return "a1", "b1", "c1"
    elif a2!=empty and b2!=empty and c2!=empty and a2==b2==c2:
        return "a2", "b2", "c2"
    elif a3!=empty and b3!=empty and c3!=empty and a3==b3==c3:
        return "a3", "b3", "c3"
    elif a1!=empty and b2!=empty and c3!=empty and a1==b2==c3:
        return "a1", "b2", "c3"
    elif a3!=empty and b2!=empty and c1!=empty and a3==b2==c1:
        return "a3", "b2", "c1"


a1,b1,c1,a2,b2,c2,a3,b3,c3 = " "*9
a1_style = "white"
Console().print(Tableau())
print()

try:
    player_1 = input("Entrez le nom du joueur 1 : ")
except Exception():
    player_1 = input("Entrez le nom du joueur 1 : ")
try:
    player_2 = input("Entrez le nom du joueur 2 : ")
except Exception():
    player_2 = input("Entrez le nom du joueur 2 : ")
tour = 1
while tour<10:
    print("Tour", f"#{tour}")
    if tour%2 != 0:
        joueur = player_1
        mark = "X"
    else:
        joueur = player_2
        mark = "O"

    print(f"A {joueur} de jouer... ({mark})")
    player_entry = input("Quelle case voulez-vous marquer ? ")

    os.system('cls')

    if player_entry == "a1":
        if a1 == " ":
            a1 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "b1":
        if b1 == " ":
            b1 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "c1":
        if c1 == " ":
            c1 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1

    elif player_entry == "a2":
        if a2 == " ":
            a2 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "b2":
        if b2 == " ":
            b2 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "c2":
        if c2 == " ":
            c2 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1

    elif player_entry == "a3":
        if a3 == " ":
            a3 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "b3":
        if b3 == " ":
            b3 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    elif player_entry == "c3":
        if c3 == " ":
            c3 = mark
        else:
            print("Cette case est déjà occupée ! :triangular_flag:")
            tour -= 1
    else:
        Console().print(joueur, ', veuillez entrez de vraies coordonnées ! :angry:')
        tour -= 1
    
    Console().print(Tableau())

    if check_winner() != None:
        for case in check_winner():
            vars_dict = globals()
            vars_dict[case] = "[red]"+vars_dict.get(case)+"[/red]"

        print('\n--------------------------------------------'*2)

        Console().print(Tableau())
        print("Fin du jeu.")
        Console().print(joueur, "remporte la partie !!!", ':trophy:', style="bold") # python -m rich.emoji : Emoji list
        
        break


    tour += 1