import os
import pandas as pd
import shutil

# Pedir entrada dos caminhos dos arquivos xlsx para Cam1 e Cam2
caminho_arquivo_cam1 = input("Digite o caminho do arquivo xlsx para Cam1: ")
caminho_arquivo_cam2 = input("Digite o caminho do arquivo xlsx para Cam2: ")

# Ler as tabelas xlsx para Cam1 e Cam2
df_cam1 = pd.read_excel(caminho_arquivo_cam1)
df_cam2 = pd.read_excel(caminho_arquivo_cam2)

# Verificar se a coluna "Diretorio" existe nas tabelas
if "Diretorio" not in df_cam1.columns:
    print("Coluna 'Diretorio' não encontrada na tabela de Cam1.")
    exit()

if "Diretorio" not in df_cam2.columns:
    print("Coluna 'Diretorio' não encontrada na tabela de Cam2.")
    exit()

# Pedir diretório de saída
diretorio_saida = input("Digite o diretório de saída: ")

# Criar as pastas CAM1 e CAM2 no diretório de saída
pasta_cam1 = os.path.join(diretorio_saida, "CAM1")
pasta_cam2 = os.path.join(diretorio_saida, "CAM2")

os.makedirs(pasta_cam1, exist_ok=True)
os.makedirs(pasta_cam2, exist_ok=True)

# Exportar as fotos para as respectivas pastas
fotos_cam1 = []
fotos_cam2 = []

for index, row in df_cam1.iterrows():
    if isinstance(row["Diretorio"], str):
        nome_foto = os.path.basename(row["Diretorio"])
        caminho_foto = row["Diretorio"]

        if os.path.exists(caminho_foto):
            fotos_cam1.append(caminho_foto)

for index, row in df_cam2.iterrows():
    if isinstance(row["Diretorio"], str):
        nome_foto = os.path.basename(row["Diretorio"])
        caminho_foto = row["Diretorio"]

        if os.path.exists(caminho_foto):
            fotos_cam2.append(caminho_foto)

for foto in fotos_cam1:
    nome_foto = os.path.basename(foto)
    caminho_destino = os.path.join(pasta_cam1, nome_foto)
    shutil.copyfile(foto, caminho_destino)

for foto in fotos_cam2:
    nome_foto = os.path.basename(foto)
    caminho_destino = os.path.join(pasta_cam2, nome_foto)
    shutil.copyfile(foto, caminho_destino)

print("Exportação concluída.")
