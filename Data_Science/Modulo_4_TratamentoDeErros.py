"""
Exercícios do Módulo 4 da Formação de Data Science - Alura.

Este arquivo serve como um registro de prática para os seguintes tópicos:
- Tratamento de Exceções (try, except, else, finally)
- Captura de erros específicos (ValueError, KeyError, ZeroDivisionError)
- Lançamento de exceções personalizadas com 'raise'
- Validação de dados em funções
- Uso avançado de 'zip' com parâmetro 'strict = True'
"""

# 1. Divisão Simples com Tratamento: Captura de ValueError (entrada não numérica) e ZeroDivisionError.
def exercicio_divisao_basica():
    try:
        # Valores hardcoded para teste rápido (simulando input)
        dividendo = 1
        divisor = 10
        resultado = dividendo / divisor
    except ValueError:
        return "Erro: Somente números!"
    except ZeroDivisionError:
        return "AT1: Resultado da divisão: 0.00"
    else:
        return f"AT1: Resultado da divisão: {resultado:.2f}"


# 2. Busca Segura em Dicionário: Tratamento de KeyError para chaves inexistentes.
def exercicio_busca_dicionario():
    idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
    chave = "Carol" # Simulação de input

    try:
        valor = idades[chave]
    except KeyError:
        return "Nome não encontrado"
    else:
        return f"AT2: Idade de {chave} é {valor}"


# 3. Validação de Tipos e Clausula Finally: Função que usa 'raise TypeError' para validar entradas e 'finally' para encerramento.
def converter_float(lista=None):
    if lista is None:
        lista = []

    lista_float = []
    if type(lista) == list:
        for num in lista:
            if isinstance(num, (int, float)):
                lista_float.append(float(num))
            else:
                continue
        return lista_float
    else:
        raise TypeError("A entrada deve ser uma lista.")


# 4. (Desafio) Análise de Dados Laboratoriais:
# Aplicação de zip(strict=True) para garantir integridade dos dados.
# Implementação de lógica de UX para decidir entre 'ver o erro' ou 'forçar o cálculo' ao encontrar divisões por zero.

def divide_colunas(pressao=None, temperaturas=None):
    if pressao is None: pressao = []
    if temperaturas is None: temperaturas = []

    # List comprehension otimizada com round e zip strict
    coluna_divisao = [round(p/t, 2) for p, t in zip(pressao, temperaturas, strict=True)]
    return coluna_divisao

def localizar_zerodivision_error(pressao, temperaturas, force=False):
    if force:
        # Força o cálculo substituindo divisões por zero por 0
        coluna_divisao = [
            0 if t == 0 else round(p/t, 2)
            for p, t in zip(pressao, temperaturas, strict=True)
        ]
        return coluna_divisao
    else:
        # Retorna relatório de onde estão os erros
        report_erros = [
            f"Erro na divisão (índice {i}): Temp {t} / Pressão {p}"
            for i, (p, t) in enumerate(zip(pressao, temperaturas, strict=True))
            if t == 0
        ]
        return report_erros


# ===================================================================
# --- BLOCO DE EXECUÇÃO (TESTES E LOGS) ---
# ===================================================================

if __name__ == "__main__":
    print("======== LOG DE SAÍDA DO MÓDULO 4 (EXCEÇÕES) ========\n")

    # --- Teste Ex 1 ---
    print(exercicio_divisao_basica())

    # --- Teste Ex 2 ---
    print(exercicio_busca_dicionario())

    # --- Teste Ex 3 ---
    try:
        lista_valores = ["1", 1, 2, 3, 4]
        lista_valores_f = converter_float(lista_valores)
        print(f"AT3: Lista convertida: {lista_valores_f}")
    except TypeError as e:
        print(f"AT3 Erro de Tipo: {e}")
    except Exception as e:
        print(f"AT3 Erro genérico: {type(e).__name__}")
    finally:
        print("AT3: Fim da execução da função converter_float")

    # --- Teste Ex 4 (Desafio Complexo) ---
    print("\n--- AT4: Desafio do Laboratório (Interativo) ---")

    # Dados para teste de erro
    pressoes_teste = [60, 120, 140, 160, 180]
    temperaturas_teste = [0, 25, 30, 35, 40] # Contém zero no índice 0

    try:
        print(f"Tentando dividir colunas...")
        print(divide_colunas(pressoes_teste, temperaturas_teste))

    except ValueError:
        print("Erro: As listas possuem tamanhos diferentes (detectado pelo strict=True).")

    except ZeroDivisionError:
        print(">> Alerta: Divisão por zero detectada.")
        # Simulação de interação (pode ser alterada para input real se desejar)
        # force_input = input("Pressione Enter para ver o erro ou digite algo para forçar: ")
        force_input = "force" # Hardcoded para demonstração no log

        if force_input.strip():
            print(f"Modo Forçado Ativado: {localizar_zerodivision_error(pressoes_teste, temperaturas_teste, force=True)}")
        else:
            print(f"Relatório de Erros: {localizar_zerodivision_error(pressoes_teste, temperaturas_teste)}")

    print("\n======== FIM DO LOG ========")