'''
Exercício 2.1 - o secretário de meio ambiente de cajazeiras solicitou um sistema para controlar as licenças ambientais dos CNPJ's criados. As licenças
são emitidas com base nas seguintes regras:
a-imóveis com mais de 200 m2 devem requerer uma vistoria especial gratuita ou devem pagar a taxa de licença sem vistoria de 500 reais o metro quadrado.
b-imóveis de até 200 m2 devem pagar 70 reais o metro quadrado, porém caso tenham finalidade sanitária deve pagar 120 reais o metro quadrado

faça um algoritmo que modele este fluxo, solicite as informações necessárias e informe para o usuário o que ele deve pagar.
'''
m2 = float(input('digite quantos metros quadrados possui seu terreno: '))
if m2 > 200:
    resp = input('voce vai requerer uma vistoria especial gratuita?')
    if resp == 'sim':
        print('voce nao precisa pagar nada')
    else:
        total = 500 * m2
        print('voce vai pagar ', total, ' reais')
else:
    resp2 = input('tem finalidade sanitária? hospital, etc ')
    if resp2 == 'sim':
        total = 120 * m2
        print('voce vai pagar ', total, ' reais por ter finalidade sanitaria')
    else:
        total = 70 * m2
        print('voce vai pagar ', total, ' reais')