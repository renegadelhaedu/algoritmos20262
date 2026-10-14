#string é um tipo de dado formado por uma cadeia de caracteres
#len() determina o tamanho de caracteres de uma string
nome = 'maria heloisa marques'

for ind in range(len(nome) - 1, -1, -1):
    print(nome[ind], end=' ')