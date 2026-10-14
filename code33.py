#receba 3 notas de um aluno e veja se a média foi
#menor que 7. se for menor que 7 coloque ele para fazer
#prova final e verifique se na final ele obteve 5 pontos para
#ser aprovado.
#o algoritmo deve informar se ele foi aprovado ou reprovado

n1 = float(input('digite sua nota 1'))
n2 = float(input('Digite sua nota 2'))
n3 = float(input('Digite sua nota 3'))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print('Aprovado')
else:
    nota_final = float(input('digite sua nota final'))
    if nota_final >= 5:
        print('Aprovado')
    else:
        print('Reprovado')



