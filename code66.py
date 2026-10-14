#Construa uma calculadora lendo os 2 números e a operação. mostre na tela os resultados.
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

operacao = input('-1 para soma \n'
                 '-2 para subtração \n'
                 '-3 para multiplicação \n'
                 '-4 para divisão \n'
                 '-5 para exponenciação \n'
                 '-6 para radiciação\n')
if operacao == '1':
    print('total:', v1 + v2)
elif operacao == '2':
    print('total:', v1 - v2)
elif operacao == '3':
    print('total:', v1 * v2)
elif operacao == '4':
    print('total:', v1 / v2)
elif operacao == '5':
    print('total:', v1 ** v2)
elif operacao == '6':
    print('total:', v1 ** (1/v2))
else:
    print('operacao invalida')