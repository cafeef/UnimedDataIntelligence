# -*- coding: utf-8 -*-

# Documentação:
# Este script foi criado para ler dados de um arquivo de texto (.txt)
# e convertê-los para um formato de valores separados por vírgula (.csv).
# Ele assume que cada linha no arquivo .txt contém uma estrutura de dados
# em formato de tupla do Python.

# Importamos as bibliotecas necessárias.
# 'csv' é a biblioteca padrão do Python para trabalhar com arquivos CSV.
# 'ast' (Abstract Syntax Trees) nos ajuda a converter de forma segura
# uma string que parece uma tupla em uma tupla de verdade.
import csv
import ast

# --- Configuração ---
# Aqui definimos os nomes dos arquivos que vamos usar.
# Você pode alterar esses nomes se precisar.
nome_arquivo_entrada = 'unimed.txt'
nome_arquivo_saida = 'unimed.csv'

# Aqui está o cabeçalho para o nosso arquivo CSV, exatamente como você pediu.
cabecalho_csv = [
    'Nome', 'Carteirinha', 'Idade', 'Genero', 'Dependentes', 'TipoContrato', 
    'CID', 'CategoriaCID', 'CustoMensal_12M', 'NumeroInternacoes_12M', 
    'NumeroConsultas_12M', 'NumeroConsultasEmergencia_12M', 
    'ConsultasEmergencia_3M', 'DiasDesdeUltimaInternacao', 
    'ProporcaoEmergencias_12M', 'ProbabilidadeRisco', 'Reinternado_30_Dias'
]

# --- Lógica Principal ---
# O bloco 'try...except' é uma boa prática para lidar com possíveis erros,
# como o arquivo de entrada não ser encontrado.
try:
    # Usamos 'with open' para garantir que os arquivos sejam abertos e
    # fechados corretamente, mesmo que ocorra um erro.
    # 'arquivo_txt' é o nosso arquivo de entrada (leitura 'r').
    # 'arquivo_csv' é o nosso arquivo de saída (escrita 'w').
    # 'newline=""' evita que o 'csv.writer' adicione linhas em branco.
    with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo_txt, \
         open(nome_arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_csv:

        # Criamos um "escritor" CSV que saberá como formatar nossos dados
        # corretamente no arquivo de saída.
        escritor_csv = csv.writer(arquivo_csv)

        # 1. Escrevemos a linha de cabeçalho no arquivo CSV.
        print("Escrevendo o cabeçalho no arquivo CSV...")
        escritor_csv.writerow(cabecalho_csv)

        # 2. Agora, vamos percorrer cada linha do arquivo de texto de entrada.
        print("Lendo os dados do arquivo de texto e processando...")
        for linha_texto in arquivo_txt:
            # 'linha_texto.strip()' remove espaços em branco ou quebras de
            # linha no início e no fim da linha.
            linha_limpa = linha_texto.strip()

            # Verificamos se a linha não está vazia após a limpeza.
            if linha_limpa:
                # Esta é a parte mais importante!
                # 'ast.literal_eval()' pega a string (ex: "('Arthur Alves', ...)")
                # e a transforma em uma tupla real do Python. É muito seguro!
                dados_da_linha = ast.literal_eval(linha_limpa)
                
                # 3. Escrevemos os dados processados como uma nova linha no CSV.
                escritor_csv.writerow(dados_da_linha)

    print(f"\nSucesso! O arquivo '{nome_arquivo_saida}' foi criado com sucesso.")

except FileNotFoundError:
    # Caso o arquivo de entrada não exista, mostramos uma mensagem de erro amigável.
    print(f"Erro: O arquivo de entrada '{nome_arquivo_entrada}' não foi encontrado.")
except Exception as e:
    # Captura qualquer outro erro que possa acontecer durante o processo.
    print(f"Ocorreu um erro inesperado: {e}")