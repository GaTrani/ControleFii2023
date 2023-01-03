from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    navegador = p.chromium.launch(headless=False) #removendo ou deixando TRUE nao aparecerá o navegador
    pagina = navegador.new_page()

    link = 'https://fiis.com.br/resumo/'
    pagina.goto(link)
    dados = pagina.locator('//*[@id="upTo--default-fiis-table"]/div/table/tbody').inner_text()
    print(dados)