def Memoring():
    # 30 premières décimals de Pi :
    pi = "3 . 1 4 1 5 9 2 6 5 3 5  8 9 7 9 3 2 3  8 4 6 2 6 4 3 3  8 3 2 7 9".replace(" ", "")
    alphabet = "zyxwvutsrqponmlkjihgfedcba"


    def learn_pi():
        while True:
            userInput = input("\n=> ")
            if userInput == "exit" or userInput == "quit":
                break
            else:
                if userInput in pi:
                    print(f"Correct !!!\nVous avez trouvé {len(userInput) - 2}/30 décimales de Pi")
                else:
                    print("Incorrect ! Essayez encore...\n")

    def learn_alphabet():
        while True:
            userInput = input("\n=> ")
            if userInput == "exit" or userInput == "quit":
                break
            else:
                if userInput in alphabet:
                    print(f"Correct !!!\nVous avez trouvé {len(userInput)}/26 lettres")
                else:
                    print("Incorrect ! Essayez encore...\n")

    # présentation

    while True:
        print("\nQue voulez-vous réviser ?\n1- Les 30 premières décimales de Pi\n2- L'alphabet à l'envers")
        print('\n--------------------------------------------')
        choice = input("\nVotre choix: ")
        if choice == "1":
            learn_pi()
        elif choice == "2":
            learn_alphabet()
        elif choice == "exit" or choice == "quit":
            break
        else:
            print("\nNon pris en charge. Entrez un numéro correct !")
            print("\n--------------------------------------------")
            continue



""" 
Phrase mnémotechnique :
3.14 15; neuf vins suisse; 5 35; 89 sceptre neufs très détruit; oui car si deux suisses grattent 3 truites; 3 des 7 nains 
3.14 15   9    2      6    5 35  89   7       9    3    2  3     8   4  6   2      6       4     3  3 8     3  2  7   9
 """