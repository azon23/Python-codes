from string import whitespace
from pyperclip import copy

repertoire = [
'abdou 77969976',
 'abdoulaye coulibaly 82829966',
 'abdoulaye sow 72122103',
 'anika 83124256',
 'assetou 72927272',
 'barber 76978563',
 'barry 98512828',
 'ben 66747373',
 'diakité 77076060',
 'gnagna 76769300',
 'habib 90153293',
 'jeanne 89557966',
 'kondo 93539684',
 'krish 63414237',
 'magnol 90303400',
 'mahamadou cisse 94645700',
 'maman 83849835 / 99937926',
 'ousmane 93753685',
 'papa 79205938 / 69013739',
 'prince 82883705',
 'rokiatou 70629724',
 'sambou 75155034',
 'selima 94892870',
 'simone 91781609',
 'souad 91344370 / 60560376',
 'thioune 70703223',
 'zani 94314127'
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