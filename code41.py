#operadores lógicos
altura = float(input('qual sua altura? '))
peso = float(input('qual o seu peso? '))
idade = int(input('qual a sua idade? '))
quer = input('qual quer dançar comigo? ')

if altura > 1.60 and peso > 40 and idade >= 18 and quer == 'sim':
    print('bora simbora')
else:
    print('vou ali que meu amigo segundo tá chamando')
