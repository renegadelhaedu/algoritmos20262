#renê informou os alunos que quem tirar mais de 9
#na prova, terá sua nota aumentada em 10%.
#faça um algoritmo que leia a nota, verifique se está
#acima de 9 e faça o aumento exibindo a nota final.
minha_nota = float(input('digite sua nota do aluno: '))

if minha_nota > 9:
    #final = minha_nota * 1.1
    final = minha_nota + (minha_nota * 0.1)
    print('sua nota final foi', final)
else:
    print('sua nota foi ', minha_nota)