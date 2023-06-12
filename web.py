from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

USERNAME = os.getlogin()

# Caminho para o Chromedriver
selenium_service = Service('file\\chromedriver.exe')

# Opções do Chrome
options = Options()
options.add_experimental_option("detach", True)
prefs = {"download.default_directory" : "file\\download"}
options.add_experimental_option("prefs", prefs)
options.add_argument(f"--user-data-dir=C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(service=selenium_service, options=options)

# Acessa o site do Mercado Livre 
driver.get("https://www.mercadolivre.com.br/anuncios/edicao-em-excel/download")

driver.implicitly_wait(10)

# Clica para expandir para maior opções
driver.find_element(By.XPATH, "/html/body/main/section/section/div[1]/div/div").click()

# Seleciona opção de SKU
driver.find_element(By.XPATH, "/html/body/main/section/section/div[1]/div/div[2]/div[2]/div[11]/label/span").click()

driver.implicitly_wait(10)

# Clica para expandir para maior opções
driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[1]").click()

# Seleciona a alteração de todos os produtos
driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div[2]/div[2]/div[2]/div[1]/label/span").click()

# Espera para evitar futuros problemas
driver.implicitly_wait(10)

# Procura e clica no botão Baixar
driver.find_element(By.XPATH, "/html/body/main/section/section/div[3]/button").click()

# Gera uma espera para que o arquivo seja gerado e efetuado seu download
driver.implicitly_wait(10)

# Após gerar a espera, clica no botão Enviar excel
driver.find_element(By.XPATH, "/html/body/main/section/section/div/div[3]/div/div/a[1]").click()

# Clica no input file e seleciona o arquivo para envio
driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div[1]/div/div/input").send_keys(os.getcwd()+"/download/teste.xlsx")

# Procura e clica no botão Enviar
driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div[2]/button").click()


driver.implicitly_wait(200) 
# Criaca nova aba no Google Chrome
driver.switch_to.new_window('tab')

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


driver.implicitly_wait(200) 
driver.switch_to.new_window('tab')

# Acessa o site da Magalu
driver.get("https://id-b2b.magazineluiza.com.br/auth/realms/B2B/protocol/openid-connect/auth?client_id=ipdv&redirect_uri=https%3A%2F%2Fparceiro.magalu.com%2Fbem-vindo&state=5f347442-7121-43b3-ac94-c0608805146a&response_mode=fragment&response_type=code&scope=openid&nonce=1f47a82f-e7df-412f-9518-cc2c316404fa")

driver.implicitly_wait(10)

# Efetua o login
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[1]/input").send_keys("email")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/form/div[2]/input").send_keys("senha")

# Procura e clica no botão de Login
driver.find_element(By.CSS_SELECTOR, "#kc-login")
driver.find_element(By.CSS_SELECTOR, "#kc-login").click()

# Clica para expandir a barra lateral
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/header/div/button[1]").click()

# Clica na seção de Produtos
driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/nav/div[6]/div[2]/span").click()

# Clica na opção Importação de Produtos
driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/nav/div[7]/div/div/div/div[1]/div").click()

# Clica na opção Selecionar todos
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div/label/span[1]/span[1]/input").click()

# Clica na opção de Ações massivas
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div/div/button").click()

# Clica na opção Exportar
# driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/p[3]").click()