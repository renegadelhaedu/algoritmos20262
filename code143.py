#4 tipos de funções
#tipo 4: sem parâmetros entrada, com retorno

def menu():
    print('MENU')
    print('1-cadastrar')
    print('2-listar')
    print('3-buscar')
    op = int(input('digite a opçao desejada: '))
    return op

opcao = menu()

