from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#def instaLogin():
try:
    print("\n\nPOUR DES RAISONS DE SECURITE,\nVOUS NE DISPOSEZ QUE D'1 HEURE\nDE CONNEXION. A LA FIN DU DELAI,\nLE PROGRAMME S'ARRETERA AUTOMATIQUE.\n")
    sleep(5)
    driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.instagram.com/direct/inbox")

    # ajout de mon cookie de login sur le site
    driver.add_cookie(
        {
            "name": "sessionid",
            "value": "15610714487%3ALOOhsD727xSB0F%3A22%3AAYfhWDBQBdgbakA5L3o8acte6W8MDx-zfMi4t-oImYU",
            "domain": ".instagram.com",
            "path": "/",
            "secure": True
        })


    driver.refresh()    # la page se recharge pour appliquer le cookie

    # refus d'activer les notifications (pop-up)
    notifAlert = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    sleep(2)
    notifAlert.click()

    sleep(3600)

    driver.quit()
    print("\nFIN DU DELAI ACCORDE")
except Exception:
    print("\n\t\t***\nErreur pendant l'opération.\nAssurer-vous d'être connecté à Internet et de disposer de la dernière version de webdriver !\n\t\t***".upper())

# capture d'écran
#driver.save_screenshot("C:\\Users\\HP\\Images")


# driver.quit()

#instaLogin()