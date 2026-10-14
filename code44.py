'''questao 11 da lista de decisao
'''
salario = float(input('digite seu salario: '))
if salario <= 280:
    aum = 0.2
if salario > 280 and salario <= 700:
    aum = 0.15
if salario > 700 and salario <= 1500:
    aum = 0.1
if salario > 1500:
    aum = 0.05

valor_aum = salario * aum
final  = salario + valor_aum
print('antes ele recebia:', salario)
print('mas ele ganhou um aumento de ', aum * 100, 'porcento')
print('isso fez o salário dele aumentar', valor_aum)
print('sendo assim, no final ele ganhará', final)




