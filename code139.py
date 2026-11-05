#escopo local e global
#1 regra: escopo global é acessado dentro do local
#2 regra: variáveis declaradas local nao existem no global
time = 'gremio'
def oi():
    cidade = 'cz'
    time = 'vasco'
    print(f'LOCAL: {time}')
    print(cidade)
oi()
print(cidade)
print(f'GLOBAL: {time}')
