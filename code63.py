#faça um algoritmo na linguagem python que leia os 3 lados de um triângulo
#e verifique se ele é isosceles ou não

l1 = int(input('digite um numero: '))
l2 = int(input('digite um numero: '))
l3 = int(input('digite um numero: '))

if (l1 == l2 and l2 != l3) or (l1 == l3 and l2 != l3) or (l2 == l3 and l3 != l1):
    print('isosceles')
else:
    print('nao é isosceles')