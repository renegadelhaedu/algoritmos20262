#4 tipos de funções
#tipo 2: com parâmetros entrada, sem retorno
#crie uma função que receba um número correspondente a um
#percentual e aplique um desconto num produto de 4000 mil
#a funçao deve exibir o valor na tela

def aplicar_desconto(valor):
    desconto = 4000 * (valor / 100)
    final = 4000 - desconto
    print(f'pra vc, meu amigo, fica só {final}')

aplicar_desconto(2)
