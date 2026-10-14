#estrutura de repetição: while
#desenvolva um algoritmo em python que pergunte para diversos
#alunos se eles estao gostando ou nao da disciplina de
#algoritmos (sim ou nao). o programa deve mostrar quantos
#votos sim/nao tiveram. se o aluno digitar fim, o programa
#para a leitura e mostra a votaçao final.
sim = 0
nao = 0
outros = 0
resposta = ''
while resposta != 'fim':
    resposta = input('voce está gostando de programação?').lower()
    if 'sim' in resposta:
        sim += 1
    elif 'não' in resposta:
        nao += 1
    else:
        outros += 1

if sim > nao:
    print('a maioria da sala está gostando de programação ', sim)
elif nao > sim:
    print('deu ruim. nao tao  gostando de programação ', nao)
else:
    print('meio a meio')







