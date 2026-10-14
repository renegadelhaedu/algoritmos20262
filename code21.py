#questao 1

preco = float(input('qual o preco do produto? '))

desconto = preco * 0.20

final = preco - desconto
print('o cliente economizou', desconto)
print('o preco do produto com desconto de 20%', final)