
def salvar_cliente(cliente):
    with open('clientes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(cliente[0] + ';' + cliente[1] + ';' +cliente[2] + ';' +cliente[3] + '\n')

def listar_clientes():
    with open('clientes.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha)

def carregar_clientes(clientes):
    {2342: ['renan', 'rua raminudo bocaiuva', '83-298347']}
    with open('clientes.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha)