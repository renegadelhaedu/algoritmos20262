#estruturas de dados
#Lista (list) []
#Dicionário (dict) {chave:valor}
#Conjunto (set) {valor}

#Conjunto obriga itens diferentes e não garante ordem

#cria o conjunto
alunos = set()
profs = {'rene','erlon','samira','fernanda'}

#percorrendo/iterando a estrutura de dados
#for p in profs:
#    print(p)

#adicionar item no conjunto
alunos.add('arthur')
alunos.add('thamires')
alunos.add('enzo')
#print(alunos)
'''

#buscar
busca = input('digite o nome do aluno para buscarmos: ')
for aluno in alunos:
    if busca == aluno:
        print(f'Achamos {aluno} no conjunto')
'''


#remover
if 'jessica' in profs:
    profs.remove('jessica')
print(profs)

#atualizar
profs.remove('rene')
profs.add('renan')

#CRUD
#Inserir, Ler/buscar, atualizar, remover







