import os
import rarfile
import chardet
from shutil import rmtree

# Possui arquivos com diferentes encoding
# Função para detectar o encoding do arquivo
def detectar_encoding(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

# Descompactar o arquivo .rar e detectar o encoding
def descompactar_e_ler_arquivo(caminho_rar, pasta_destino):
    # Verificar se a pasta de destino existe, se não, criar
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    try:
        # Abrir o arquivo .rar com rarfile
        with rarfile.RarFile(caminho_rar) as rar:
            # Extrair todos os arquivos para a pasta de destino
            rar.extractall(pasta_destino)
            print(f'Arquivos extraídos para {pasta_destino}')

        # Percorrer os arquivos extraídos e tentar detectar o encoding
        for nome_arquivo in os.listdir(pasta_destino):
            caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

            if os.path.isfile(caminho_arquivo):
                encoding = detectar_encoding(caminho_arquivo)
                print(f'O arquivo "{nome_arquivo}" possui o encoding: {encoding}')
                # Ler o conteúdo do arquivo com o encoding detectado
                with open(caminho_arquivo, 'r', encoding=encoding) as file:
                    conteudo = file.read()
                    # print(f'Conteúdo de "{nome_arquivo}":\n{conteudo[:100]}...')  Verificar conteúdo
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Testando Execução
# caminho_rar = 'base_dados/Backup_de_dados_92577.rar'
# pasta_destino = 'pasta_destino'
# descompactar_e_ler_arquivo(caminho_rar, pasta_destino)
