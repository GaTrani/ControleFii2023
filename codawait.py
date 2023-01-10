import asyncio, sqlite3,BD, os
import pandas as pd
from playwright.async_api import async_playwright

#CRIAR DATABASE
database = sqlite3.connect('BancoDadosFii2023.db')
c = database.cursor()
BD.criarTabela()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        pagina = await browser.new_page()
        link = 'https://fiis.com.br/resumo/'
        await pagina.goto(link)
        dados = await pagina.locator('//*[@id="upTo--default-fiis-table"]/div/table/tbody').inner_text()          
        dados = dados.split()
        qtd = int(len(dados)/9)
        print('Total de ativos a coletar dados: ', qtd)

        j = 0
        tickers = []
        print('NA?', dados[2])
        for i in range(0, qtd):    
            if(dados[j+2] != 'N/A'):        
                tickers.append(dados[j])
                j+=9

        print(len(tickers))
        link2 = 'https://fiis.com.br/'

        ativosComErro = []
        errosvariados = 0
        erroTimeOut = 0
        for i in range(0, len(tickers)):
            print('****************')
            print('Ativo:', i, tickers[i])
            link2 = 'https://fiis.com.br/' + tickers[i]
            try:
                await pagina.goto(link2, wait_until='load')                
                dados = []
                linhas = 0
                cont = 0
                dados = await pagina.locator('//*[@id="carbon_fields_fiis_dividends-2"]/div[2]/div[2]/div/div/div/div/div[2]').inner_text()
                if(len(dados) > 0):
                    dados = dados.split()
                    linhas = int(len(dados) / 7)                    
                    for l in range(0, linhas):                    
                        BD.inserirat(tickers[i], dados[cont + 0], dados[cont + 1], dados[cont + 3], dados[cont + 4], dados[cont + 7])
                        database.commit()
                        cont += 7
                else:
                    ativosComErro.append(tickers[i])
                
            except TimeoutError:
                erroTimeOut+=1                
            except Exception as e:
                errosvariados+= 1
                # Handle the exception and continue the loop
                #print(f"Element not found: {e}")
                continue
            linhas = 0 

    print('erros:', errosvariados, erroTimeOut)
    print('Ativos com erros:', ativosComErro)

    print('Convertendo BD em Excel...')
    desktop = os.path.abspath("C:\\Users\\gabri\\OneDrive\\Área de Trabalho")
    # Caminho do arquivo de saída
    arquivo_saida = os.path.join(desktop, 'dadosBDFii2.xlsx')
    # lê os dados da tabela 'tabela'
    df = pd.read_sql_query("SELECT * from BDFii", database)
    # salva os dados em um arquivo Excel
    df.to_excel(arquivo_saida, index=False)
    # fecha a conexão com o banco de dados
    print('BANCO CONVERTIDO COM SUCESSO.')
    database.close()

    await browser.close()
asyncio.run(main())