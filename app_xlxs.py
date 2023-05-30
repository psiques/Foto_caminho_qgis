import os
import openpyxl

def criar_xlsx_com_nomes(diretorio):
    # Criar uma instância do Workbook
    wb = openpyxl.Workbook()
    # Selecionar a primeira planilha
    planilha = wb.active

    # Definir o cabeçalho das colunas
    planilha['A1'] = 'num_foto'
    planilha['B1'] = 'cam_foto'

    # Percorrer os arquivos no diretório
    num_foto = 1
    for nome_arquivo in os.listdir(diretorio):
        cam_foto = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(cam_foto) and nome_arquivo.endswith('.jpg'):
            # Adicionar o número da foto e o caminho à planilha
            planilha.append([num_foto, cam_foto])
            num_foto += 1

    # Salvar o arquivo XLSX
    nome_arquivo_xlsx = os.path.join(diretorio, 'nomes_fotos.xlsx')
    wb.save(nome_arquivo_xlsx)
    print(f'Arquivo {nome_arquivo_xlsx} salvo com sucesso!')

# Solicitar o diretório ao usuário
diretorio = input("Digite o caminho para o diretório: ")
criar_xlsx_com_nomes(diretorio)
