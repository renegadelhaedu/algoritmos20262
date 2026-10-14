#questao 1 -  de listas
letras = []
vogais = ['a', 'e', 'i', 'o', 'u']
for i in range(10):
    letra = input('diga a letra: ')
    letras.append(letra)

qtde = 0
for letra in letras:
    if letra not in vogais:
    #if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        qtde = qtde + 1
        print(letra)

print(f'foram digitadas {qtde} consoantes')