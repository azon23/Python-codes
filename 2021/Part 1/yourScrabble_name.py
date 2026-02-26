"""
A,E,I,L,N,O,R,S,T,U : 1 point
D,G,M : 2 points
B,C,P : 3 points
F,H,V : 4 points
J,Q : 8 points
K,W,X,Y,Z : 10 points
"""

def yourScrabble_name():
    scrabble_value = {
        "a" : 1,
        "b" : 3, 
        "c" : 3, 
        "d" : 2, 
        "e" : 1,
        "é" : 1, 
        "è" : 1, 
        "ê" : 1, 
        "f" : 4, 
        "g" : 2, 
        "h" : 4, 
        "i" : 1, 
        "j" : 8, 
        "k" : 10, 
        "l" : 1, 
        "m" : 2, 
        "n" : 1, 
        "ñ" : 1, 
        "o" : 1, 
        "p" : 3, 
        "q" : 8, 
        "r" : 1, 
        "s" : 1, 
        "t" : 1, 
        "u" : 1, 
        "v" : 4, 
        "w" : 10, 
        "x" : 10, 
        "y" : 10, 
        "z" : 10,
        " " : 0
        }

    print("\nVous vous êtes toujours demandé combien de\npoints vallait votre nom au SCRABBLE ?\nEt bien, vous êtes au BON endroit...\nEntrez votre nom ci-dessous pour le savoir :)")
    while True:
        user_name = str(input("\nVOTRE NOM: ")).lower()
        total_value = 0
        if user_name == "exit" or user_name == "quit":
            break
        else:
            for x in user_name:
                if x in scrabble_value:
                    letter_value = scrabble_value.get(x)
                    total_value += letter_value
                else:
                    continue
        print(f"\nValeur du nom : {total_value} points")
        print('\n------------------------------')
yourScrabble_name()
    