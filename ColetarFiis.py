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
    link = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'    
    pagina.goto(link)
    pagina.get_by_role('Button', name='Buscar').click()
    print(pagina.locator('//*[@id="list-result"]/div/div[1]/div[2]/div/table/tbody').text_content())

    for row in pagina.get_by_role('list-result').all():
        print(row.text_content())

    #//*[@id="list-result"]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/a/div/span
    #//*[@id="list-result"]/div/div[1]/div[2]/div/table/tbody/tr[61]/td[1]/a/div/span