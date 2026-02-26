alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for l in range(len(alphabet)):
    alphabet.append(alphabet[l])

def cryptage(lettre,alphabet,cle):
    for i in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[i] == lettre:
            return str(alphabet[i+cle])
    return ' '

def decryptage(lettre, alphabet, cle): # les signe de ponctuation seront remplacer par des espaces
    for i in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[i] == lettre:
            return str(alphabet[i-cle])
    return ' '


message = input('Entrez votre message ') # message crypté ou message à crypter
cle=int(input('Entrez votre cle ')) # clé utilisée pour crypter le message ou celle à utiliser

choix = int(input("Tapez 1 pour chiffrer le message et 2 pour déchiffrer "))

messagefinal = ""

if choix == 1:
    for lettre in message:
        messagefinal += cryptage(lettre,alphabet,cle)
elif choix == 2:
    for lettre in message:
        messagefinal += decryptage(lettre,alphabet,cle)
else:
    print("Veuillez entrez une option valide")

print(messagefinal)