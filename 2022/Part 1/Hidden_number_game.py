from string import ascii_letters, digits
from random import randint
import time
import sys

separator = '\n--------------------------------------------'

def hidden_number_game():
    # fonction d'affichage du meilleur score
    def showHighscore():
        attemps_list = []   # stockage du nombre de tentatives pour chaque partie
        index_dict = {} # dictionnaire pour faire correspondre chaque ligne de records.txt avec l'index de cette ligne
        chars = ascii_letters + digits    # ensemble des lettres (majuscules et minuscules) et des chiffres

        with open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\records.txt", "r") as file:
            content = file.readlines()  # récupère et stocke chaque ligne du fichier dans la variable "content" sous forme de liste
            for element in chars:
                for line in content:    # pour chaque line du fichier
                    if line.startswith(element):    # si la ligne commence par une lettre minuscule, majuscule ou un chiffre
                        index_dict[line] = content.index(line)  # ajoute au dictionnaire "index_dict", le contenu de la ligne comme clé et l'index de la ligne comme valeur
                        arrow_index = line.index(">")   # Cherche le signe ">" sur la ligne et stocke son index dans la variable "arrow_index"
                        a = line[arrow_index + 2]   # "a" stocke le nombre de tentatives soit le 2e élément après le signe '>'
                        if line[arrow_index + 3].isdigit(): # Vérifie si le caractère qui suit "a" est un chiffre ou pas
                            attemps_list.append(str(int(a) * 10 + int(line[arrow_index + 3])))  # si oui on ajoute les deux chiffres à la liste "attemps_list" en tant qu'un seul nombre (ex. 1 et 7 => 17)
                        else:
                            attemps_list.append(a)  # sinon on ajoute que "a" dans la liste
                    else:   # sinon on ignore la ligne
                        continue

            attemps_list.sort() # ordonne la liste de sorte que le nombre (de tentatives) se trouve au début de la liste
            
            for x in index_dict:    # pour chaque clé (correspond aux lignes du fichier) dans "index_dict" 
                equal_index = x.index("=")  # Cherche le signe "=" sur la ligne(x) et stocke son index dans la variable "equal_index
                first_digit = x[equal_index + 3]
                if x[equal_index + 4].isdigit():
                    attemp_number = str(int(first_digit) * 10 + int(x[equal_index + 4]))
                else:
                    attemp_number = first_digit
                # affichage du meilleur score
                if attemps_list[0] == attemp_number:
                    highscore_index = index_dict[x]
                    print(content[highscore_index])

            file.close()

    def hiddenNumberGame():
        # Génération du nombre mystère et affichage des instructions
        nombreMystere = randint(0, 10000)
        username = input('Veuillez entrez votre nom: ')
        attemps = 0 # nombre de tentatives
        nowdate = time.strftime('%d/%m/%Y %H:%M') # date et heure actuelle
        print("\nBienvenue dans le HIDDEN NUMBER Game...")
        print("\nVous devez trouver le nombre mystère choisi par l'algo.\nLe nombre se situe entre 0 et 10 000.\nPour jouer, entrez une intervalle de recherche.\nLe bot va scanner les nombres situés dans cette intervalle et vous dira si le nombre mystère s'y trouve.\nSi vous pensez avoir touver le nombre mystère, tapez le chiffre 0 comme première et deuxième intervalle.\nCela vous fera sortir de la boucle pour que vous proposez votre réponse.\n")
        
        # Début du jeu
        while True:
            try:
                d = int(input("\nEntrez le 1er nombre de l'intervalle:  "))
                f = int(input("Entrez le 2e nombre de l'intervalle:  "))

                if d == 0 and f == 0:   # si les deux intervales sont égales à 0, demande au joueur de proposer sa réponse...
                    answer = int(input("Quel est le nombre mystère?  "))
                    if answer == nombreMystere:
                        print(f"\nFélicitation!!! Vous avez trouvé le nombre mystère en {attemps} essaies.")
                        # enregistre le scrore dans un fichier txt
                        with open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\records.txt", 'r+') as record:
                            content = record.read()
                            record.seek(0)
                            record.write(f"{username}\t=>\t{attemps} tentatives\t=>\t{nowdate}\n\n" + content)
                            record.close()
                        print(separator)    
                        commands()
                    else:
                        print("\nCe n'est le nombre mystère. Cherchez encore !")
                        attemps += 1    # ajoute 1 au nombre de tentatives
                        continue
                else:   # ...sinon lance un scan dans l'intervalle donnée et dis si cette dernière contient le nombre mystère
                    print("Début du scan...")
                    time.sleep(1)
                    for i in range(d, f+1):
                        print(i)

                    if nombreMystere in range(d, f+1):
                        print("Let's go! Le chiffre mystère se situe dans cette intervalle.\n")
                    else:
                        print("Oups! L'intervalle ne contient pas le chiffre mystère.\n")

                    attemps += 1 # ajoute 1 au nombre de tentatives
            except Exception:
                print("\n** Erreur pendant l'opération. Veuillez re-saisir les deux intervales ! **".upper())
                continue

    # demande au player quel action il veut fait(rejouer, afficher lemeilleur scroce ou les dernières parties)
    def commands():
        while True:
            print("\nTapez l'une des commandes ci-dessous:\n'P' => Jouer\n'H' => Donner le meilleur scrore\n'L' => Afficher les 5 dernières parties\n'A' => Afficher toutes les parties gagnées\n")
            choice = input("=> ").lower()

            if choice == 'p': # lance une nouvelle partie
                print("-------------------------------------------")
                hiddenNumberGame()
            elif choice == 'h': # affiche le meilleur scrore
                print("-------------------------------------------")
                print("Le record actuel est détenu par:\n")
                showHighscore()
                print(separator)
                commands()
            elif choice == 'l': # affiche les 5 dernières parties
                print("-------------------------------------------")
                print("Voici les 5 dernières parties gagnées:\n")
                with open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\records.txt", 'r') as record:
                    for x in record:
                        if x.startswith("\n"):
                            pass
                        else:
                            print(x)
                    time.sleep(1)
                    record.close()
                print(separator)
                commands()
            elif choice == 'a': # affiche toutes les parties gagnées
                print("-------------------------------------------")
                print("Voici la liste de toutes les parties gagnées:\n")
                myList = []
                with open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\records.txt", 'r') as record:
                    for x in record:
                        myList.append(x)
                    
                    for y in myList:
                        if y == "\n":
                            myList.remove("\n")
                        else:
                            pass

                    print(myList)
                    print("\n".join(myList[:6]))
                    record.close()
                print(separator)
                commands()
            elif choice == "exit" or choice == "quit": # pour quitter la boucle ou le jeu en général
                break
            else: # redemande de faire un choix si autre chose a été tapé
                print("\nVeuillez entrer une option valide.")
                print(separator)
                commands()


    commands()

hidden_number_game()