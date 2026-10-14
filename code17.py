#questao 7
qtde = int(input('digite quantos pedaços: '))
pessoas = int(input('digite quantos pessoas: '))

fp = qtde // pessoas
sobrou = qtde % pessoas

print('cada pessoa vai receber ', fp, 'pedaços')
print('sobrou ainda', sobrou,'pedaços')