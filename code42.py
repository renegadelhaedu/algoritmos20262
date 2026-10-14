#operadores lógicos (AND)
curso_online = input('fez curso online? ')
psicot = input('passou no psicotecnico? ')
toxi = input('o exame apontou algo ilícito? ')
pratica = input('passou na pratica? ')

if curso_online == 'sim' and psicot == 'sim' and toxi == 'não' and pratica == 'sim':
    print('voce está aprovado e tome sua CNH')
else:
    print('deu ruim para você')


