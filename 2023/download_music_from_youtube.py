import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

urls = []
print("\nCe programme prends en entrée des urls vers des vidéos Youtube et en sortie, il retourne un fichier .mp3 de ces vidéos dans le dossier de téléchargement par défaut.\nPour commencer entrez les urls une par une puis tapez 'ok', 'quit' ou 'exit' pour valider.")
while True:
    user_input = str(input("\nEntrez une url Youtube : "))

    if user_input == "ok" or user_input == "exit" or user_input == "quit":
        break
    else:
        urls.append(user_input)

# Configurez le dossier de téléchargement
download_directory = r"C:\Users\HP\Downloads"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory
})

try:
    for i in range(0, len(urls)):

        # variable qui declenche le driver et ouvrir la page web
        driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Documents\Files\scripts\Test ressources\chromedriver.exe', options=chrome_options)
        driver.get(r"https://notube.io/fr/youtube-app-v102")
        # driver.maximize_window()
        
        driver.implicitly_wait(120)
        time.sleep(5)
        
        # recup et remplir la case input
        url_input = driver.find_element(By.ID, "keyword")
        url_input.send_keys(urls[0])
        
        # recup et cliquer sur le boutton "redemarrer"
        submit_btn = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
        submit_btn.click()
        
        driver.implicitly_wait(120)
        time.sleep(5)
        
        copyright_msg = driver.find_element(By.XPATH, '//*[@id="breadcrumbs-section"]/div/p').text
        print("\n\n\n", copyright_msg, "\n\n\n")
        if "Cette vidéo est protégée par des droits d'auteur" in copyright_msg:
            urls.pop(0)
            driver.quit()
        else:
            title = driver.find_element(By.XPATH, '//*[@id="blocLinkDownload"]/h2').text

            driver.implicitly_wait(120)
            time.sleep(1)

            # recup et cliquer sur le boutton "redemarrer"
            download_btn = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
            download_btn.click()

            # Attendez que le fichier soit téléchargé
            def wait_for_download(filename):
                while True:
                    if filename in os.listdir(download_directory):
                        return True
                    time.sleep(1)

            # Attendez le téléchargement
            file_name_to_wait_for = (title + ".mp3").replace("|", "")
            print(file_name_to_wait_for)
            if wait_for_download(file_name_to_wait_for):
                print("Le téléchargement est terminé.")
            else:
                print("Le téléchargement a expiré ou a échoué.")

            # Fermez le driver
            driver.quit()

    urls.pop(0)

    print("\nOPERATION ACCOMPLIE AVEC SUCCES")

except Exception:
    print("\n\t\t***\nErreur pendant l'opération.\nAssurer-vous d'être connecté à Internet et de disposer de la dernière version de webdriver !\n\t\t***".upper())
    print("\n\t\t***\nNous allons relancer l'opération.\n\t\t***".upper())

    for i in range(0, len(urls)):

        # variable qui declenche le driver et ouvrir la page web
        driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Documents\Files\scripts\Test ressources\chromedriver.exe', options=chrome_options)
        driver.get(r"https://notube.io/fr/youtube-app-v102")
        # driver.maximize_window()
        
        driver.implicitly_wait(120)
        time.sleep(5)
        
        # recup et remplir la case input
        url_input = driver.find_element(By.ID, "keyword")
        url_input.send_keys(urls[0])
        
        # recup et cliquer sur le boutton "redemarrer"
        submit_btn = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
        submit_btn.click()
        
        driver.implicitly_wait(120)
        time.sleep(5)
        
        copyright_msg = driver.find_element(By.XPATH, '//*[@id="breadcrumbs-section"]/div/p').text
        print("\n\n\n", copyright_msg, "\n\n\n")
        if "Cette vidéo est protégée par des droits d'auteur" in copyright_msg:
            urls.pop(0)
            driver.quit()
        else:
            title = driver.find_element(By.XPATH, '//*[@id="blocLinkDownload"]/h2').text

            driver.implicitly_wait(120)
            time.sleep(1)

            # recup et cliquer sur le boutton "redemarrer"
            download_btn = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
            download_btn.click()

            # Attendez que le fichier soit téléchargé
            def wait_for_download(filename):
                while True:
                    if filename in os.listdir(download_directory):
                        return True
                    time.sleep(1)

            # Attendez le téléchargement
            file_name_to_wait_for = (title + ".mp3").replace("|", "")
            print(file_name_to_wait_for)
            if wait_for_download(file_name_to_wait_for):
                print("Le téléchargement est terminé.")
            else:
                print("Le téléchargement a expiré ou a échoué.")

            # Fermez le driver
            driver.quit()

    urls.pop(0)
    
    print("\nOPERATION ACCOMPLIE AVEC SUCCES")