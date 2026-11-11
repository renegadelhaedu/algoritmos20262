#principal
import code145_pacote_funcoes1 as f1
import code145_pacote_funcoes2 as f2

lista_alunos = []

while True:
    resposta = f1.menu()
    if resposta == 1:
        nome = input('Digite o nome do cadastro: ')
        idade = input('Digite a idade do cadastro: ')
        f1.cadastrar(lista_alunos, nome, idade)
    elif resposta == 2:
        f1.listar(lista_alunos)
    elif resposta == 3:
        f2.contido(lista_alunos)


