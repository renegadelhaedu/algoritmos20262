#criar
#adicionar
#percorrer/buscar
#atualizar um elemento

so = ['xp','7','vista','8','10','11']
campo = input('qual so vc quer mudar? ')
ind = -1
for i in range(6):
    if so[i] == campo:
        ind = i

if ind == -1:
    print('o SO digitado nao está presente na lista')
else:
    novo = input('digite o SO que vai substituir: ')
    so[ind] = novo
    print(so)
