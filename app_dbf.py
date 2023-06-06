import os
import openpyxl

def criar_xlsx_com_nomes(Diretorio):
    # Criar uma instância do Workbook
    wb = openpyxl.Workbook()
    # Selecionar a primeira planilha
    planilha = wb.active

    # Definir o cabeçalho das colunas
    planilha['A1'] = 'Fotos'
    planilha['B1'] = 'Diretorio'

    # Percorrer os arquivos no diretório
    num_foto = 1
    for nome_arquivo in os.listdir(Diretorio):
        cam_foto = os.path.join(Diretorio, nome_arquivo)
        if os.path.isfile(cam_foto) and nome_arquivo.endswith('.jpg'):
            # Adicionar o número da foto e o caminho à planilha
            planilha.append([num_foto, cam_foto])
            num_foto = 'h'+str(nome_arquivo[11:13])+str(nome_arquivo[14:16])+str(nome_arquivo[17:19])+',000'

    # Salvar o arquivo XLSX
    nome_arquivo_xlsx = os.path.join(Diretorio, 'nomes_fotos.xlsx')
    wb.save(nome_arquivo_xlsx)
    print(f'Arquivo {nome_arquivo_xlsx} salvo com sucesso!')

# Solicitar o diretório ao usuário
Diretorio = input("Digite o caminho para o diretório: ")
criar_xlsx_com_nomes(Diretorio)
