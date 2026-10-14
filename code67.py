'''
extra: um cidadão decidiu criar um quarto inteligente no qual o quarto possui sensores e atuadores. O objetivo é criar um algoritmo que facilite a noite de sono do morador, conferindo conforto térmico e economia de energia.
O algoritmo deve também controlar e proteger o quarto de assalto, chuva e entrada de animais indesejados (gatos de rua).

sensores: sensor de luminosidade na janela, sensor de temperatura, sensor de umidade, sensor de presença dentro do quarto, sensor de presença na área externa a janela.

atuadores: controla o ar-condicionado, controla a abertura/fechamento da janela, controle do ventilador, controle dos umidificadores.

Crie um algoritmo que receba como entrada o status dos sensores, além do horário e modele um algoritmo para o quarto responder com os atuadores com base nos objetivos.
'''
luz = int(input('Digite o valor do sensor de luminosidade: '))
temp = int(input('Digite o valor do sensor de temperatura: '))
umid = int(input('Digite o valor do sensor de umidade: '))
pres_intra = input('tem presença interna? ')
pres_exter = input('tem presença externa na janela? ')
horario = int(input('Digite o valor das horas: '))

if luz >= 7 and horario >= 5 and pres_intra == 'sim':
    print('feche a janela')
    print('ligar o ar-condicionado')
elif umid < 45 and temp < 22 and pres_intra == 'sim' and (horario > 23 or horario < 7) and pres_exter == 'sim':
    print('feche a janela')

#criem mais
















