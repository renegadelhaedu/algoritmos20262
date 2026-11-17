'''
construa um algoritmo que abra um diário em texto (arquivo) e
salve o que o usuário digitar sempre pedindo a data e o texto
'''

arquivo = open('vida.txt','a',encoding='utf-8')
data = input('Digite a data de hoje: ')
relato = input('Abra seu coração: ')

arquivo.write(data + ': ' + relato + '\n')
arquivo.close()

