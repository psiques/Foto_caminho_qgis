import os
from dbfread import DBF
from dbfread import Field

def criar_dbf_com_nomes(diretorio):
    # Criar a estrutura do arquivo DBF
    campos = [Field("num_foto", "C", 10), Field("cam_foto", "C", 255)]
    dbf = DBF(filename=os.path.join(diretorio, 'nomes_fotos.dbf'), fields=campos, dbt=False)

    # Percorrer os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        cam_foto = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(cam_foto) and nome_arquivo.endswith('.jpg'):
            # Extrair os caracteres desejados do nome do arquivo
            num_foto = 'h'+nome_arquivo[2:5] + nome_arquivo[7:12]

            # Adicionar o número da foto e o caminho ao arquivo DBF
            dbf.write({"num_foto": num_foto, "cam_foto": cam_foto})

    print('Arquivo DBF salvo com sucesso!')

# Solicitar o diretório ao usuário
diretorio = input("Digite o caminho para o diretório: ")
criar_dbf_com_nomes(diretorio)