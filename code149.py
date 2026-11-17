#arquivos
#registro de dados em disco de armazenamento
#escrita: write(w),append(a)
#leitura: read(r)

#modo a: cria o arquivo e atualiza na última linha

arquivo = open('exemplo2.txt', 'a', encoding='utf-8')
texto = input('Digite um texto: ')
arquivo.write('\n' + texto)
arquivo.close()

