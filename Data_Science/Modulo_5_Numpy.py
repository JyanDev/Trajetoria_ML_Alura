#Nessa etapa, você deve efetuar a leitura dos dados. Para isso, importe a NumPy e use a função loadtxt. Use o link da url e o parâmetro usecols para pular a primeira coluna. É possível usar np.arange para criar a sequência de números que representam as colunas. Por fim, também é necessário incluir o parâmetro skiprows=1 para que a primeira linha de texto seja desconsiderada na leitura do arquivo.


import numpy as np

url = "https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv"
dados_csv = np.loadtxt( url, delimiter=",", usecols=np.arange(1,6,1), skiprows=1 )
