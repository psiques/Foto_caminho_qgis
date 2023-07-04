import os
import glob
import re
import pandas as pd
from pyproj import CRS, Transformer

def obter_nome_saida(saida):
    arquivos_saida = glob.glob(os.path.join(saida, 'Saida_*.xlsx'))
    if arquivos_saida:
        padrao = r"Saida_([\w\d]+)\.xlsx"
        nomes = [re.search(padrao, arquivo).group(1) for arquivo in arquivos_saida]
        ultimo_numero = max([int(re.findall(r'\d+', nome)[-1]) for nome in nomes])
        return f'cam{ultimo_numero + 1}'
    else:
        return 'cam1'

sistema_origem = CRS.from_string('+proj=utm +zone=19 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs +south')  # SIRGAS 2000 UTM Zona 19
sistema_destino = CRS.from_epsg(4326)  # EPSG 4326 representa o sistema de coordenadas geográficas (WGS84)
transformador = Transformer.from_crs(sistema_origem, sistema_destino)

pasta = input('Entre com o diretório das fotos: ')
saida = input('Entre com o diretório de saída: ')
nome_saida = obter_nome_saida(saida)

lista = []
lista_fim = []
for i in os.walk(pasta):
    lista.append(i)

for i in lista[0][2]:
    lista_fim.append(i)

lista_fotos = []
for i in lista_fim:
    if '.jpg' in i:
        lista_fotos.append(i)

nome_original = []
nome_foto = []
for i in lista_fotos:
    nome = 'h' + str(i[11:13]) + str(i[14:16]) + str(i[17:19]) + ',000'
    nome_original.append(nome)
    nome_foto.append(i)

lista_fotos_final = []
for i in lista_fotos:
    lista_fotos_final.append(os.path.join(pasta, i))

planilha = pd.DataFrame({
    'Fotos': nome_original,
    'Diretorio': lista_fotos_final,
    'nom_foto': nome_foto
})

caminho_arquivo = input('Digite o caminho do arquivo de texto: ')
dados_texto = pd.read_csv(caminho_arquivo, sep=r'\t|\s{1,}', names=['x', 'y', 'z', 'Chave_Foto_Log'], dtype=str, usecols=[0, 1, 2, 3])
dados_texto['Chave_Foto_Log'] = dados_texto['Chave_Foto_Log'].str.strip()

dados_final = pd.merge(planilha, dados_texto, left_on='Fotos', right_on='Chave_Foto_Log', how='left')
dados_final[['x', 'y']] = dados_final[['x', 'y']].replace(',', '.', regex=True)
dados_final[['x', 'y']] = dados_final[['x', 'y']].astype(float)

dados_final[['lat', 'long']] = dados_final[['x', 'y']].apply(lambda row: transformador.transform(row['x'], row['y']), axis=1, result_type='expand')

dados_final = dados_final.drop(['Chave_Foto_Log'], axis=1)

nome_pai = os.path.basename(os.path.dirname(os.path.dirname(pasta)))
caminho_saida = os.path.join(saida, f'{nome_pai}_{nome_saida}.xlsx')

contador = 2
while os.path.exists(caminho_saida):
    caminho_saida = os.path.join(saida, f'{nome_pai}_{nome_saida}_{contador}.xlsx')
    contador += 1

dados_final.to_excel(caminho_saida, index=False)

caminho_txt = os.path.join(saida, f'{nome_pai}_{nome_saida}.txt')
dados_txt = dados_final[['nom_foto', 'lat', 'long']]
dados_txt.to_csv(caminho_txt, index=False, sep=',', header=['SourceFile', 'GPSLatitude', 'GPSLongitude'])

print('FINALIZADO')
