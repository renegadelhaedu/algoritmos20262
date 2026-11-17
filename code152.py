#arquivos
#registro de dados em disco de armazenamento
#escrita: write(w),append(a)
#leitura: read(r)

#modo r: lê o arquivo sem alterar conteúdo

arquivo = open('vida.txt','r',encoding='utf-8')
#criar uma lista de linhas do texto
texto = arquivo.readlines()
eu = 0
espa = 0
for linha in texto:
    if 'eu'in linha.lower():
        eu += 1
    espa += linha.count(' ') + 1
arquivo.close()

tx_na = eu / espa * 100
print(tx_na)