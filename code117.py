lanches = dict()
op = 99
while op != 0:
    print('1-cadastrar')
    print('2-listar')
    print('3-buscar prof')
    print('0-sair')
    op = int(input('digita a opcao'))
    if op == 1:
        nome = input('Diga o nome do lanche: ')
        preco = float(input('qual o preco? '))
        lanches[nome] = preco
    elif op == 2:
        for nome, preco  in lanches.items():
            print(f'{nome}: {preco}')

    elif op == 3:
        busca = input('buscar lanche: ')
        for nome  in lanches:
            if busca in nome:
                print(f'{nome}: {lanches[nome]}')
