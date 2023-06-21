import pandas as pd
import os

setar_tab = input("Insira o caminho da tabela:")
setar_fotos = input("Insira o diretório de fotos:")

ler_tab = pd.read_excel(setar_tab)

pastas_n_achadas = []
pastas_n_presentes = []
menos_2 = []

for index, row in ler_tab.iterrows():
    nom_atual = row['Correlativo']
    nom_novo = row['nom_novo']
    pasta_atual = os.path.join(setar_fotos, str(nom_atual))
    pasta_nova = os.path.join(setar_fotos, str(nom_novo))
    
    if nom_atual in os.listdir(setar_fotos):
        os.rename(pasta_atual, pasta_nova)
    else:
        pastas_n_achadas.append(nom_atual)

    if nom_atual not in os.listdir(setar_fotos):
        pastas_n_presentes.append(nom_atual)

print("\nPastas não encontradas na tabela:")
print(pastas_n_achadas)

print("\nPastas não presentes no diretório:")
print(pastas_n_presentes)

# Exportar informações para um arquivo txt
contador = 1
arquivo_nome = "renomeacao_pastas.txt"
while os.path.exists(arquivo_nome):
    arquivo_nome = f"renomeacao_pastas_{contador}.txt"
    contador += 1

with open(arquivo_nome, "w") as arquivo:
    arquivo.write("Pastas renomeadas:\n")
    for index, row in ler_tab.iterrows():
        nom_atual = row['Correlativo']
        nom_novo = row['nom_novo']
        arquivo.write(f"Nome antigo: {nom_atual}\tNome novo: {nom_novo}\n")

print(f"Arquivo '{arquivo_nome}' exportado com sucesso!")
