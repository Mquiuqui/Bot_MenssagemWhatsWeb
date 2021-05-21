from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
i = 0
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
time.sleep(2)

contatos = ['Testes']
mensagem = 'emoji'
def buscar_contato(contato):
    campo_pesquisa = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')  
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')  
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    while i<10:
        enviar_mensagem(mensagem)
        i = i+1
