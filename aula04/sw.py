# pip install selenium
# pip install pandas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Configurar navegador (modo headless opcional)
options = Options()
# options.add_argument('--headless')  # Sem interface gráfica
driver = webdriver.Chrome(options=options)

# Buscar produto na KaBuM
produto = "bicicleta"
url = f"https://www.kabum.com.br/busca/{produto.replace(' ', '-')}"
driver.get(url)
time.sleep(3)

# Coletar dados
produtos = driver.find_elements(By.CLASS_NAME, "productCard")

dados = []
for prod in produtos[:20]:  # Limitar a 20
    try:
        nome = prod.find_element(By.CLASS_NAME, "nameCard").text
        preco = prod.find_element(By.CLASS_NAME, "priceCard").text
        
        dados.append({
            'produto': nome,
            'preco': preco
        })
    except:
        continue

# Exportar
df = pd.DataFrame(dados)
df.to_csv('precos_kabum.csv', index=False)
print(f"Coletados {len(dados)} produtos!")

driver.quit()