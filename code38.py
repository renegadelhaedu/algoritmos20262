#o aluno do p1 jose augusto foi tirar a cnh e foi informado que precisa ter pelo menos 18 anos, fazer o
#teste psicotécnico e ser aprovado na prova de direção. Desenvolva um algoritmo na linguagem
#python que pergunte para o usuário a idade, se ele foi aprovado no psicotécnico e se foi
#aprovado no teste de direção. O programa deve informar se ele receberá sim ou nao a CNH.

#5 minutos para fazer

idade = int(input('Digite sua idade: '))

if idade >= 18:
    psico = input('voce foi aprovado no psicotecnico: sim ou nao? ')
    if psico == 'sim':
        direcao = input('voce foi aprovado no teste de direçao: sim ou nao? ')
        if direcao == 'sim':
            print('voce pode receber sua CNH')
        else:
            print('poxa, faltou só passar na prova prática de direçao')
    else:
        print('você precisa ter mais atençao no psicotecnico')
else:
    print('aguarde completar 18 anos de idade')