#sistema de cadastro de eventos

eventos = {}
users = {}
op = 99
while op != 0:
    print('\n1-fazer login')
    print('2-cadastrar usuário')
    print('0-sair')

    op = int(input('digite opçao: '))
    if op == 2:
        nome = input('digite seu nome: ')
        login = input('digite seu login: ')
        senha = input('digite sua senha: ')
        users[login] = [nome, senha]
        print('usuario cadastrado com sucesso')

    elif op == 1:
        login = input('digite seu login: ')
        senha = input('digite sua senha: ')
        if login not in users:
            print('usuário inexistente')
        else:
            logado = []#se continuar vazio é pq nao achei ninguem
            for login_user , dados_user in users.items():
                if login == login_user and senha == dados_user[1]:
                    logado = dados_user
                    break
            if len(logado) != 0:
                #login e senha deram certo
                op2 = 99
                while op2 != 0:
                    print('______MENU_____')
                    print('1-cadastrar evento')
                    print('2-participar de evento')
                    print('3-exibir eventos que criei')
                    print('0-sair')
                    op2 = int(input('Digite a opçao desejada: '))
                    if op2 == 1:
                        nome = input('digite nome do evento: ')
                        qtde_max = int(input('digite quantidade de maximos do evento: '))
                        while qtde_max <= 0:
                            qtde_max = int(input('digite quantidade de maximos do evento: '))
                        code = int(input('digite code: '))
                        while code in eventos:
                            code = int(input('digite code: '))
                        descr = input('informe a descriçao: ')
                        valor = float(input('informe o valor: '))
                        eventos[code] = [nome, qtde_max, descr, valor, [], login]
                        print('evento cadastrado com sucesso')

                    elif op2 == 2:
                        nome = input('digite o nome do evento: ')
                        lista_busca = []
                        for code, dados in eventos.items():
                            if nome in dados[0]:
                                lista_busca.append([code,dados[0]])
                        if len(lista_busca) > 0:
                            for evento in lista_busca:
                                print(f'Código:{evento[0]} - Nome: {evento[1]}')
                            codigo_escolh = int(input('Digite o código do evento desejado: '))
                            #estou acessando a lista de inscritos do evento e me inscrevendo
                            eventos[codigo_escolh][4].append(login)
                            print(eventos[codigo_escolh])
                        else:
                            print('nao foi encontrado nenhum evento com este nome')

                    elif op2 == 3:
                        for code, dados in eventos.items():
                            #mostra quem é o dono do evento e confere
                            if login == dados[5]:
                                print(f'{code} - {dados}')