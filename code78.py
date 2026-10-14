#continue
#continue quando acionado dentro do laço, remete diretamente
#para o início da repetição

qtde = 0
nome = ''
while True:
    nome = input('digite seu nome ou digite fim para encerrar: ')
    if nome == 'rafael':
        continue
    if nome == 'fim':
        break
    qtde = qtde + 1

print('a quantidae final foi ', qtde)