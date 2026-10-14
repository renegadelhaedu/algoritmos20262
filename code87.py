#desenvolva um algoritmo em python que verifique o menor
#numero de uma sequencia de numeros informados pelo usuário.
#a quantidade de numeros deve ser informada pelo usuario
#no inicio do codigo
menor = 99999999
qtde_numeros = int(input('quantos numeros? '))

for i in range(qtde_numeros):
    numero = int(input('digite um numero: '))
    if numero < menor:
        menor = numero

print(f'o menor numero digitado foi {menor}')