'''um casal de alunos está precisando de um sistema
para ler a nota e a frequência do casal nas aulas.
o sistema deve aprovar o aluno mesmo que ele tenha
obtido nota inferior a 7, porém a frequencia precisa
ser 100% e a nota nao pode ser menor que 6.
algoritmo deve receber dois dados: nota e frequência.
obs:menos de 75% de frequência reprova.
'''
nota = float(input('digite sua nota: '))
frequencia = float(input('digite sua frequencia: '))
if (nota >= 7 and frequencia >= 75) or (nota >= 6 and frequencia >= 100):
    print('aprovado')
else:
    print('reprovado')





