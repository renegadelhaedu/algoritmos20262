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


def buscar_produto(prods):
    busca = input('Digite o nome do produto: ')
    resposta = None
    for id, prod in prods.items():
        if busca == prod[0]:
            resposta = id
            break
    return resposta

def listar_produtos(prods):
    for id,prod in prods.items():
        print(f'ID:{id} - Nome:{prod[0]} - Preco:{prod[1]} - Quantidade:{prod[2]}')

def realizar_venda(vendas, id_prod, cpf):
    qtde = int(input('Digite a quantidade em unidades do produto: '))
    vendas.append([id_prod, cpf, qtde])
    print('Venda realizada com sucesso!\n')