#funcoes1

def menu():
    print('MENU')
    print('1-cadastrar')
    print('2-listar')
    print('3-buscar')
    op = int(input('digite a opçao desejada: '))
    return op

def cadastrar(lista, nome, idade):
    lista.append([nome, idade])

def listar(lista):
    for aluno in lista:
        print(f'Nome: {aluno[0]}, Idade: {aluno[1]}')
