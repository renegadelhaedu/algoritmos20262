#4 tipos de funções
#tipo 2: com parâmetros entrada, sem retorno
#crie uma função que receba um número correspondente a um
#percentual e o valor do produto. aplique um desconto num produto
#a funçao deve exibir o valor na tela

def aplicar_desconto(percentual, valor_prod, nome):
    desconto = valor_prod * (percentual / 100)
    final = valor_prod - desconto
    print(f'pra vc, {nome}, fica só {final}')

desco = float(input('digite o valor do desconto: '))
valor = float(input('digite o valor do produto: '))
cliente =  input('digite o nome do cliente: ')
aplicar_desconto(desco, valor, cliente)
