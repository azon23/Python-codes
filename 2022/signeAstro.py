from datetime import datetime

# Source: https://icalendrier.fr/signes-astrologiques
"""
Verseau : 21 janvier - 19 février       21 - 50
Poissons : 20 février - 20 mars         51 - 80
Bélier : 21 mars - 20 avril             81 - 111
Taureau : 21 avril - 21 mai             112 - 142
Gémeaux : 22 mai - 21 juin              143 - 173
Cancer : 22 juin - 22 juillet           174 - 204
Lion : 23 juillet - 22 août             205 - 235
Vierge : 23 août - 22 septembre         236 - 266
Balance : 23 septembre - 22 octobre     267 - 296
Scorpion : 23 octobre - 22 novembre     297 - 327
Sagittaire : 23 novembre - 21 décembre  328 - 356
Capricorne : 22 décembre - 20 janvier   357 - 386 (20 * 366)
"""
 
def signe_astro():
    try:
        # Calcule le rang de la date de naissance dans l'année
        def daycalculator(a, b, c):
            if a == 1:
                pos = b
            elif a == 2:                # a représente le mois et b représente le jour de naissance
                pos = b + 31            # c représente le nombre de jours du mois de février (année bixextile ou non)
            elif a == 3:                # pos représente le rang de la date de naissance
                pos = b + 31 + c        # ex. si a = 2(mois) et b = 4(jours) alors pos = 35e jours de l'année
            elif a == 4:
                pos = b + 31 + c + 31
            elif a == 5:
                pos = b + 31 + c + 31 + 30
            elif a == 6:
                pos = b + 31 + c + 31 + 30 + 31
            elif a == 7:
                pos = b + 31 + c + 31 + 30 + 31 + 30
            elif a == 8:
                pos = b + 31 + c + 31 + 30 + 31 + 30 + 31
            elif a == 9:
                pos = b + 31 + c + 31 + 30 + 31 + 30 + 31 + 31
            elif a == 10:
                pos = b + 31 + c + 31 + 30 + 31 + 30 + 31 + 31 + 30
            elif a == 11:
                pos = b + 31 + c + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            elif a == 12:
                pos = b + 31 + c + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
            
            return pos

        # Instructions
        print("\nVous devez renseigner votre jour, votre mois\net votre année de naissance.\nLe programme retournera votre signe\nastrologique et d'autres infos en plus.\n\n")
        userDay = int(input("Jour de naissance (entre 01 et 31): "))
        userMonth = int(input("Mois de naissance (entre 01 et 12): "))
        userYear = int(input("Année de naissance (entre .... et 2022): "))

        # Donne la date de naissance avec le mois en lettres
        monthList = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        mois = monthList[userMonth - 1]
        print(f"\nDate de naissance: {userDay} {mois} {userYear}")

        # Détermine si l'année est bissextile ou non (366 ou 365 jours)
        def bissex(a):
            if a%4 == 0:
                bissextile = 29
            else:
                bissextile = 28

            return bissextile

        # Nombres de jours du mois de février en fonction de l'année mis en entrée
        bissexBirthyear = bissex(userYear)
        bissexActualyear = bissex(datetime.now().year)

        # Affiche le rang de la date de naissance dans l'année de naissance (ex. 25e jours de l'année 2022)
        dayPosition = daycalculator(userMonth, userDay, bissexBirthyear)
        if dayPosition == 1:
            print(f"Vous êtes né(e) le {dayPosition}er jour de l'année {userYear}")
        else:
            print(f"Vous êtes né(e) le {dayPosition}e jours de l'année {userYear}")

        # Calcul et affiche l'age (si aujourd'hui, à venir ou passé)
        age = datetime.now().year - userYear
        if datetime.now().month == userMonth and datetime.now().day == userDay:
            print(f"Aujourd'hui, vous avez {age} ans. Félicitation!!!\u2764")
        elif daycalculator(datetime.now().month, datetime.now().day, bissexActualyear) < daycalculator(userMonth, userDay, bissexBirthyear):
            print(f"Vous allez avoir avoir {age} ans cette année")
        else:
            print(f"Vous avez eu {age} ans cette année")

        # Ajoute 365 ou 366 jours si date < 21 janvier (Pour Capricorne)
        if dayPosition < 21 and bissexBirthyear == 28:
            dayPosition += 365
        elif dayPosition < 21 and bissexBirthyear == 29:
            dayPosition += 366

        # Calcul et retourne le signe astrologique
        def astro(a):
            if bissexBirthyear == 28:
                if 20 < a < 51:
                    return "Verseau\u2652"
                elif 50 <= a <= 80:
                    return "Poisson\u2653"
                elif 81 <= a <= 111:
                    return "Bélier\u2648"
                elif 112 <= a <= 142:
                    return "Taureau\u2649"
                elif 143 <= a <= 173:
                    return "Gémeaux\u264a"
                elif 174 <= a <= 204:
                    return "Cancer\u264b"
                elif 205 <= a <= 235:
                    return "Lion\u264c"
                elif 236 <= a <= 266:
                    return "Vierge\u264d"
                elif 267 <= a <= 296:
                    return "Balance\u264e"
                elif 297 <= a <= 327:
                    return "Scorpion\u264f"
                elif 328 <= a <= 356:
                    return "Sagittaire\u2650"
                elif 357 <= a <= 386:
                    return "Capricorne\u2651"
            elif bissexBirthyear == 29:
                if 20 <= a <= 51:
                    return "Verseau\u2652"
                elif 50 <= a <= 81:
                    return "Poisson\u2653"
                elif 82 <= a <= 112:
                    return "Bélier\u2648"
                elif 113 <= a <= 143:
                    return "Taureau\u2649"
                elif 144 <= a <= 174:
                    return "Gémeaux\u264a"
                elif 175 <= a <= 205:
                    return "Cancer\u264b"
                elif 206 <= a <= 236:
                    return "Lion\u264c"
                elif 237 <= a <= 267:
                    return "Vierge\u264d"
                elif 268 <= a <= 297:
                    return "Balance\u264e"
                elif 298 <= a <= 328:
                    return "Scorpion\u264f"
                elif 329 <= a <= 357:
                    return "Sagittaire\u2650"
                elif 358 <= a <= 387:
                    return "Capricorne\u2651"

        # Affiche le signe astrologique
        signe = astro(dayPosition)
        print(f"Votre signe astrologique: {signe}")
    except Exception:
        print("\n\t\t***\nErreur de calcul\nChiffres uniquement autorisé...\n\t\t***".upper())


signe_astro()