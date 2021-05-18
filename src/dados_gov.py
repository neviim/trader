from typing import DefaultDict
import pandas as pd
import requests
import zipfile
import io

# Pegando dados publicos para analizes
r = requests.get('http://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv')

# Passando para datafreme
linha = [i.strip().split(';') for i in r.text.split('\n')]
df = pd.DataFrame(linha[1:], columns=linha[0])
# print(df)

# Pegar um arquivo .csv direto do site dentro de um arquivo .zip
link = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2021.zip'
arquivo = 'dfp_cia_aberta_BPA_con_2021.csv'

r  = requests.get(link)
zf = zipfile.ZipFile(io.BytesIO(r.content))
zf = zf.open(arquivo)
linhas = zf.readlines()
linhas = [i.strip().decode('ISO-8859-1') for i in linhas ]
linhas = [i.split(';')for i in linhas]
df = pd.DataFrame(linhas[1:], columns=linhas[0])
# print(df)