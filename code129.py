pessoas = dict()

for i in range(4):
    nome = input('diga seu nome ')
    cpf  = input('diga seu CPF ')
    tit_eleitor = input('diga seu titulo de eleitor ')
    email = input('diga seu email ')
    pessoas[email] = (nome, cpf, tit_eleitor)

#faça uma forma de atualizar o nome de uma pessoa
# buscando por email
email_busca = input('diga seu email ')
for email in pessoas:
    if email == email_busca:
        nome_atual = input('diga seu nome atualizado ')
        nova = (nome_atual, pessoas[email][1], pessoas[email][2])
        break
if nova:
    pessoas[email_busca] = nova
#----------------------------------------
if email_busca in pessoas:
    nome_atual = input('diga seu nome atualizado ')
    nova = (nome_atual, pessoas[email_busca][1], pessoas[email_busca][2])
    pessoas[email_busca] = nova










