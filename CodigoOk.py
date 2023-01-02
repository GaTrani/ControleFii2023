from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    navegador = p.chromium.launch(headless=False) #removendo ou deixando TRUE nao aparecerá o navegador
    pagina = navegador.new_page()

    #codigo funcionando!!
    link = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'
    pagina.goto(link)
    pagina.get_by_role('Button', name='Buscar').click()
    pagina.locator('//*[@id="list-result"]/div/div[2]/div').click()   
    time.sleep(2)
    pagina.keyboard.press('ArrowDown')
    pagina.keyboard.press('ArrowDown')
    pagina.keyboard.press('Enter')
    time.sleep(2)
    dados = pagina.locator('//*[@id="list-result"]/div/div[1]/div[2]/div/table/tbody').inner_text().split('\t')

    qtdAtivos = round((len(dados)/13))
    tickers = []
    dicionario = {}
    print(dados)
    print(qtdAtivos)
    j = 0
    for i in range(0, qtdAtivos):
        print(dados[j])
        ativo = dados[j].replace('\narrow_forward\n', '')
        tickers.append(ativo[-4::])
        j = j + 13

    print('tickers', tickers)

    print(tickers)
