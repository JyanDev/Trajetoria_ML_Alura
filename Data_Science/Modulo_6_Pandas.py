"""
Neste módulo iniciei meus estudos em Pandas junto com Numpy

"""
import pandas as pd

# Carregando dados de um csv e testando funções básicas de visualização de tabelas
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'


dados = pd.read_csv(url)
print(f"""--- Visualizando 7 primeiras linhas ---\n {dados.head(7)}
          --- Visuallizando últimas 5 linhas ---\n {dados.tail(5)}
          --- Visualizando total de tabelas e linhas ---\n {dados.shape}
          --- Visualizando as colunas ---\n {dados.columns}
          --- Visualizando uma coluna ---\n {dados["Nome"]}
          --- Visualizando mais de uma coluna ---\n {dados[["Idade","Notas"]]}
          --- Visualizando o tipo de dados das colunas ---\n {dados.dtypes}
          --- Visualizando um resumo da tabela ---\n {dados.describe}""")
