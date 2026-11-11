#adm

def menu():
    print('-'*40)
    print('         MENU')
    print('-'*40)
    print('1-cadastrar produto')
    print('2-cadastrar cliente')
    print('3-realizar venda')
    op = int(input('digite a opcao desejada: '))
    return op

def cadastrar_produto(prods, id):
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    qtde = int(input('Digite a quantidade de produtos: '))
    prods[id] = [nome, preco, qtde]
    print('Produto cadastrado com sucesso!\n')
