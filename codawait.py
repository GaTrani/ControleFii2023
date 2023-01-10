import asyncio, sqlite3,BD
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

        link2 = 'https://fiis.com.br/'

        errosvariados = 0
        erroTimeOut = 0 #len(tickers)
        for i in range(0, len(tickers)):
            print('*******************************************')
            print('Ativo:', tickers[i])
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
                    print(tickers[i], dados[0], dados[1], dados[3], dados[4], dados[7])
                    for l in range(0, linhas):                    
                        BD.inserirat(tickers[i], dados[cont + 0], dados[cont + 1], dados[cont + 3], dados[cont + 4], dados[cont + 7])
                        database.commit()
                        cont += 7
                print('Contem', linhas, 'dados/linhas')
            except TimeoutError:
                erroTimeOut+=1
            except Exception as e:
                    errosvariados+= 1
                    # Handle the exception and continue the loop
                    print(f"Element not found: {e}")
                    continue
            linhas = 0 

            #page.locator("https://fiis.com.br/URPR11", waitUntil=["load"])
    await browser.close()

asyncio.run(main())