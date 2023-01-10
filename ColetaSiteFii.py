from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import sqlite3, BD, os
import pandas as pd

#CRIAR DATABASE
database = sqlite3.connect('BancoDadosFii2023.db')
c = database.cursor()

BD.criarTabela()

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
    erroTimeOut = 0 #len(tickers)
    for i in range(0, 5):
        print('Ativo:', tickers[i])
        link2 = 'https://fiis.com.br/' + tickers[i]
        pagina.goto(link2)
        dados = []
        linhas = 0
        cont = 0
        try:
            print('*******************************************')
            dados = pagina.locator('//*[@id="carbon_fields_fiis_dividends-2"]/div[2]/div[2]/div/div/div/div/div[2]').inner_text()
            
            if(len(dados) > 0):
                dados = dados.split()
                linhas = int(len(dados) / 7)            
                print(tickers[i], dados[0], dados[1], dados[3], dados[4], dados[7])
                for l in range(0, linhas):                    
                    BD.inserirat(tickers[l], dados[cont + 0], dados[cont + 1], dados[cont + 3], dados[cont + 4], dados[cont + 7])
                    database.commit()
                    cont += 7
            print('linha', linhas)            
                  
        except TimeoutError:
            erroTimeOut+=1
        except:
            errosvariados+= 1
            print('-------------------erro try.')
        linhas = 0 
        print('errosVariados', errosvariados)
        print('errosTimeOut', erroTimeOut)


desktop = os.path.abspath("C:\\Users\\gabri\\OneDrive\\Área de Trabalho")

# Caminho do arquivo de saída
arquivo_saida = os.path.join(desktop, 'dadosBDFii2.xlsx')

# lê os dados da tabela 'tabela'
df = pd.read_sql_query("SELECT * from BDFii", database)

# salva os dados em um arquivo Excel
df.to_excel(arquivo_saida, index=False)

# fecha a conexão com o banco de dados
database.close()



