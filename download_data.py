import wget, sys, os
from zipfile import ZipFile

# Leitura da lista de arquivos a serem baixados
def get_file_list():
    
    file_list = []

    with open("files.txt") as in_file:
        for line in in_file:
            file_list.append(line.strip())

    return file_list

def download_data(download_dir:str = "downloads/"):
    # Verifica se existe diretório de daowload padrão
    if download_dir == "downloads/":
        if not os.path.exists(download_dir):
            os.system("mkdir downloads")

    repositorio = "https://repositorio.dados.gov.br/seges/detru/"
    
    # Lista de arquivos a serem coletados
    file_list = get_file_list()

    print("Baixando arquivos ...")
    
    for file_name in file_list:
        print('\n' + file_name)
        
        arquivo_zip = download_dir + file_name
        
        # Exclui se já existir uma cópia do arquivo
        if os.path.exists(arquivo_zip):
            os.system("rm " + arquivo_zip)

        # Download do arquivo zip
        wget.download(repositorio + file_name, arquivo_zip)
        
        # Extraindo o arquivo
        zf = ZipFile(arquivo_zip, 'r')
        zf.extractall(download_dir)
        zf.close()

        # Excluindo arquivo zip
        os.system("rm " + arquivo_zip) 
    

if __name__ == '__main__':
    
    # Caso não passe o caminho no parametro o diretório default é dawnloads/
    if len(sys.argv) < 2:
        print(sys.argv)
        download_data()
    else:
        download_data(sys.argv[1])


