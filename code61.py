#faça um algoritmo em python que verifique se o nome digitado
#pelo usuário corresponde a uma das seguintes opções: ruim, bom, ótimo
#para as seguintes perguntas:
#
#você gostou das aulas de calculo 1?
#você gostou das aulas de AoC?
#você gostou das aulas de Ingles?
#você gostou das aulas de portugues?

#o sistema deve verificar qual a nota média que o aluno deu para o semestre
#letivo.

p1 = input('você gostou das aulas de algoritmos?')
p2 = input('você gostou das aulas de calculo 1?')
p3 = input('você gostou das aulas de Aoc?')
p4 = input('você gostou das aulas de ingles?')
p5 = input('você gostou das aulas de portugues?')
soma = 0
if p1 == 'ruim':
    soma = soma + 3
elif p1 == 'bom':
    soma = soma + 7
else:
    soma = soma + 10

if p2 == 'ruim':
    soma = soma + 3
elif p2 == 'bom':
    soma = soma + 7
else:
    soma = soma + 10

if p3 == 'ruim':
    soma = soma + 3
elif p3 == 'bom':
    soma = soma + 7
else:
    soma = soma + 10

if p4 == 'ruim':
    soma = soma + 3
elif p4 == 'bom':
    soma = soma + 7
else:
    soma = soma + 10

if p5 == 'ruim':
    soma = soma + 3
elif p5 == 'bom':
    soma = soma + 7
else:
    soma = soma + 10

media = soma / 5

print('a média geral do semestre foi ', media)