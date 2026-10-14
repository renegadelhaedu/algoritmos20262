'''questao 16 da lista de decisao
'''
a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))
if a == 0:
    print('nao é equacao do segundo grau')
else:
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print('nao possui raizes reais')
    if delta == 0:
        x = (-b + delta ** (1/2)) / (2 * a)
        print('essa é a raiz real:', x)
    if delta > 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print('raiz real positivo:', x1)
        print('raiz real negativo:', x2)