#while precisa que seja True para entrar no bloco dentro dele
#e continuar repetindo
#se for falso, vai para a primeira instrução depois do while.
'''
valide a senha da rádio angelim: abc123
'''

login = ''
senha = ''
logado = False
tent = 0
while tent < 5 and logado == False:
    login = input('\nDigite o login da radio: ')
    senha = input('Digite sua senha: ')
    if login == 'angelim' and senha == 'abc123':
        logado = True
    else:
        tent += 1
        print('quantidade de tentativas restantes: ', 5 - tent)

if logado:
    print('MENU')
    print('1-cadastrar radialista')
else:
    print('login e senha incorretos')