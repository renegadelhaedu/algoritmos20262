#main
import funcoesadm as adm
import funcoescliente as cli
import graficos as gr
import funfile as file

clientes = {2342:['renan','rua raminudo bocaiuva','83-298347']}
produtos = {0:['chip oi',20,90],1:['amd',10,50]}
vendas = [[1, 2342, 5]]
id_prod = 1
while True:
    opcao = adm.menu()
    if opcao == 1:
        id_prod += 1
        adm.cadastrar_produto(id=id_prod, prods=produtos)
    elif opcao == 2:
        cli.cadastrar_cliente(clientes)
    elif opcao == 3:
        saida_id = adm.buscar_produto(produtos)
        #se vier o id preenchido é pq o produto existe
        if saida_id:
            cpf = cli.verificar_usuario(clientes)
            qtde_vendida = adm.realizar_venda(vendas, saida_id, cpf)
            adm.diminuir_estoque(produtos, id_prod, qtde_vendida)
        else:
            #nao achou o produto
            adm.listar_produtos(produtos)
            id_escolhido = int(input('Digite o ID do produto que deseja comprar: '))
            if id_escolhido in produtos:
                cpf = cli.verificar_usuario(clientes)
                qtde_vendida = adm.realizar_venda(vendas, saida_id, cpf)
                adm.diminuir_estoque(produtos, id_prod, qtde_vendida)
    elif opcao == 4:
        gr.exibir_produtos(produtos)

    elif opcao == 5:
        file.listar_clientes()