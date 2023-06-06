import os
import pandas as pd
import shutil

# Passo 1: Pedir entrada do diretório das fotos
diretorio_fotos = input("Digite o diretório que contém as fotos: ")

# Passo 2: Pedir entrada do arquivo xlsx com nomes das fotos
caminho_arquivo_xlsx = input("Digite o caminho do arquivo xlsx com os nomes das fotos: ")

# Passo 3: Ler os arquivos jpg do diretório e selecionar apenas as fotos listadas no xlsx
fotos_selecionadas = []
df = pd.read_excel(caminho_arquivo_xlsx)

# Verificar se a coluna "Diretório" existe no DataFrame
if "Diretorio" in df.columns:
    for i, row in df.iterrows():
        diretorio = row["Diretorio"]
        nome_foto = diretorio.split("/")[-1].split(".jpg")[0]
        caminho_foto = os.path.join(diretorio_fotos, nome_foto + ".jpg")
        if os.path.exists(caminho_foto):
            fotos_selecionadas.append(caminho_foto)
else:
    print("A coluna 'Diretório' não foi encontrada no arquivo XLSX.")

# Passo 4: Imprimir mensagem de "fotos selecionadas"
print("Fotos selecionadas:")
print(fotos_selecionadas)

# Passo 5: Pedir diretório de saída e exportar as fotos selecionadas para lá
diretorio_saida = input("Digite o diretório de saída: ")

for foto in fotos_selecionadas:
    nome_foto = os.path.basename(foto)
    caminho_destino = os.path.join(diretorio_saida, nome_foto)
    shutil.copyfile(foto, caminho_destino)

print("Exportação concluída.")
