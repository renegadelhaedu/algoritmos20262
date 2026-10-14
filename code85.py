#construa um algoritmo que o nome de 150 pessoas e verifique
#quantas possuem maria no nome. exiba o total no final

qtde = 0
for i in range(5):
    nome = input('Digite o nome: ')
    if 'maria' in nome:
        qtde = qtde + 1

print(f'achamos no final um total de {qtde} marias')