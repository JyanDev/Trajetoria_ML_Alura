#Aquecimento

#1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
#Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

try:
    #dividendo = float(input("Número do dividendo: "))
    #divisor = float(input("Número do divisor: "))
    dividendo = 1
    divisor = 10
    resultado = dividendo/divisor
except ValueError as v:
    print(f"Somente números!")
except ZeroDivisionError:
    print(f"AT1: Resultado da divisão: 0.00")
else:
    print(f"AT1: Resultado da divisão: {resultado:.2f}")


#2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.
#Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:

    #chave = str(input("Nome para buscar:"))
    chave = "Carol"
    valor = idades[chave]

except KeyError as k:
    print("Nome não encontrado")

else:
    print(f"AT2: Idade de {chave} é {valor}")


#3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.

def converter_float(lista = []):
    lista_float = []
    if type(lista) == list:
        for num in lista:
            if isinstance(num, (int, float)):
                lista_float.append(float(num))
                continue
            else:
                continue
        return lista_float
    else:
        raise TypeError ()

try:
    lista_valores = ["1",1,2,3,4]
    lista_valores_f = converter_float(lista_valores)
    print(f"AT3: Convertendo lista do tipo {type(lista_valores[1]).__name__} para {type(lista_valores_f[1]).__name__}...")

except TypeError:
    print(f" Certifique-se de ser uma lista adequada to tipo list. Exemplo: [1,2,3,...]")

except IndexError as i:
    print(f"Erro: {type(i).__name__}. Certifique-se de não haver tuplas, dict, lista dentro de lista ou formato irregular dentro da sua lista.")

except Exception as e:
    print(f"Erro: {type(e).__name__}.")

else:
    print(f"Lista float: {lista_valores_f} ")
finally:
    print("Fim da execução da função")

#7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.
#
#Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:
#
#Verificar se as listas têm o mesmo tamanho (ValueError)
#Verificar se existe alguma divisão por zero (ZeroDivisionError)
#Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.
#
#Como teste, use os seguintes dados:
#
#Dados sem exceção:
#pressoes = [100, 120, 140, 160, 180]
#temperaturas = [20, 25, 30, 35, 40]
#Copiar código
#Dados com exceção:
#1) Exceção de ZeroDivisionError
#
#pressoes = [60, 120, 140, 160, 180]
#temperaturas = [0, 25, 30, 35, 40]
#Copiar código
#2) Exceção de ValueError
#
#pressoes = [100, 120, 140, 160]
#temperaturas = [20, 25, 30, 35, 40]
#Copiar código
#Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.