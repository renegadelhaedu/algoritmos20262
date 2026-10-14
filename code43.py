'''
o professor de cálculo 1, flavio, pediu para você construir
um algoritmo em python para receber do usuário os 3 lados de
um triângulo. o programa deve informar se o triângulo é
equilátero ou não.
'''
l1 = int(input('primeiro lado: '))
l2 = int(input('segundo lado: '))
l3 = int(input('terceiro lado: '))
if l1 == l2 and l2 == l3:
    print('é sim equilatero')
else:
    print('NAO é equilatero')
