#escopo local e global
#3 regra: estruturas de dados modificadas em escopo local se alteram no global
alunos = ['mateus lucas','arthur sabino']
def mudar_ordem(lista):
    aux = lista[0]
    lista[0] = lista[1]
    lista[1] = aux

print(alunos)
mudar_ordem(alunos)
print(alunos)