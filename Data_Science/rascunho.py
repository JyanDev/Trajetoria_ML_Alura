import matplotlib.pyplot as plt
import numpy as np
url = "https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv"
dados_csv = np.loadtxt( url, delimiter=",", usecols= np.arange(1,6,1), skiprows=1)

# Exemplo: Vendas por Fruta
frutas_filtradas = dados_csv[(dados_csv[:,0] >= 7.0) & (dados_csv[:,0] <= 7.5)]
print(frutas_filtradas[:,1])
