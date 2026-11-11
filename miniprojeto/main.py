#main
import funcoesadm as adm
import funcoescliente as cli

clientes = {2342:['renan','rua raminudo bocaiuva','83-298347']}
produtos = {0:['chip oi',20,90]}
vendas = [[1, 2342, 5]]
id_prod = 0
while True:
    opcao = adm.menu()
    if opcao == 1:
        id_prod += 1
        adm.cadastrar_produto(produtos, id_prod)
    elif opcao == 2:
        cli.cadastrar_cliente(clientes)
    elif opcao == 3:
        saida_id = adm.buscar_produto(produtos)
        if saida_id:
            cpf = cli.verificar_usuario(clientes)
            qtde_vendida = adm.realizar_venda(vendas, saida_id, cpf)
            adm.diminuir_estoque(produtos, id_prod, qtde_vendida)