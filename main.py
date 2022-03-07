'''gerar um programa que irá receber como input um arquivo csv
contendo informações pessoais de usuários e deverá validar todos os dados com base na descrição'''

import csv


with open("cadastros.csv", "r") as arquivo: #em cadastros.csv é o arquivo com as informações, em caso de trocar o arquivo é só mudar o nome de referencia
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("cabeçalho: " + str(linha))
        else:
            print("valor: " + str(linha))










