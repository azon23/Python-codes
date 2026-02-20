""" 
OUVRE D'ABORD LA FENETRE DANS LAQUELLE TU VEUX ECRICRE.
FAIS GAFFE SINON LE PROGRAMME VA ECRIRE N'IMPORTE OU.
SI CA SE PASSE MAL, AMENE LA SOURIS DANS LE COIN SUPERIEUR GAUCHE (FAIL SAFE SYSTEM).
CELA VA SUSPENDRE L'EXECUTION DU SCRIPT.
"""
import pyautogui as pg
from time import sleep

pg.FAILSAFE = True  #FAILSAFE => suspend l'execution du programme si la souris part dans le coin supérieur gauche

# Retardateur d'exécution du scrript
wait_time = 10
print(f"Début de la saisie dans {wait_time}")
for i in range(wait_time, 0, -1): #(start, stop, step) => step négatif pour un décompte(compte à reculons)
    print(i)
    sleep(1)

# Saisie automatique
# with open(r"C:\Users\HP\Documents\Files\scripts\Test ressources\nom_famille_FR.txt") as file:
#     pg.write("Voici quelques noms de familles français :")
#     pg.press("Enter")

#     for name in file:   # Boucles de saisie
#         pg.write(name, interval=0)
#         pg.press("Enter")
        
#     pg.write("C'est tout pour l'instant. Bonne soirée !")
#     pg.press("Enter")

pg.moveTo(119, 304)  # move mouse to XY coordinates over num_second seconds
pg.click(x=25, y=160, clicks=1, button='left')

# Alerte de fin dans la console
print("Fin de la saisie.")


"""

Documentation:
https://pyautogui.readthedocs.io/en/latest/quickstart.html

"""
