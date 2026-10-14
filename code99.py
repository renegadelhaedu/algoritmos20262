print('---Sistema do primeiro ano---')
alunos = ['enzo','nycole','joao pedro']
print(alunos)
print(alunos[0])
while True:
    print('\n---OPCOES---')
    print('1-cadastrar aluno')
    print('2-mostrar alunos')
    print('3-sair')
    op = int(input('Qual a sua opcao: '))
    if op == 1:
        nome = input('Qual o nome do aluno? ')
        alunos.append(nome)
        print('Pessoa inserida com sucesso!')
    elif op == 2:
        print(alunos)
    elif op == 3:
        break
    else:
        print('Opcao invalida!')

print('Programa finalizado com sucesso!')