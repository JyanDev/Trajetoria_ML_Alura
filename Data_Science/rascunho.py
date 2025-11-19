url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'
import numpy as np
dado= np.loadtxt(url, delimiter=',',skiprows=1,dtype=float)
dado.shape