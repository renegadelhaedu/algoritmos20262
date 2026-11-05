#4 tipos de funções
#tipo 2: com parâmetros entrada, sem retorno

def descobrir_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print(f'Você tem {idade} anos')

ano = int(input('digite o ano de nascimento: '))
descobrir_idade(ano)


