#primo ou nao: faça um algoritmo que mostre
# numeros primos entre 3 e 1000000
qtde = 0
num = int(input('digite um numero: '))
for i in range(2,num):
    if num % i == 0:
        qtde = qtde + 1

if qtde == 0:
    print('é primo')
else:
    print('nao é primo')

