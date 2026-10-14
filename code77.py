opcao = 99

while True:
    print('------------MENU-----------')
    print('[1] para cadastrar pacientes')
    print('[2] para buscar pacientes')
    print('[3] para remover pacientes')
    print('[0] para sair')
    opcao = int(input('digite sua opcao: '))
    if opcao == 0:
        break
    elif opcao == 1:
        print('cadastrar pacientes')
    elif opcao == 2:
        print('buscar pacientes')
    elif opcao == 3:
        print('remover pacientes')

