op = -1
bandas = []
while op != 0:
    print('\n___FESTIVAL ROCK PB___')
    print('1-cadastrar banda')
    print('2-remover banda')
    print('3-listar bandas')
    print('0-SAIR')
    op = int(input('digite a opçao desejada: '))
    if op == 1:
        nome_banda = input('digite o nome da banda')
        bandas.append(nome_banda)
    elif op == 2:
        busca = input('digite o nome da banda para remover')

        ind = -1
        for i in range(len(bandas)):
            if busca == bandas[i]:
                ind = i
        if ind == -1:
            print('banda nao encontrada')
        else:
            bandas.pop(ind) #pop remove pelo índice
            print('banda removida com sucesso')


