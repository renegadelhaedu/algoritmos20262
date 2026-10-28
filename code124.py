#dict: itens ordenados
#lista: acessível por índice, ordenada

alunos = {}
profs = dict()
carros = {'onix':89, 'hb20':93, 'polo': 106}
#adicionar
carros['vectra'] = 140
#remover pela chave
carros.pop('hb20')
#atualizar valor
carros['polo'] = 114
print(carros)
