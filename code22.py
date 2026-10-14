#questao 2

valor = float(input('qual o valor do produto? '))
desconto = float(input('qual o desconto do produto? '))

final = valor -(valor * (desconto / 100))

print('voce vai pagar ', final, 'reais')