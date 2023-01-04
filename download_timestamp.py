import requests, os, sys
from datetime import datetime
from download_data import download_data

# Leitura do arquivo de data da coleta
def get_data_carga(file_name):
    with open(file_name, encoding='utf-8-sig') as in_file:
        return  in_file.read().strip()

# Compara a última data de carga registrada no arquivo last_data_carga.txt com a data atual
def check_data_carga(data_str):
    current_data_carga = data_str
    last_data_carga = get_data_carga('last_data_carga.txt')
    
    t1 = datetime.strptime(current_data_carga, "%d/%m/%Y %H:%M:%S")
    t2 = datetime.strptime(last_data_carga, "%d/%m/%Y %H:%M:%S")

    # True se a data atual for maior que a ultima data
    return t1 > t2

if __name__ == '__main__':

    repositorio = "https://repositorio.dados.gov.br/seges/detru/"
    
    # Coleta o arquivo de data para verificação
    print('Verificando datas ...\n')
    
    current_data_carga = requests.get(repositorio + "data_carga_siconv.txt").content.decode(encoding='utf-8-sig').strip()
    
    if check_data_carga(current_data_carga):
        if len(sys.argv) < 2:
            print(sys.argv)
            download_data()
        else:
            download_data(sys.argv[1])

        with open('last_data_carga.txt', 'w') as out_file:
            out_file.write(current_data_carga)
            out_file.close()
    else:
        print("Dados já foram coletados para esta data!")

