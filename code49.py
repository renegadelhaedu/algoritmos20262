'''
desenvolva um algoritmo que leia a idade de uma pessoa
e informe para ela se ela está fora dos parâmetros
de normalidade para entrar na PF.
a PF aceita apenas pessoas de 18 até 34.
'''
idade = int(input('Digite sua idade: '))
if idade < 18 or idade > 34:
    print('voce nao pode entrar na PF')
else:
    print('voce pode entrar na PF')