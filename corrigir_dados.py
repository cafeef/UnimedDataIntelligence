import csv
import ast

def corrigir_genero(nome):
    """
    Corrige o gênero com base no primeiro nome do paciente.

    Args:
        nome (str): O nome completo do paciente.

    Returns:
        str: Retorna 'Feminino' ou 'Masculino' com base na análise do nome.
    """
    # Lista de primeiros nomes comuns para cada gênero.
    # Esta lista foi criada com base nos nomes presentes no seu arquivo.
    nomes_femininos = [
        'Maria', 'Heloísa', 'Laura', 'Alice', 'Isabella', 'Helena',
        'Sophia', 'Maitê', 'Luísa', 'Cecília'
    ]
    nomes_masculinos = [
        'Arthur', 'Bernardo', 'Miguel', 'Heitor', 'Samuel', 'João',
        'Gabriel', 'Theo', 'Gael', 'Davi'
    ]

    # Extrai o primeiro nome.
    primeiro_nome = nome.split()[0]

    # Verifica se o primeiro nome está na lista de nomes femininos.
    if primeiro_nome in nomes_femininos:
        return 'Feminino'
    # Verifica se o primeiro nome está na lista de nomes masculinos.
    elif primeiro_nome in nomes_masculinos:
        return 'Masculino'
    
    # Se o nome não for encontrado em nenhuma lista, um gênero padrão
    # poderia ser retornado, mas para este caso, assumiremos que
    # os nomes no arquivo se limitam aos listados.
    return 'Gênero não identificado'

def processar_arquivo_txt_para_csv(arquivo_entrada, arquivo_saida):
    """
    Lê um arquivo de texto com dados de pacientes, corrige o gênero
    e salva os dados em um arquivo CSV.

    Args:
        arquivo_entrada (str): O caminho do arquivo .txt de entrada.
        arquivo_saida (str): O caminho do arquivo .csv de saída.
    """
    # Cabeçalho para o arquivo CSV.
    cabecalho = [
        'Nome', 'Carteirinha', 'Idade', 'Genero', 'Dependentes', 'TipoContrato', 'CID', 'CategoriaCID', 'CustoMensal_12M', 'NumeroInternacoes_12M', 'NumeroConsultas_12M', 'NumeroConsultasEmergencia_12M', 'ConsultasEmergencia_3M', 'DiasDesdeUltimaInternacao', 'ProporcaoEmergencias_12M', 'ProbabilidadeRisco', 'Reinternado_30_Dias'
    ]

    # Lista para armazenar todos os dados corrigidos.
    dados_corrigidos = []

    # Tenta abrir e ler o arquivo de entrada.
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f_entrada:
            # O conteúdo completo do arquivo é lido.
            conteudo = f_entrada.read()
            
            # Remove parênteses de abertura/fechamento extras e divide
            # o conteúdo em linhas individuais baseadas no padrão "),\n(".
            linhas_texto = conteudo.strip()[1:-1].split('),\n(')

            for linha in linhas_texto:
                # Garante que a linha seja formatada como uma tupla válida em string.
                linha_tupla_str = f"({linha.strip()})"
                
                try:
                    # 'ast.literal_eval' converte a string de tupla para um objeto tupla real.
                    dados_paciente = ast.literal_eval(linha_tupla_str)
                    
                    # Converte a tupla para uma lista para que possamos modificar os dados.
                    lista_paciente = list(dados_paciente)
                    
                    # Extrai o nome do paciente (primeiro item da lista).
                    nome_paciente = lista_paciente[0]
                    
                    # Chama a função para obter o gênero correto.
                    genero_corrigido = corrigir_genero(nome_paciente)
                    
                    # Atualiza o gênero na lista de dados do paciente (o gênero é o quarto item).
                    lista_paciente[3] = genero_corrigido
                    
                    # Adiciona a lista corrigida à nossa lista principal.
                    dados_corrigidos.append(lista_paciente)

                except (ValueError, SyntaxError) as e:
                    print(f"Erro ao processar a linha: {linha}\nErro: {e}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
        return

    # Tenta abrir e escrever no arquivo de saída.
    try:
        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as f_saida:
            # Cria um objeto de escrita CSV.
            writer = csv.writer(f_saida)
            
            # Escreve a linha de cabeçalho no arquivo CSV.
            writer.writerow(cabecalho)
            
            # Escreve todos os dados dos pacientes corrigidos.
            writer.writerows(dados_corrigidos)
        
        print(f"Arquivo '{arquivo_saida}' criado com sucesso!")

    except IOError:
        print(f"Erro: Não foi possível escrever no arquivo '{arquivo_saida}'.")

# --- Execução do Script ---
# Define o nome do arquivo de entrada e de saída.
arquivo_txt = 'unimed.txt'
arquivo_csv = 'unimed_corrigido.csv'

# Chama a função principal para iniciar o processo.
processar_arquivo_txt_para_csv(arquivo_txt, arquivo_csv)