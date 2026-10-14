#questao 27 da lista de decisao
qtde_mor = float(input('quantidade: '))
qtde_mac = float(input('quantidade: '))

if qtde_mor <= 5:
    prec_mor = qtde_mor * 2.5
else:
    prec_mor = qtde_mor * 2.2

if qtde_mac <= 5:
    prec_mac = qtde_mac * 1.8
else:
    prec_mac = qtde_mac * 1.5

total = prec_mac + prec_mor

if qtde_mac + qtde_mor > 8 or total > 25:
    total = total * 0.9

print('voce vai pagar no total', total)
