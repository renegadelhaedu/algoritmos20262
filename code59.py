#desenvolva um algoritmo que verifique se o usuário é está elegendo
#a chapa correta para presidente de sala. o algoritmo deve ler
#o número do voto e informar se o usuário votou em algum candidato,
#se votou nulo ou em branco(00). as chapas são: 01, 02, 03, 04;

voto = input('qual seu voto? ')
if voto == '01' or voto == '02' or voto == '03' or voto == '04':
    print('seu voto foi válido')
elif voto == '00':
    print('seu voto foi em branco')
else:
    print('seu voto foi invalidado ou nulo')