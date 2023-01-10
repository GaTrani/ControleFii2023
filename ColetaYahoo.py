import yfinance as yf

# Defina o ticker do fundo imobiliário e o período para o qual deseja baixar os dados
ticker = 'ABCP11.SA'
start = "2019-01-01"
end = "2020-01-01"

# Baixe os dados de preços de fechamento do fundo imobiliário
fundo = yf.download(ticker, start=start, end=end)

#Imprima o dataframe
print(fundo)




