from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://fast.com/pt/")



# Define um tempo limite para a espera (10 segundos neste exemplo)
tempo = 120
wait = WebDriverWait(driver, tempo)

try:
    # Espera até que o elemento esteja presente na página
    time.sleep(60)

    print("Medição efetuada")

    # Extrai o texto do elemento "speed-value"
    velocidade = wait.until(EC.presence_of_element_located((By.ID, "speed-value"))).text

    
    # Copia o valor extraído para onde desejar
    print("Valor de speed-value:", velocidade)  # Por exemplo, imprime o valor na tela



except:
    # Se o elemento não for encontrado dentro do tempo limite, imprime uma mensagem de erro
    print("Elemento não encontrado ou tempo limite excedido.")

# # Pausa a execução do script até que você pressione Enter
# input("Pressione Enter para fechar o navegador...")

# Fecha o navegador
driver.quit()