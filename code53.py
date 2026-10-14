'''desenvolva um algoritmo em python que leia
o valor do litro de alcool e o valor do litro de gasolina
o algoritmo deve informar qual combustível compensa
abastecer.'''
alc = float(input('qual o valor do alcool?'))
gas = float(input('qual o valor da gasolina?'))

if alc/gas < 0.7:
    print('abasteça com alcool')
else:
    print('abasteça com gasolina')