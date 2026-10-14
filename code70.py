#estrutura de repetição: while

soma = 0
i = 0
while i < 5:
    idade = int(input('digite sua idade: '))
    soma = soma + idade
    i = i + 1

print('a soma de idades foi ', soma)
media = soma / 5
print('a media de idade foi ', media)
print('valor de i', i)