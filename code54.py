#questao 17 da lista de decisao

ano = int(input('qual o ano ?'))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('ano bissexto')
else:
    print('ano nao bissexto')