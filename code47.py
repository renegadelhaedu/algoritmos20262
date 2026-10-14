#ajude Renê a melhorar o algoritmo
num = int(input('digite um numero: '))
resposta = input('o número digitado é par? ')

if num % 2 == 0 and resposta == 'sim':
    print('este número é par e voce acertou')

if num % 2 == 1 and resposta == 'sim':
    print('este número é impar e voce ERROU')

if num % 2 == 0 and resposta == 'nao':
    print('este número é par e voce ERROU')

if num % 2 == 1 and resposta == 'nao':
    print('este número é impar e voce acertou')