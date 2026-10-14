adms = [["higor", "123", True]]
clientes = [["caio", "123", False],["maria", "456", False]]
user_logado = []
animais_cadastrados = []
produtos_cadastrados = []
ListaTipos = []
ListaStatus = []
index = 0
index2 = -1
logado = False
agendamentos = []
estoque = []
racao = []
pedidos_compra = []

while True:
    print("     *****MENU*****\n 1 - Cadastrar\n 2 - Login\n 0 - Encerrar")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        verif = int(
            input("Deseja criar um conta de ADM ou Cliente?(1 - ADM, 2 - Cliente)")
        )
        if verif == 1:
            login = input("Crie seu nome de usuario: ")
            senha = input("Crie sua senha: ")
            adms.append([login, senha, True])
        elif verif == 2:
            login = input("Crie seu nome de usuario: ")
            senha = input("Crie sua senha: ")
            clientes.append([login, senha, False])
        continue

    elif opcao == 2:
        verif = int(input("Deseja entrar como ADM ou Cliente?(1 - ADM, 2 - Cliente)"))

        if verif == 1:
            login = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha de acesso: ")
            for adm in adms:
                if login == adm[0] and senha == adm[1]:
                    logado = True
                    user_logado = [[adm[0], adm[2]]]
                    break
            if not logado:
                print("Login ou senha incorretos...")
                continue

        elif verif == 2:
            login = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha de acesso: ")
            for cliente in clientes:
                if login == cliente[0] and senha == cliente[1]:
                    logado = True
                    user_logado = [[cliente[0], cliente[2]]]
                    break
            if not logado:
                print("Login ou senha incorretos...")
                continue
    elif opcao == 0:
        break

    if logado == True:
        print("Login efetuado com sucesso")

    if user_logado and user_logado[0][1] == True:
        while True:
            print(
                f'{"\n"*4}Bem-vindo, {user_logado[0][0]} \n     *****MENU*****\n 1 - Gerenciar Rebanho\n 2 - Gerenciar Produção e Derivados\n 3 - Gerenciar Estoque de Ração\n 4 - Visualizar Pedidos de Compra\n 0 - Menu de Cadastro\n'
            )
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                while True:
                    print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar
4 - Remover Animais
0 - Voltar""")
                    controle = int(input("Digite a opção desejada: "))
                    if controle == 0:
                        print("Voltando ao menu")
                        break

                    elif controle == 1:
                        Tipo = str(input("Qual o tipo de animal?\n")).upper()
                        indetificacao = int(input("Qual o número de indentificação?\n"))
                        status = input("Qual o status do animal?\n").upper()
                        animais_cadastrados.append([Tipo, indetificacao, status])

                        venda = input(
                            "Deseja colocar esse animal à venda? (S - Sim / N - Não) "
                        ).upper()
                        if venda == "S":
                            preco = float(input("Qual o preço do animal? R$ "))
                            estoque.append(["ANIMAL", indetificacao, Tipo, preco])

                    elif controle == 2:
                        while True:
                            print(
                                f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Busca por ID do animal\n 2 - Buscar por Tipo dos animais\n 3 - Buscar por status\n 4 - Verificar animais à venda\n 0 - Sair da busca\n'
                            )
                            opcao = int(input("Digite a opção desejada: "))

                            if opcao == 1:
                                busca = input("Digite o número do animal: ")
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][1]:
                                        index = i
                                        break
                                print(f"O seu animal {animais_cadastrados[index]}")

                            elif opcao == 2:
                                busca = str(input("Digite o Tipo do animal: ")).upper()
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][0]:
                                        ListaTipos.append(animais_cadastrados[i])
                                print(f"Os seus {busca}s são:\n{ListaTipos}")
                                print(f"Você tem {len(ListaTipos)} {busca}s")
                                ListaTipos.clear()

                            elif opcao == 3:
                                busca = str(
                                    input(
                                        "Digite o Status do animal que deseja buscar: "
                                    )
                                ).upper()
                                for i in range(len(animais_cadastrados)):
                                    if busca == animais_cadastrados[i][2]:
                                        ListaStatus.append(animais_cadastrados[i])
                                print(
                                    f"Você tem {len(ListaStatus)} animais em: {busca}"
                                )
                                print(
                                    f"Os seus animais em {busca}s são:\n{ListaStatus}"
                                )
                                ListaStatus.clear()

                            elif opcao == 4:
                                print("Animais à venda:\n")
                                for i in range(len(estoque)):
                                    if "ANIMAL" == estoque[i][0]:
                                        ListaStatus.append(estoque[i])
                                print(f"Você tem {len(ListaStatus)} animais à VENDA")
                                print(
                                    f"Os seus animais à venda são:\n{ListaStatus}",
                                    end="\n",
                                )
                                ListaStatus.clear()

                            elif opcao == 0:
                                print("Encerrando busca.")
                                break
                            else:
                                print("Opçao inválida")
                                continue

                    elif controle == 3:
                        busca = int(
                            input(
                                "Qual o número de identificação do animal que deseja atualizar?\n"
                            )
                        )
                        for i in range(len(animais_cadastrados)):
                            if busca == animais_cadastrados[i][1]:
                                index = i
                                break
                        index2 = -1
                        for i in range(len(estoque)):
                            if busca == estoque[i][1]:
                                index2 = i
                                break
                        if index2 > -1:
                            a = input(
                                f"O status atual do animal é: {animais_cadastrados[index][2]}, e seu valor no estoque é: {estoque[index2][3]}. Deseja Atulizar?(S - Sim N - Não)"
                            ).upper()
                            if a == "S":
                                b = input("Digite o status atual do animal: ").upper()
                                c = input("Qual o preço do animal: ")
                                estoque[index2][3] = c
                                animais_cadastrados[index][2] = b
                            else:
                                print("Retornando ao menu")
                                break
                        else:
                            a = input(
                                f"O status atual do animal é: {animais_cadastrados[index][2]}. Deseja Atulizar?(S - Sim N - Não)"
                            ).upper()
                            if a == "S":
                                b = input("Digite o status atual do animal: ").upper()
                                animais_cadastrados[index][2] = b
                            else:
                                print("Retornando ao menu")
                                break

                    elif controle == 4:
                        busca = int(
                            input(
                                "Qual o número de identificação do animal que deseja remover?\n"
                            )
                        )
                        for i in range(len(animais_cadastrados)):
                            if busca == animais_cadastrados[i][1]:
                                index = i
                                break
                        a = input(
                            f"Os dados do animal é: {animais_cadastrados[index]}. Deseja Remover?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            animais_cadastrados.pop(index)
                            for i in range(len(estoque)):
                                if estoque[i][1] == busca:
                                    estoque.pop(i)
                                    break
                        elif a == "N":
                            print("Retornando ao menu")
                            break
                    elif controle == 0:
                        break
                    else:
                        print("Opção inválida!!!")
                        continue

            elif opcao == 2:
                while True:
                    print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar Itens
4 - Remover Itens
0 - Voltar""")
                    controle = int(input("Digite a opção desejada: "))
                    if controle == 0:
                        print("Voltando ao menu")
                        break

                    elif controle == 1:
                        Tipo = str(input("Qual o tipo de Produto?\n")).upper()
                        Quantidade = int(
                            input("Qual a quantidade do Produto no estoque?\n")
                        )
                        status = input("Qual o status do produto?\n").upper()
                        produtos_cadastrados.append([Tipo, Quantidade, status])

                        venda = input(
                            "Deseja colocar esse produto à venda no estoque? (S - Sim / N - Não) "
                        ).upper()
                        if venda == "S":
                            preco = float(input("Qual o preço do produto? R$ "))
                            estoque.append(["PRODUTO", Tipo, Quantidade, preco])

                    elif controle == 2:
                        while True:
                            print(
                                f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Busca por Nome do Produto\n 2 - Buscar por status\n 0 - Sair da busca\n'
                            )
                            opcao = int(input("Digite a opção desejada: "))

                            if opcao == 1:
                                busca = input("Digite o nome do Produto: ").upper()
                                achou_estoque = False
                                for i in range(len(estoque)):
                                    if busca == estoque[i][1]:
                                        index = i
                                        achou_estoque = True
                                        break
                                if achou_estoque:
                                    print(
                                        f"A situação do seu produto no estoque: {estoque[index]}"
                                    )
                                else:
                                    for i in range(len(produtos_cadastrados)):
                                        if busca == produtos_cadastrados[i][0]:
                                            index = i
                                            break
                                    print(
                                        f"A situação do seu produto: {produtos_cadastrados[index]}"
                                    )

                            elif opcao == 2:
                                print("Exibindo estoque:\n")
                                for i in range(len(estoque)):
                                    if "PRODUTO" == estoque[i][0]:
                                        ListaStatus.append([estoque[i]])
                                print(
                                    f"Você tem {len(ListaStatus)} produtos em seu estoque"
                                )
                                print(
                                    f"Os seus produtos em estoque são:\n{ListaStatus}"
                                )
                                ListaStatus.clear()

                            elif opcao == 0:
                                print("Encerrando busca.")
                                break
                            else:
                                print("Opçao inválida")
                                continue

                    elif controle == 3:
                        busca = input(
                            "Qual o nome do produto que deseja atualizar?\n"
                        ).upper()
                        for i in range(len(produtos_cadastrados)):
                            if busca == produtos_cadastrados[i][0]:
                                index = i
                                break

                        index2 = -1
                        for i in range(len(estoque)):
                            if busca == estoque[i][1]:
                                index2 = i
                                break

                        if index2 > -1:
                            a = input(
                                f"A quantidade atual do produto é: {estoque[index2][2]}, e seu valor no estoque é: R$ {estoque[index2][3]}. Deseja Atualizar?(S - Sim N - Não) "
                            ).upper()
                            if a == "S":
                                b = int(
                                    input(
                                        "Digite quanto foi adicionado ou retirado do produto: "
                                    )
                                )
                                estoque[index2][2] += b
                                produtos_cadastrados[index][1] += b
                                c = input("Qual o novo preço do produto? R$ ")
                                estoque[index2][3] = c
                        else:
                            a = input(
                                f"A quantidade atual do produto é: {produtos_cadastrados[index][1]}. Deseja Atulizar?(S - Sim N - Não)"
                            ).upper()
                            if a == "S":
                                b = int(
                                    input(
                                        "Digite quanto foi adicionado ou retirado do produto: "
                                    )
                                )
                                produtos_cadastrados[index][1] += b
                            elif a == "N":
                                print("Retornando ao menu")
                                break

                    elif controle == 4:
                        busca = input(
                            "Qual o nome do produto que deseja remover?\n"
                        ).upper()
                        for i in range(len(produtos_cadastrados)):
                            if busca == produtos_cadastrados[i][0]:
                                index = i
                                break
                        a = input(
                            f"Os dados do produto são: {produtos_cadastrados[index]}. Deseja Remover?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            produtos_cadastrados.pop(index)
                            for i in range(len(estoque)):
                                if estoque[i][1] == busca:
                                    estoque.pop(i)
                                    break
                        elif a == "N":
                            print("Retornando ao menu")
                            break
                    else:
                        print("Opção inválida!!!")
                        continue

            elif opcao == 3:
                while True:
                    print(
                        f'{"\n"*4}Gerenciar Ração, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Cadastrar uma ração\n 2 - Vizualizar Estoque\n 3 - Atulizar estoque\n 0 - Sair\n'
                    )
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao == 1:
                        nome = str(input("Qual o Nome da raçao?\n")).upper()
                        Tipo = str(input("Qual o tipo da raçao?\n")).upper()
                        Quantidade = int(input("Qual a quantidade de ração(em kg)?\n"))
                        racao.append([nome, Tipo, Quantidade])
                    elif opcao == 2:
                        for i in range(len(racao)):
                            print(
                                f"A sua ração {racao[i][0]} de {racao[i][1]} tem {racao[i][2]}kg restantes."
                            )
                    elif opcao == 3:
                        busca = input(
                            "Qual o nome do produto que deseja atualizar?\n"
                        ).upper()
                        for i in range(len(racao)):
                            if busca == racao[i][0]:
                                index = i
                                break
                        a = input(
                            f"A quantidade atual da ração {racao[index][0]} é: {racao[index][2]}. Deseja Atulizar?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            b = int(
                                input(
                                    "Digite quanto foi adicionado ou retirado de ração: "
                                )
                            )
                            racao[index][2] += b
                        elif a == "N":
                            print("Retornando ao menu")
                            break
                    elif opcao == 0:
                        break

            elif opcao == 4:
                while True:
                    print(
                        f'{"\n"*4}Pedidos de Compra \n     *****MENU*****\n 1 - Visualizar seus pedidos pendentes\n 2 - Validar um pedido\n 0 - Voltar\n'
                    )
                    controle = int(input("Digite a opção desejada: "))

                    if controle == 0:
                        break

                    elif controle == 1:
                        pedido_encontrado = False
                        for i in range(len(pedidos_compra)):
                            print(
                                f"[{i}] Cliente: {pedidos_compra[i][0]} | Produto: {pedidos_compra[i][1]} | Quantidade: {pedidos_compra[i][2]} | Prazo: {pedidos_compra[i][3]} | Situação: {pedidos_compra[i][4]}"
                            )
                            pedido_encontrado = True
                        if not pedido_encontrado:
                            print("Nenhum pedido de compra registrado.")

                    elif controle == 2:
                        if len(pedidos_compra) == 0:
                            print("Nenhum pedido para validar.")
                            continue

                        for i in range(len(pedidos_compra)):
                            if pedidos_compra[i][4] == "PENDENTE":
                                print(
                                    f"[{i}] Cliente: {pedidos_compra[i][0]} | Produto: {pedidos_compra[i][1]} | Quantidade: {pedidos_compra[i][2]} | Prazo: {pedidos_compra[i][3]}"
                                )

                        posicao_pedido = int(
                            input("\nDigite o número do pedido que deseja validar: ")
                        )

                        if posicao_pedido < 0 or posicao_pedido >= len(pedidos_compra):
                            print("Pedido inválido.")
                            continue

                        resposta = input(
                            f"Deseja APROVAR o pedido de {pedidos_compra[posicao_pedido][1]} do cliente {pedidos_compra[posicao_pedido][0]}? (S - Sim / N - Não) "
                        ).upper()

                        if resposta == "S":
                            pedidos_compra[posicao_pedido][4] = "APROVADO"
                            print("Pedido aprovado com sucesso!")
                        elif resposta == "N":
                            pedidos_compra[posicao_pedido][4] = "RECUSADO"
                            print("Pedido recusado.")
                    else:
                        print("Opção inválida!!!")
                        continue
            elif opcao == 3:
                while True:
                    print(
                        f'{"\n"*4}O que você deseja buscar, {user_logado[0][0]}? \n     *****MENU*****\n 1 - Cadastrar uma ração\n 2 - Vizualizar Estoque\n 3 - Atulizar estoque 0 - Sair da busca\n'
                    )
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao == 1:
                        nome = str(input("Qual o Nome da raçao?\n")).upper()
                        Tipo = str(input("Qual o tipo da raçao?\n")).upper()
                        Quantidade = int(input("Qual a quantidade de ração(em kg)?\n"))
                        racao.append([nome, Tipo, Quantidade])
                    elif opcao == 2:
                        for i in range(len(racao)):
                            print(
                                f"A sua ração {racao[i][0]} de {racao[i][1]}tem {racao[i][2]}kg restantes."
                            )
                    elif opcao == 3:
                        busca = input(
                            "Qual o nome do produto que deseja atualizar?\n"
                        ).upper()
                        for i in range(len(racao)):
                            if busca == racao[i][0]:
                                index = i
                                break
                        a = input(
                            f"A quantidade atual da ração {racao[index][0]} é: {racao[index][2]}. Deseja Atulizar?(S - Sim N - Não)"
                        ).upper()
                        if a == "S":
                            b = int(
                                input(
                                    "Digite quanto foi adicionado ou retirado de ração: "
                                )
                            )
                            racao[index][2] += b
                        elif a == "N":
                            print("Retornando ao menu")
                            break
            elif opcao == 0:
                print("Retomando...")
                logado = False
                user_logado = []
                break

    elif user_logado and user_logado[0][1] != True and logado == True:
        while True:
            print(
                f'{"\n"*4}Bem-vindo, {user_logado[0][0]} \n     *****MENU CLIENTE*****\n 1 - Comprar\n 2 - Visualizar Estoque\n 3 - Agendar Retirada/Transporte\n 4 - Ver Meus Agendamentos\n 5 - Fazer Pedido de Compra\n 6 - Ver Meus Pedidos\n 0 - Sair\n'
            )
            opcao_cliente = int(input("Digite a opção desejada: "))

            if opcao_cliente == 1:
                if len(estoque) == 0:
                    print("Nenhum item disponível no momento.")
                    continue

                print("\n===== ITENS DISPONÍVEIS =====")
                for posicao_item in range(len(estoque)):
                    print(
                        f"[{posicao_item}] {estoque[posicao_item][0]} | {estoque[posicao_item][2]} | Preço: R$ {estoque[posicao_item][3]}"
                    )

                posicao_escolhida = int(
                    input("\nDigite o número do item que deseja comprar: ")
                )

                if posicao_escolhida < 0 or posicao_escolhida >= len(estoque):
                    print("Item inválido.")
                    continue

                confirmacao_compra = input(
                    f"Confirmar compra de {estoque[posicao_escolhida][2]}? (S - Sim / N - Não) "
                ).upper()

                if confirmacao_compra == "S":
                    print(
                        f"Compra realizada com sucesso! Você comprou {estoque[posicao_escolhida][2]}."
                    )
                    estoque.pop(posicao_escolhida)
                else:
                    print("Compra cancelada.")

            elif opcao_cliente == 2:
                print("\n===== ITENS DISPONÍVEIS =====")
                if len(estoque) == 0:
                    print("Nenhum item disponível no momento.")
                    continue
                for posicao_item in range(len(estoque)):
                    print(
                        f"[{posicao_item}] {estoque[posicao_item][0]} | {estoque[posicao_item][2]} | Preço: R$ {estoque[posicao_item][3]}"
                    )

            elif opcao_cliente == 3:
                print("\n===== AGENDAR RETIRADA/TRANSPORTE =====")

                if len(estoque) == 0:
                    print("Nenhum item disponível no estoque para agendar retirada.")
                    continue

                print("Itens disponíveis para retirada:")
                for posicao_item in range(len(estoque)):
                    print(
                        f"[{posicao_item}] {estoque[posicao_item][0]} | {estoque[posicao_item][2]} | Preço: R$ {estoque[posicao_item][3]}"
                    )

                posicao_agendamento = int(
                    input("\nDigite o número do item que deseja agendar a retirada: ")
                )

                if posicao_agendamento < 0 or posicao_agendamento >= len(estoque):
                    print("Item inválido.")
                    continue

                item_para_retirar = f"{estoque[posicao_agendamento][2]} ({estoque[posicao_agendamento][0]})"

                data_retirada = input("Informe a data para retirada (ex: 25/06/2025): ")
                horario_retirada = input(
                    "Informe o horário para retirada (ex: 14:00): "
                )

                confirmacao_agendamento = input(
                    f"\nConfirmar agendamento?\n  Item: {item_para_retirar}\n  Data: {data_retirada}\n  Horário: {horario_retirada}\n(S - Sim / N - Não) "
                ).upper()

                if confirmacao_agendamento == "S":
                    agendamentos.append(
                        [
                            user_logado[0][0],
                            item_para_retirar,
                            data_retirada,
                            horario_retirada,
                        ]
                    )
                    print(
                        "Agendamento realizado com sucesso! O caminhão estará na fazenda na data e horário informados."
                    )
                else:
                    print("Agendamento cancelado.")

            elif opcao_cliente == 4:
                print("\n===== MEUS AGENDAMENTOS =====")
                agendamento_encontrado = False
                for agendamento_atual in agendamentos:
                    if agendamento_atual[0] == user_logado[0][0]:
                        print(
                            f"Item: {agendamento_atual[1]} | Data: {agendamento_atual[2]} | Horário: {agendamento_atual[3]}"
                        )
                        agendamento_encontrado = True
                if not agendamento_encontrado:
                    print("Você não possui agendamentos.")

            elif opcao_cliente == 5:
                print("\n===== FAZER PEDIDO DE COMPRA =====")
                nome_produto_pedido = input(
                    "Qual o nome do produto que deseja pedir? "
                ).upper()
                quantidade_pedido = int(input("Qual a quantidade desejada? "))
                prazo_pedido = input("Para quando você precisa? (ex: 30/06/2025): ")

                confirmacao_pedido = input(
                    f"\nConfirmar pedido?\n  Produto: {nome_produto_pedido}\n  Quantidade: {quantidade_pedido}\n  Prazo: {prazo_pedido}\n(S - Sim / N - Não) "
                ).upper()

                if confirmacao_pedido == "S":

                    pedidos_compra.append(
                        [
                            user_logado[0][0],
                            nome_produto_pedido,
                            quantidade_pedido,
                            prazo_pedido,
                            "PENDENTE",
                        ]
                    )
                    print(
                        "Pedido realizado com sucesso! Aguarde a validação do administrador."
                    )
                else:
                    print("Pedido cancelado.")

            elif opcao_cliente == 6:
                print("\n===== MEUS PEDIDOS DE COMPRA =====")
                pedido_encontrado = False
                for pedido_atual in pedidos_compra:
                    if pedido_atual[0] == user_logado[0][0]:
                        print(
                            f"Produto: {pedido_atual[1]} | Quantidade: {pedido_atual[2]} | Prazo: {pedido_atual[3]} | Situação: {pedido_atual[4]}"
                        )
                        pedido_encontrado = True
                if not pedido_encontrado:
                    print("Você não possui pedidos de compra.")

            elif opcao_cliente == 0:
                print("Saindo...")
                logado = False
                user_logado = []
                break
            else:
                print("Opção inválida!")
                continue