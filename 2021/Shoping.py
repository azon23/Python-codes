solde = 3000

prix = {
    "banane" : 150,
    "poire" : 45,
    "sacoche" : 200
    }

print("\nArticles disponibles:")
for keys in prix.keys():
    print("- ", keys.capitalize())

while True:
    choice = str(input("\nQue voulez vous acheter ? ")).lower()
    item_price = prix.get(choice)

    if choice in prix.keys():
        print(f"L'article {choice.capitalize()} coûte {item_price}€.")
        print("Solde :", solde)
        
        askforbuy = str(input("\nVoulez-vous acheter cet article ?(Y/N) ")).lower()

        if askforbuy == "y":
            print("Achat effectué avec succès.\nL'article vous sera livré dans un délai de 7 jours.")
            solde -= item_price
            print(f"Votre solde après achat est de {solde}€.\nA BIENTÔT !")
        else:
            print(f"Article non acheté.\nVotre solde actuel est de {solde}€.\nA BIENTÔT !")
    else:
        print("Larticle demandé n'est pas disponible.")




