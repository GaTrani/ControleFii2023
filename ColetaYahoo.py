import yfinance as yf
import datetime

# Defina o ticker do fundo imobiliário e o período para o qual deseja baixar os dados
ticker = 'ABCP11.SA'
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)

# Baixe os dados do fundo imobiliário
fundo = yf.download(ticker, start=start, end=end)

# Colete os dados de dividendos
dividends = fundo["Dividends"]

#Imprima os dados de dividendos
print(dividends)




