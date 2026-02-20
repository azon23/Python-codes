from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from time import sleep
 

# Scrapping de tous les liens de la page
def scrape(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser').find_all('a')
    
    links = []
    for link in soup:
        links.append(link.get('href'))

    return links


website = str(input("Entrez l'url du site web : "))
index_dict = {}
index = 0
for char in website:
    index_dict[char] = index
    index += 1

baseUrl = website[:int(index_dict["/"]+1)]
print("\nBase d'url :", baseUrl)


all_links = []
for links in scrape(website):
    l = str(links)
    if not(l.startswith("/") or l.startswith("http")) and (l.endswith(".asp") or l.endswith(".php")):
        all_links.append(baseUrl+links)
            

print("Il y a", len(all_links), "pages à télécharger\n")


# Téléchargement des pages
downloaded = 0
try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\HP\\Documents\\Files\\scripts\\Test ressources\\chromedriver.exe')
    driver.get("https://webtopdf.com/")
    driver.maximize_window()

    for url in all_links:
        print(url)

        driver.find_element(By.ID, "textUrl").send_keys(url)
        driver.find_element(By.ID, "btnConvert").click()
        driver.implicitly_wait(120)
        driver.find_element(By.CLASS_NAME, "downfile_over").click()
        driver.find_element(By.ID, "divStartover").click()
        
        downloaded += 1
        sleep(2)
    
    print(downloaded, "fichiers téléchargés")

except Exception as e:
    print(e)
    print(downloaded, "fichiers téléchargés")

