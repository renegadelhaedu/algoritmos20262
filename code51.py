p1 = input('Telefonou para a vítima?')
p2 = input('Esteve no local do crime?')
p3 = input('Mora perto da vítima?')
p4 = input('Devia para a vítima?')
p5 = input('Já trabalhou com a vítima?')

soma = 0
if p1 == 'sim':
    soma = soma + 1
if p2 == 'sim':
    soma = soma + 1
if p3 == 'sim':
    soma = soma + 1
if p4 == 'sim':
    soma = soma + 1
if p5 == 'sim':
    soma = soma + 1

if soma == 2:
    print('suspeito')
if soma == 3 or soma == 4:
    print('cúmplice')
if soma == 5:
    print('assassino')
if soma < 2:
    print('nao tem nada com isso. livre de tudo')