#estrutura de repetição: while
#desenvolva um algoritmo em python que faça a leitura do numero
#dos candidatos (99,88). leia a votaçao para uma turma de 38 alunos
#ao final, compute os votos e dig
# a quem ganhou
v99 = 0
v88 = 0
i = 0

while i < 38:
    voto = int(input('vc vota no 99 ou 88'))
    if voto == 99:
        v99 = v99 + 1
    elif voto == 88:
        v88 = v88 + 1

    i = i + 1

if v88 > v99:
    print('a chapa do 88 ganhou')
elif v99 > v88:
    print('a chapa do 99 ganhou')
else:
    print('segundo turno pois deu empate')