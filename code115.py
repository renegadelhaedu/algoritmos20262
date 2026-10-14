#questao 17
nome_campeao = ''
atletas = []
maior_media = 0
while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    saltos = list()
    media = 0
    for i in range(5):
        salto = float(input('digite o salto: '))
        media += salto
        saltos.append(salto)
    atletas.append([nome, saltos])
    if media > maior_media:
        maior_media = media
        nome_campeao = nome

maior_media = maior_media / 5
print(f'a maior media foi {maior_media} e o campeao foi {nome_campeao}')


print(atletas)






