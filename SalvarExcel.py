import sqlite3
import pandas as pd
import os

#CRIAR DATABASE
database = sqlite3.connect('TesteSalvar.db')
c = database.cursor()

def criarTabela():
    database.execute(''' CREATE TABLE IF NOT EXISTS BDFii(
                            ATIVO VARCHAR(7),
                            DATABA INT NOT NULL,
                            DATAPAGTO INT NOT NULL,
                            COTA FLOAT NOT NULL,
                            PERCENT FLOAT NOT NULL,
                            DIVIDENDO FLOAT NOT NULL) 
                            ''')
    # APRLICA AS ALTERAÇOES NA TABELA
    database.commit()

criarTabela()

# Define caminho da área de trabalho
#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
desktop = os.path.abspath("C:\\Users\\gabri\\OneDrive\\Área de Trabalho")

# Caminho do arquivo de saída
arquivo_saida = os.path.join(desktop, 'dadosBDFii2.xlsx')

# lê os dados da tabela 'tabela'
df = pd.read_sql_query("SELECT * from BDFii", database)

# salva os dados em um arquivo Excel
df.to_excel(arquivo_saida, index=False)

# fecha a conexão com o banco de dados
database.close()
