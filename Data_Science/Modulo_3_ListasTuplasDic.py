"""
Exercícios do Módulo 3 da Formação de Data Science - Alura.

Este arquivo serve como um registro de prática para os seguintes tópicos:
- Manipulação de Listas, Tuplas e Dicionários
- List Comprehensions
- Dict Comprehensions
- Estruturação de dados com 'zip', 'range' e 'enumerate'
- Uso de 'set' para encontrar valores únicos
- Lógica de agrupamento e contagem
"""


# 1. Soma de sub-listas: Feito com list comprehension após pesquisar a função sum().
lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]
lista_de_listas_somadas = [sum(lista) for lista in lista_de_listas]


# 2. Extração de elementos de tuplas: Feito sozinho com list comprehension e lógica de índices.
lista_de_tuplas_ex2 = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
T_elementos_separados = [tupla[2] for tupla in lista_de_tuplas_ex2]


# 3. Criando tuplas (índice, valor): Feito com list comprehension após pesquisar a função .index() e depois aprimorado para enumerate().
lista_nomes = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
lista_de_tuplas_nomes = [(indice, nome) for indice, nome in enumerate(lista_nomes)]


# 4. List comprehension com filtro (if): Feito sozinho, aplicando a lógica de filtro 'if' no comprehension.
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
lista_numerica_apartamento = [apartamento[1] for apartamento in aluguel if apartamento[0] == "Apartamento"]


# 5. Dict comprehension a partir de duas listas: Feito após revisar aulas sobre como parear listas (com 'range' ou 'zip').
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
dic_comprehension = {mes: valor for mes, valor in zip(meses, despesa)}


# 6. List comprehension com filtro duplo (and): Feito sozinho, aplicando lógica com 'and' dentro do filtro 'if'.
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
lista_filtrada_2022 = [lista for lista in vendas if lista[0] == "2022" and lista[1] >= 6000]


# 7. List comprehension com 'if-else' aninhado: Feito após pesquisar a sintaxe de 'if-else' ternário aninhado em comprehensions.
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
rotulos = ['Hipoglicemia', 'Normal', 'Alterada', 'Diabetes']
lista_de_tuplas_clinica = [
    (rotulos[0], i) if i <= 70 else
    (rotulos[1], i) if i <= 99 else
    (rotulos[2], i) if i <= 125 else
    (rotulos[3], i)
    for i in glicemia
]


# 8. Agrupando múltiplas listas e adicionando um cabeçalho: Feito sozinho, apenas com pesquisa sobre a estrutura de cabeçalho de tabela.
id_venda = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

cabecalho = [('id', 'quantidade', 'preco', 'total')]
dados = [(id_venda[i], quantidade[i], preco[i], round(quantidade[i] * preco[i], 2)) for i in range(len(id_venda))]
tabela_final = cabecalho + dados


# 9. Contagem de itens únicos: Feito após pesquisar como usar 'set()' para obter valores únicos e 'list.count()' para contagem.
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
dict_contagem_estados = {estado: estados.count(estado) for estado in set(estados)}


# 10. Agrupando dados em dicionário (loop 'for'): Feito com loop 'for' padrão, pois 'comprehensions' seriam muito complexas.
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES', 9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG', 8), ('ES', 8), ('SP', 9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

dic_listas_por_estado = {}
dic_soma_por_estado = {}

for estado, valor in funcionarios:
    # Lógica para Dicionário de Listas
    if estado not in dic_listas_por_estado:
        dic_listas_por_estado[estado] = []
    dic_listas_por_estado[estado].append(valor)

    # Lógica para Dicionário de Somas
    if estado not in dic_soma_por_estado:
        dic_soma_por_estado[estado] = 0
    dic_soma_por_estado[estado] += valor


#
# ===================================================================
# --- BLOCO DE EXECUÇÃO (LOG DE SAÍDA) ---
# ===================================================================
#
if __name__ == "__main__":

    print("======== LOG DE SAÍDA DO MÓDULO 3 ========")

    # Imprime os resultados simples em uma linha
    print(f"1. Soma de sub-listas: {lista_de_listas_somadas}")
    print(f"2. Extração de elementos: {T_elementos_separados}")
    print(f"3. Tuplas (índice, valor): {lista_de_tuplas_nomes}")
    print(f"4. Filtro (if): {lista_numerica_apartamento}")
    print(f"5. Dict comprehension: {dic_comprehension}")
    print(f"6. Filtro duplo (and): {lista_filtrada_2022}")

    # Para listas/tabelas longas, usamos um 'for' para imprimir linha a linha
    print(f"\n7. 'if-else' aninhado:")
    for item in lista_de_tuplas_clinica:
        print(f"  {item}")

    print(f"\n8. Tabela com Cabeçalho:")
    for linha in tabela_final:
        print(f"  {linha}")

    # De volta aos prints de uma linha
    print(f"\n9. Contagem de itens únicos: {dict_contagem_estados}")

    # Para resultados duplos, separamos para clareza
    print(f"\n10. Agrupamento de Dados:")
    print(f"  Listas por estado: {dic_listas_por_estado}")
    print(f"  Soma por estado:   {dic_soma_por_estado}")

    print("\n======== FIM DO LOG ========")