atletas = [['rene',[1.1, 2.14, 7.22]], ['gilvan',[3.1, 4.14, 9.22]]]


k = []
j = ['aaaa']
k.append([j, 23423423])


usuarios = []

usuario = ['rene','renegadelha@gmail.com','123', ['12/10','14/10']]
usuarios.append(usuario)
print('email do usuário:', usuarios[0][3][0])


login = input('digite seu login')
senha = input('Digite sua senha')
logado = False
for user in usuarios:
    if login == user[1] and senha == user[2]:
        logado = True

if not logado:
    print('usuario ou senha incorretos')
else:
    print('logado com sucesso')
    print('MENU')



