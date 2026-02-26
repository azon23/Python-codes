from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def routeur():
    try:
        '''
        Redémarre le routeur wifi sur un réseau personnel
        '''
        # variable qui declenche le driver et ouvrir la page web
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://192.168.1.1")

        # recup et remplir la case pwd
        pwd_case = driver.find_element(By.NAME, "http_passwd")
        pwd_case.send_keys("admin")

        # recup et cliquer sur le boutton "connexion"
        connect_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/form/table/tbody/tr/td[2]/a')
        connect_btn.click()

        # recup et cliquer sur le boutton "redemarrer"
        restart_btn = driver.find_element(By.NAME, "btn_reboot")
        restart_btn.click()

        # valider sur la boite de dialogue
        alert = driver.switch_to.alert
        alert.accept()

        sleep(10)

        driver.quit()   # sys.exit() pour fermer le terminal

        print("\nOPERATION ACCOMPLIE AVEC SUCCES")
        
    except Exception:
        print("\n\t\t***\nErreur pendant l'opération.\nAssurer-vous d'être connecté à Internet et de disposer de la dernière version de webdriver !\n\t\t***".upper())

routeur()