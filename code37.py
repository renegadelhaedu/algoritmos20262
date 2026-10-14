#questao 24 da lista de est de decisao

n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))

operacao = input('digite o símbolo da operaçao: ')
resultado = 0
if operacao == '+':
    resultado = n1 + n2
if operacao == '-':
    resultado = n1 - n2
if operacao == '*':
    resultado = n1 * n2
if operacao == '/':
    resultado = n1 / n2

if resultado % 2 == 0:
    print('par')
else:
    print('ímpar')

if resultado > 0:
    print('positivo')
if resultado < 0:
    print('negativo')

if resultado % 1 == 0:
    print('inteiro')
else:
    print('decimal')

