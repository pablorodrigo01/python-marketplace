import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

USERNAME = os.getlogin()

# Caminho para o Chromedriver
selenium_service = Service("file\\chromedriver.exe")

# Opções do Chrome
options = Options()
options.add_experimental_option("detach", True)
# prefs = {"download.default_directory" : "file"}
# options.add_experimental_option("prefs", prefs)
options.add_argument(f"--user-data-dir=C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

# Criação do driver com o perfil no Google (Default: Profile 1)
driver = webdriver.Chrome(service=selenium_service, options=options)

# Acessa o site da Shopee
driver.get("https://seller.shopee.com.br/portal/tools/mass-update/download")

# Aguarda o carregamento do elemento passado por XPATH
load = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/span[2]/div/div/label/span[1]"))
    )
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/span[2]/div/div/label/span[1]").click()

# Driver procura elemento especificado via XPATH
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div/button[1]")
WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[4]/div/button[1]").click()

# Driver procura elemento especificado via XPATH
WebDriverWait(driver, 20)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div[3]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/button").click()