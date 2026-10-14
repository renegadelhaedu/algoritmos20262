#estrutura de decisão simples
nome1 =input('qual seu nome? ')
alt_pessoa1 = float(input('qual a altura? '))
nome2 = input('qual seu nome? ')
alt_pessoa2 = float(input('qual a altura? '))

if alt_pessoa1 > alt_pessoa2:
    print(nome1, ' é mais alto do que', nome2)
else:
    print(nome1, ' é menor ou igual a ', nome2)