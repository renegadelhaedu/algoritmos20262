#arquivos
#registro de dados em disco de armazenamento

#abrir o arquivo
arq = open('exemplo2.txt', 'w', encoding='utf-8')
arq.write('o minicurso de agentes de IA vai ser top')

#fechar o arquivo
arq.close()

#escrita: write(w),append(a)
#leitura: read(r)

#modo w: cria o arquivo e sobrescreve o que tem dentro

