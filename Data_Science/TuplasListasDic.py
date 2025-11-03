#Aquecimento
#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
#versão sozinho pesquisando sobre append
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
lista_de_listas_somadas = []
for lista in lista_de_listas:
    lista_de_listas_somadas.append(lista[0] + lista[1] + lista[2] + lista[3])
#print(lista_de_listas_somadas)

#versão sozinho pesquisando a função sum
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
lista_de_listas_somadas = []
for lista in lista_de_listas:
    lista_de_listas_somadas.append(sum(lista))
#print(lista_de_listas_somadas)

#variando... pra encurtar , tentei várias vezes e por fim usei o método de exemplo da IA do google
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
lista_de_listas_somadas = [sum(lista) for lista in lista_de_listas]
print("Atividade 1: ",lista_de_listas_somadas)

#2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
#versão sozinho sem pesquisar, como ficou curto, parei por aq e ainda acertei de primeira hehehe
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
T_elementos_separados = [lista[2] for lista in lista_de_tuplas]
print("Atividade 2: ",T_elementos_separados)

#3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.
#versão sozinho pesquisando como descobrir a posição de um item da lista apenas, descoberto .index()
lista_nomes = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
lista_de_tuplas = []
for lista in lista_nomes:
    lista_de_tuplas.append((lista_nomes.index(lista),lista))
#print(lista_de_tuplas)

#versão variada sozinho pra encurtar o código. Obs: pesquisei como adicionar elementos em tupla usando essa expressão e descobri a expressão "tuple()", mas por acidente realizando teste, ao colocar ".index(lista)" acabei gerando o resultado que eu queria, e assim compreendi que a primeira expressão da list comprehension é onde podemos realizar oq fazer com o retorno do for q vem a seguir, pelo menos eu acho q é isso.
lista_de_tuplas2 = tuple(lista.index(lista) for lista in lista_nomes)
print("Atividade 3: ",lista_de_tuplas)

#4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
#versão sozinho sem precisar pesquisar nada, ficou curto então deixarei assim. Compreensão melhor do list comprehension, agora percebi que a leitura inicia pelo for, passa pelas condição if e após isso passa pela expressão inicial, q neste caso é o apartamento[1].
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
lista_numerica_apartamento = [apartamento[1] for apartamento in aluguel if apartamento[0] == "Apartamento"]
print("Atividade 4: ",lista_numerica_apartamento)

#5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
#Versão sozinho, este me pegou de surpresa, tive que voltar a uma aula anterior do curso pra compreender como juntar valores de 2 lista em um dicionário, apenas retornei a parte exata do video e já fiz o resto sozinho.
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
dic_comprehension = {meses[i]:despesa[i] for i in range(len(meses))}
print("Atividade 5: ",dic_comprehension)

#6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código. Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.
#Eu não entendi se quer somente os valores acima de 6 mil ou o ano junto, ent por via das dúvidas coloquei o ano junto. Este fiz sozinho sem pesquisas, apenas lembrando conteúdo teórico. O resultado foi lista de tuplas, mas se o pedido for somente o valor 6 mil, então bastaria colocar "lista_filtrada_2022 = [lista[1] for lista in vendas if lista[0] == "2022" and lista[1] >= 6000]" e pronto, uma lista única!
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
lista_filtrada_2022 = [lista for lista in vendas if lista[0] == "2022" and lista[1] >= 6000]
#lista_filtrada_2022 = [lista[1] for lista in vendas if lista[0] == "2022" and lista[1] >= 6000]  #Caso seja apenas uma lista única com valres igual ou superior a 6 mil de 2022
print("Atividade 6: ",lista_filtrada_2022)


#7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

#Glicose igual ou inferior a 70: 'Hipoglicemia'
#Glicose entre 70 a 99: 'Normal'
#Glicose entre 100 e 125: 'Alterada'
#Glicose superior a 125: 'Diabetes'
#A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.
#versão sozinho. Essa foi muito díficil, fiquei uns 10 minutos quebrando a cabeça e me rendi a pesquisar: "como fazer uma list comprehension que tenha ao menos 3 if e 1 else?" e vi a sintax como funcionava e então apliquei aqui. Minha compreensão aumentou mais após saber disso, além que percebi q devo primeiro analisar "Oq me impede de resolver o problema? n consigo adicionar mais if na expressão? ent vou pesquisar sobre" e procurar o problema chave pra resolução.
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
rotulos = ['Hipoglicemia','Normal', 'Alterada',  'Diabete']
lista_de_tuplas_clinica = [(rotulos[0],i) if i <= 70 else
                           (rotulos[1],i) if i > 70 and i <= 99 else
                           (rotulos[2],i) if i >100 and i <= 125 else
                           (rotulos[3],i)
                           for i in glicemia]
print("Atividade 7: ",lista_de_tuplas_clinica)


#8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:
#O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.
#Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

#versão sozinho. Outra muito díficil,, mas esta fiz sozinho. Tive dificuldade pra compreender a formatação da tabela, ent pesquisei "oq é cabeçalho de uma tabela e oq significaria q o primeiro valor é o cabeçalho da tabela?" Assim compreendi como é o formato da saída esperado e com isso montei o código sozinho.
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
colunas = [('id', 'quantidade', 'preco', 'total')]
#tabela = [(colunas[0], id[i], colunas[1], quantidade[i], colunas[2], preco[i], colunas[3], quantidade[i]*preco[i]) for i in range(len(id))]
tabela = [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
colunas += tabela
print("Atividade 8:",colunas)

#9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence:

#A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

#A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

#Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui o nome de apenas um Estado com valores repetidos.
#versão sozinho. Aqui tive que pesquisar, teve jeito. Pesquisei por "como posso identificar vários valores string ou inteiros e contar eles apartir de uma lista criando um dict comprehension informando a quantidade das strings iguais que apareceram ou numeros inteiros repetidos. como poderia fazer isso?" e "o parametro set no for faz oq?", com isso aprendi do parametro set e list.count() que foram muito útil.

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
dict_comprehension = {estado:estados.count(estado) for estado in set(estados)}
print("Atividade 9:",dict_comprehension)


#10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:
#A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de colaboradores(as) por Estado.
#Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui apenas os valores numéricos de funcionários(as) de cada Estado.

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

# (O primeiro pedido do exercício)
dic_listas_por_estado = {}

# (O segundo pedido do exercício)
dic_soma_por_estado = {}

for tupla in funcionarios:
    estado = tupla[0]  # Pega o estado (ex: 'SP')
    valor = tupla[1]    # Pega o valor (ex: 16)

    # --- Lógica para o Dicionário de Listas ---
    if estado not in dic_listas_por_estado:
        dic_listas_por_estado[estado] = [valor]

    else:
        dic_listas_por_estado[estado].append(valor)

    # --- Lógica para o Dicionário de Somas ---
    if estado not in dic_soma_por_estado:
        dic_soma_por_estado[estado] = valor

    else:
        dic_soma_por_estado[estado] += valor

print("Atividade 10: Primeiro dicionário = ", dic_listas_por_estado, "Segundo dicionário = ",dic_soma_por_estado)





#========= LOG DE SAÍDA DE CADA ATIVIDADE/RESULTADO DE CADA UM NO TERMINAL =========
"""Atividade 1:  [24, 10, 16]
Atividade 2:  [81, 67, 83]
Atividade 3:  [(0, 'Pedro'), (1, 'Júlia'), (2, 'Otávio'), (3, 'Eduardo')]
Atividade 4:  [1700, 1400, 1900]
Atividade 5:  {'Jan': 860, 'Fev': 490, 'Mar': 1010, 'Abr': 780, 'Mai': 900, 'Jun': 630, 'Jul': 590, 'Ago': 770, 'Set': 620, 'Out': 560, 'Nov': 840, 'Dez': 360}
Atividade 6:  [('2022', 8883), ('2022', 7688), ('2022', 9544), ('2022', 8190)]
Atividade 7:  [('Diabete', 129), ('Normal', 82), ('Hipoglicemia', 60), ('Normal', 97), ('Alterada', 101), ('Hipoglicemia', 65), ('Hipoglicemia', 62), ('Diabete', 167), ('Normal', 87), ('Hipoglicemia', 53), ('Hipoglicemia', 58), ('Normal', 92), ('Hipoglicemia', 66), ('Alterada', 120), ('Alterada', 109), ('Hipoglicemia', 62), ('Normal', 86), ('Normal', 96), ('Alterada', 103), ('Normal', 88), ('Diabete', 155), ('Hipoglicemia', 52), ('Normal', 89), ('Normal', 73)]
Atividade 8: [('id', 0, 'quantidade', 15, 'preco', 93.0, 'total', 1395.0), ('id', 1, 'quantidade', 12, 'preco', 102.0, 'total', 1224.0), ('id', 2, 'quantidade', 1, 'preco', 18.0, 'total', 18.0), ('id', 3, 'quantidade', 15, 'preco', 41.0, 'total', 615.0), ('id', 4, 'quantidade', 2, 'preco', 122.0, 'total', 244.0), ('id', 5, 'quantidade', 11, 'preco', 14.0, 'total', 154.0), ('id', 6, 'quantidade', 2, 'preco', 71.0, 'total', 142.0), ('id', 7, 'quantidade', 12, 'preco', 48.0, 'total', 576.0), ('id', 8, 'quantidade', 2, 'preco', 14.0, 'total', 28.0), ('id', 9, 'quantidade', 4, 'preco', 144.0, 'total', 576.0)]
Atividade 9: {'SP': 8, 'RJ': 2, 'ES': 6, 'MG': 7}
Atividade 10: Primeiro dicionário =  {'SP': [16, 10, 7, 11, 9, 12, 7, 10], 'ES': [8, 9, 7, 12, 8, 14], 'MG': [9, 6, 4, 8, 5, 10, 12], 'RJ': [13, 9]} Segundo dicionário =  {'SP': 82, 'ES': 58, 'MG': 54, 'RJ': 22} """