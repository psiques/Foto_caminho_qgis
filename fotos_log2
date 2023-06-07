import os
import pandas as pd
import shutil

# Passo 1: Pedir entrada do arquivo xlsx com nomes das fotos
caminho_arquivo_xlsx = input("Digite o caminho do arquivo xlsx com os nomes das fotos: ")

# Passo 2: Ler a tabela xlsx e obter o diretório das fotos
df = pd.read_excel(caminho_arquivo_xlsx)

# Passo 3: Verificar se a coluna "Diretorio" existe na tabela
if "Diretorio" not in df.columns:
    print("Coluna 'Diretorio' não encontrada na tabela XLSX.")
    exit()

# Passo 4: Pedir diretório de saída
diretorio_saida = input("Digite o diretório de saída: ")

# Passo 5: Exportar as fotos para o diretório de saída
fotos_selecionadas = []

for index, row in df.iterrows():
    if isinstance(row["Diretorio"], str):
        nome_foto = os.path.basename(row["Diretorio"])
        caminho_foto = row["Diretorio"]

        if os.path.exists(caminho_foto):
            fotos_selecionadas.append(caminho_foto)

for foto in fotos_selecionadas:
    nome_foto = os.path.basename(foto)
    caminho_destino = os.path.join(diretorio_saida, nome_foto)
    shutil.copyfile(foto, caminho_destino)

print("Exportação concluída.")
