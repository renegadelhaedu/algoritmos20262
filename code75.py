#construa um algoritmo em python que consiga ler 10 numeros
#informados pelo usuário. O código deve ao final informar a
#quantidade de números pares e ímpares.

contador = 1
par = 0
impar = 0
while contador <= 10:
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('a quantidade de números pares é ', par)
print('a quantidade de números impares é ', impar)