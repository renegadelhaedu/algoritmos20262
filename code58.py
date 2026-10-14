#questao 14 lista decisao

n1 = float(input('digite seu primeiro valor: '))
n2 = float(input('digite seu segundo valor: '))
media = (n1 + n2) / 2
if media >= 9 and media <= 10:
    print('conceito A')
elif media >= 7.5:
    print('conceito B')
elif media >= 6:
    print('conceito C')
elif media >= 4:
    print('conceito D')
else:
    print('conceito E')