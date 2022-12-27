from playwright.sync_api import sync_playwright
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    navegador = p.chromium.launch(headless=False) #removendo ou deixando TRUE nao aparecerá o navegador
    pagina = navegador.new_page()
    i = 'URPR11'
    #link = 'https://fiis.com.br/' + i + '/'
    link = 'https://statusinvest.com.br/fundos-imobiliarios/afhi11'
    '''pagina.goto(link)
    print('Acessando:', link)
    
    indicador1 = pagina.locator('//*[@id="main-2"]/div[2]/div[1]').text_content().split()
    indicador2 = pagina.locator('//*[@id="main-2"]/div[2]/div[5]/div').text_content().split()
    ultimoRendimento = pagina.locator('//*[@id="dy-info"]').text_content().split()
    #tabela dividendos
    dividendos = pagina.locator('//*[@id="earning-section"]/div[7]/div/div[2]/table').text_content()

    cnpj_tipo = pagina.locator('//*[@id="fund-section"]/div/div/div[2]/div').text_content().split()
    segmento = pagina.locator('//*[@id="fund-section"]/div/div/div[4]/div').text_content().split()'''
    
    #evolucao preco
    link2 = 'https://br.investing.com/equities/af-invest-cri-fii-historical-data'
    pagina.goto(link2)
    print('Acessando:', link2)
    #alterar para mensal
    pagina.locator('#history-timeframe-selector').click()
    pagina.keyboard.press('ArrowUp')
    pagina.keyboard.press('Enter')    
    historicoPreco = pagina.locator('//*[@id="__next"]/div/div/div/div[2]/main/div/div[8]/div/div/div[3]/div/table/tbody').text_content()

    
    print('-----', historicoPreco)
    #print(len(historicoPreco))

    #pagina.close()
    browser.close()