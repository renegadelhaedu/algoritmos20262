saque = int(input("digite um valor inteiro: "))

nota100 = saque // 100
resto = saque % 100
print('resto de 100', resto)
nota50 = resto // 50
resto = resto % 500
print('resto de 50', resto)
nota10 = resto // 10
resto = resto % 10
print('resto de 10', resto)
nota1 = resto // 1
resto = resto % 1
print('notas de 100: ', nota100 )
print('notas de 50: ', nota50)
print('notas de 10: ', nota10)
print('notas de 1: ', nota1)
