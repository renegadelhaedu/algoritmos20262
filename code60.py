#questao 6
n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite um numero inteiro: '))
n3 = int(input('digite um numero inteiro: '))

if n1 > n2 and n1 > n3:
    print('n1')
elif n2 > n1 and n2 > n3:
    print('n2')
elif n3 > n1 and n3 > n2:
    print('n3')
else:
    print('deu empate')



