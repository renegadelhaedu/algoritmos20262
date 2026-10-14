#primo ou nao: faça um algoritmo que mostre
# numeros primos entre 3 e 1000000
for num in range(3,10001):
    qtde = 0
    for i in range(2,num):
        if num % i == 0:
            qtde = qtde + 1

    if qtde == 0:
        print(num)
