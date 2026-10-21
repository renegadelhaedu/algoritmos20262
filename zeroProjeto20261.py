usuario_achado = []#sldkfjlkdjfklsdjflksdlf
usuarios = [["Caio" , "caio=123" , False] , ["Higor" , "higor123" , True]]
usuario_logado = []
while True:
    print(" 1 - LOGIN \n 2 - CADASTRAR USUARIO \n 0 - SAIR")
    op = int(input("-> "))

    if op == 1:
        user_nome = input("Digite seu nome: ")
        user_senha = input("Digite sua senha: ")

        for usuario in usuarios:
            if usuario[0] == user_nome and usuario[1] == user_senha:
                usuario_achado = usuario
                break

        if len(usuario_achado) > 0:
            print("Login Efetuado com Sucesso")
        else:
            print("Senha ou usuario inválidas")

    elif op == 2:
        while True:
            print("Você ira cadastrar um ADM ou CLIENTE? [ 1 - ADM ] [ 2 - CLIENTE ]")
            verify = int(input("-> "))
            if verify == 1:
                regis_nome = input("Digite seu nome: ")
                regis_senha = input("Digite sua senha: ")

                usuarios.append([regis_nome, regis_senha , True])

                print("USUARIO CADASTRADO COM SUCESSO.")
                break
            if verify == 2:
                regis_nome = input("Digite seu nome: ")
                regis_senha = input("Digite sua senha: ")

                usuarios.append([regis_nome, regis_senha, False])

                print("USUARIO CADASTRADO COM SUCESSO.")
                break
    elif op == 0:
        print("Saindo...")
        break