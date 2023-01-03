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
    
    #CAGR (Compound Annual Growth Rate ou taxa de crescimento anual composta), indica a taxa de crescimento anual de dividendos em dinheiro por cota nos últimos 3 anos
    dicio = {'Ticker': '', 
            'Preco': '', 
            'Gestao': '', 
            'DY': '', 
            'P/VP': '', 
            'Valor Patr Cota': '', 
            'Liq. Media Diaria': '', 
            'Percentual caixa': '', 
            'DY CAGR': '',
            'Valor CAGR': '',
            'Num cotistas': '',
            'Num cotas': '',
            'Patrimonio': '',
            'Ultimo Rendimento': ''}
    listaGeral = []
    j = 0
    i = 0
    for i in range(0, qtdAtivos):
        print(i, qtdAtivos, j)
        ativo = dados[j].replace('\narrow_forward\n', '')
        ticker = ativo[-6::]
        dicio['Ticker']             = ticker
        dicio['Preco']              = dados[j+1]
        dicio['Gestao']             = dados[j+2]
        dicio['DY']                 = dados[j+3]
        dicio['P/VP']               = dados[j+4]
        dicio['Valor Patr Cota']    = dados[j+5]
        dicio['Liq. Media Diaria']  = dados[j+6]
        dicio['Percentual caixa']   = dados[j+7]
        dicio['DY CAGR']            = dados[j+8]
        dicio['Valor CAGR']         = dados[j+9]
        dicio['Num cotistas']       = dados[j+10]
        dicio['Num cotas']          = dados[j+11]
        dicio['Patrimonio']         = dados[j+12]
        texto = dados[j+13]    

        #if para coletar o ultimo ativo por conta de nao conter o '\n'
        if(i == qtdAtivos-1):              
            dicio['Ultimo Rendimento'] = texto 
        else:
            indice = dados[j+13].index('\n')
            dicio['Ultimo Rendimento']  = texto[:indice]

        listaGeral.append(dicio.copy())
        j = j + 13

    print('dicio: ', listaGeral)
    
