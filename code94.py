#Desenvolva um algoritmo que leia alturas dos alunos de uma
#sala de 43 alunos e verifique quem é o mais alto, o menor
#e a media de altura.
nome_maior = ''
nome_menor = ''
maior = 0
menor = 999
soma = 0
for pessoa in range(43):
    nome = input('qual seu nome? ')
    alt = float(input('qual sua altura? '))
    if alt > maior:
        nome_maior = nome
        maior = alt
    if alt < menor:
        nome_menor = nome
        menor = alt
    soma = soma + alt

media = soma / 43

