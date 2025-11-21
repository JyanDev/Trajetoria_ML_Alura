"""
Na alura não continha muitos exercícios para praticar, então usei Gemini para criar exercícios de práticas do nível básico ao difícil.

"""

import numpy as np
import matplotlib.pyplot as plt

# --- DADOS DE TREINAMENTO (1-6) ---

# [ID_Aluno, Nota_Trabalho, Nota_Prova]
dados_alunos = np.array([
    [101, 75, 88],  # Aluno 1
    [102, 92, 95],  # Aluno 2
    [103, 60, 72],  # Aluno 3
    [104, 85, 90],  # Aluno 4
    [105, 55, 68],  # Aluno 5
    [106, 99, 100], # Aluno 6
    [107, 78, np.nan], # Aluno com erro
    [108, 81, 85]   # Aluno 8
])


#   Nível 	Objetivo do Exercício

#1	Básico	Seleção Simples: Imprima a nota da Prova (Coluna 2) do Aluno de ID 104.

print(f"AT1: {dados_alunos[3,2]}")

#2	Básico	Slicing (Fatiamento): Imprima as Notas de Trabalho (Coluna 1) dos Alunos 3 ao 6 (incluindo o 6).
print(f"AT2: {dados_alunos[2:6, 1]}")

#3	Básico	Slicing (Todas as Colunas): Imprima todos os dados (ID, Trabalho, Prova) dos Alunos 5, 6 e 7.
print(f"AT3: {dados_alunos[4:7, :]}")

#4	Interm.	Máscara Booleana (Comparações): Selecione e Imprima apenas as linhas (dados completos) dos alunos que tiraram Nota de Trabalho maior que 80.
print(f"AT4: {dados_alunos[dados_alunos[:, 1] > 80]}")

#5	Interm.	Verificação de NaNs: Descubra quantos alunos têm pelo menos um NaN na linha de notas. (Dica: use np.isnan e np.sum no eixo correto).
print(f"AT5: Total de alunos com notas faltando = {np.sum(np.any(np.isnan(dados_alunos), axis=1))}. Id do aluno: {dados_alunos[np.any(np.isnan(dados_alunos),axis=1), 0]}")


#6	Interm.	Máscara Dupla (Complexidade): Selecione os alunos que tiraram Nota de Trabalho maior ou igual a 85 E Nota de Prova maior que 90. (Dica: use & entre as máscaras).
print(f"AT6: {dados_alunos[(dados_alunos[:, 1] >= 85) & (dados_alunos[:, 2] > 90)]}")


#--- Complexidade aumentada ---
url = "https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv"
dados_csv = np.loadtxt( url, delimiter=",", usecols= np.arange(1,6,1), skiprows=1)


#   Nível 	Objetivo do Exercício

#7	Avançado	Plotagem Básica: Crie um gráfico de dispersão (plt.scatter) simples. Plote a Coluna 0 (Diâmetro) no Eixo X e a Coluna 1 (Peso) no Eixo Y.
plt.scatter(dados_csv[:,0],dados_csv[:,1])
#plt.show()

#8	Avançado	Plotagem Profissional: Repita o exercício 7. Adicione título e rótulos para os Eixos X (Diâmetro) e Y (Peso).
plt.scatter(dados_csv[:,0], dados_csv[:,1])
plt.title("Variação de peso das frutas cítricas ao diâmetro")
plt.xlabel("Diâmetro")
plt.ylabel("Peso")
#plt.show()




#9	Avançado	Seleção no Mundo Real: Conte quantas frutas têm Diâmetro (Coluna 0) maior que 6.5 e Peso (Coluna 1) menor que 280.
total_frutas = np.sum((dados_csv[:,0] >6.5) & (dados_csv[:,1] < 280))
print(f"AT9: {total_frutas} ")

#10	 Chefão 	Análise Completa: 1. Crie uma máscara booleana que filtre apenas as frutas com Diâmetro (Coluna 0) entre 7.0 e 7.5. 2. Plote um gráfico de barras (plt.bar ou plt.hist) que exiba a distribuição de Peso (Coluna 1) APENAS para as frutas filtradas.

frutas_filtradas = dados_csv[(dados_csv[:,0] >= 7.0) & (dados_csv[:,0] <= 7.5)]

#Exemplo com plt.bar
#Impossível sem uma categoria predefinada com strings para plotar no gráfico.

#Exemplo com plt.hist

plt.close()
plt.hist(frutas_filtradas[:,1], bins= "auto")
plt.title("Distribuição de Peso de frutas com diâmetros de 7.0 a 7.5")
plt.xlabel("Peso")
plt.ylabel("Frequência")
#plt.show()