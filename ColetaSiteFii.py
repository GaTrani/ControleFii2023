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
    #print(dados)    
    dados = dados.split()
    #print('dados split', dados)
    qtd = int(len(dados)/9)
    #print('qtd: ', qtd)
    j = 0
    tickers = []
    for i in range(0, qtd):
        tickers.append(dados[j])
        j+=9
    
    #print(tickers)
    
    link2 = 'https://fiis.com.br/'
    errosvariados = 0
    erroTimeOut = 0
    for i in range(0, len(tickers)):
        link2 = 'https://fiis.com.br/' + tickers[i]
        pagina.goto(link2)
        print('Ativo:', tickers[i])

        try:
            dividendos = pagina.locator('//*[@id="carbon_fields_fiis_dividends-2"]/div[2]/div[2]/div/div/div/div/div[2]').inner_text()
            #print(dividendos)
        except TimeoutError:
            erroTimeOut+=1
        except:
            errosvariados+= 1
            print('erro try.')
        print('errosVariados', errosvariados)
        print('errosTimeOut', erroTimeOut)