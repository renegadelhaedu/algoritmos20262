#4 tipos de funções
#tipo 3: com parâmetros entrada, com retorno

def buscar(lista, nome):
    achei = False
    for aluno in lista:
        if nome in aluno[0]:
            achei = True
            break
    return achei


alunos = [['matheus', 20],['maria', 19],['tomaz', 29],['lais', 40]]
if buscar(alunos, 'mari'):
    print('uhuuuu. achamos essa pessoa')
else:
    print('deu ruim. ta aqui nao')
