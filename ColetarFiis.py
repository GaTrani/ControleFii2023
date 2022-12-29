from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    navegador = p.chromium.launch(headless=False) #removendo ou deixando TRUE nao aparecerá o navegador
    pagina = navegador.new_page()
    '''link = 'https://www.clubefii.com.br/fundo_imobiliario_lista'
    pagina.goto(link)

    listaAtivos = []
    for i in range(1,500):
        linha = '//*[@id="fundos_listados"]/div[3]/table/tbody/tr[' + str(i) + ']/td[1]/a' 
        listaAtivos.append(pagina.locator(linha).text_content())
        
    print(listaAtivos)'''
    
   
    '''link = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'
    pagina.goto(link)
    qtd = pagina.locator('//*[@id="bucafiis"]/form/label/span').text_content().split()
    qtd = int(qtd[0])'''


    link = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'
    pagina.goto(link)
    pagina.get_by_role('Button', name='Buscar').click()
    pagina.locator('//*[@id="list-result"]/div/div[2]/div/input').click()    
    

    pagina.select_option('select-wrapper', 'TODOS').click()
    #pagina.keyboard.press('ArrowUp')
    #pagina.keyboard.press('ArrowUp')
    pagina.keyboard.press('Enter')   
    time.sleep(5)
    print(qtd)
    listaAtivos = []
'''
    for i in range(1, qtd):
        linha = '//*[@id="list-result"]/div/div[1]/div[2]/div/table/tbody/tr[' + str(i) + ']/td[1]/a/div/span'
        listaAtivos.append(pagina.locator(linha).text_content())
        print(listaAtivos)
'''