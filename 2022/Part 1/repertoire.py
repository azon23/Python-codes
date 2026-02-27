from string import whitespace
from pyperclip import copy

repertoire = [
    "Jean Dupont 060102XXXX",
    "Marie Lefevre 061122XXXX",
    "Lucas Martin 062233XXXX",
    "Emma Bernard 063344XXXX",
    "Noah Petit 064455XXXX",
    "Lina Moreau 065566XXXX"
]


def add():
    newContact = input("=>")
    while True:
        if newContact.lower() in repertoire:
            add()
        elif newContact.lower() == "exit" or newContact.lower() == "quit":
            
            break
        else:
            repertoire.append(newContact.lower())
            add()

def search():
    userInput = str(input("Contact à rechercher: ")).lower()
    for element in repertoire:
        if userInput in element:
            print(f"\n***  {element}  ***\n")
            print('\n---------------------------')

def show():
    repertoire.sort()
    notlist = str(repertoire).replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").title()
    print(" " + notlist + "\n\n*La liste a été copié")
    print('\n---------------------------')
    copy(notlist.replace(",", ",\n").lower())


while True:    
    print("\nChoisissez une option:\n1 : Ajouter un contact\n2 : Rechercher un contact\n3 : Afficher les contacts\n\nTapez 1 ou 2 pour valider\n")
    userChoice = input("Votre choix: ")
    if userChoice == "1":
        print('\n-------------------------------')
        add()
    elif userChoice == "2":
        print('\n-------------------------------')
        search()
    elif userChoice == "3":
        print('\n-------------------------------')
        show()
    elif userChoice == "exit" or userChoice == "quit":
        break
    else:
        print(userChoice, " n'est pas une option. Veuillez rééssayer...\n")
        print('\n-------------------------------')
        continue