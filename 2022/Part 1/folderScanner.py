import os

def folder_scanner():
    while True:
        try:
            file_number = 0       # compteur = nombres de fichiers
            list = []
            systemfiles = ["Default.rdp", "desktop.ini"]     # fichiers-système à ne pas afficher après l'analyse
            path = str(input("\nChemin du dossier à analyser: ")).replace('"', '')

            if f"{path}" == "exit" or f"{path}" == "quit":
                break
            else:
                option = str(input("\nVoulez-vous effectuer une recherche ciblée (Y/N): "))
                if option == "exit" or option == "quit":
                    break
                elif option.lower() == "y":
                    fileformat = str(input("\nExtension/Type de fichiers: "))     # extension à préciser pour afficher les fichiers de ce type
                    for file in os.listdir(path):
                        if file.endswith(fileformat):
                            file_number += 1
                            list.append(file)
                    print(f"\n***  {file_number} fichiers '{fileformat}' trouvés  ***\n")
                    for element in list:
                        print(element)
                else:       # si rien n'est mis en option, fais une analyse globale et retourne tous les fichiers du dossier
                    for element in os.listdir(path):
                        if '.' in element:  # permet d'exclure les dossiers de la recherche(les noms dossiers n'ont pas de points car ils n'ont pas d'extension [ex: 3])
                            if element in systemfiles:   # si l'élément est dans la list des fichiers systèmes alors ne pas afficher (passer)
                                continue
                            else:   # sinon compter comme un fichier normal à afficher
                                file_number += 1
                                list.append(element)
                        else:
                            continue
                    print(f"\nIl y {file_number} fichiers dans le dossier '{path}'\n")
                    for file in list:
                        print(file)
        except Exception:
            print("\n\t\t***\nLe dossier indiqué n'existe pas.\nVeuillez vérifier le chemin saisi...\n\t\t***".upper())
            continue

folder_scanner()