#cliente

def cadastrar_cliente(clientes):
    cpf = input('Digite o CPF do cliente: ')
    while not verificar_cpf_valido(clientes, cpf):
        cpf = input('CPF já cadastrado. Digite outro CPF do cliente: ')
    nome = input('Digite o nome do cliente: ')
    endereco = input('DIgite o endereco do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    clientes[cpf] = [nome, endereco, telefone]
    print('Cliente cadastrado com sucesso!\n')

def verificar_cpf_valido(clientes, cpf):
    if cpf not in clientes:
        return True
    else:
        return False

def verificar_usuario(clientes):
    cpf = input('Digite o cpf do cliente: ')
    if cpf in clientes:
        return cpf
    else:
        return None
