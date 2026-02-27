from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

abs_path = os.path.abspath(__file__)
rel_path = os.path.dirname(abs_path)

print("\n\nPOUR DES RAISONS DE SECURITE,\nVOUS NE DISPOSEZ QUE D'1 HEURE\nDE CONNEXION. A LA FIN DU DELAI,\nLE PROGRAMME S'ARRETERA AUTOMATIQUE.\n")
sleep(5)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/direct/inbox")

# ajout de mon cookie de login sur le site
driver.add_cookie(
    {
        "name": "sessionid",
        "value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
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

# capture d'écran
#driver.save_screenshot("C:\\Users\\HP\\Images")


