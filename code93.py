ano_inicial = 1995
sal_inicial = float(input('quanto é q tu ganha? '))
aumento = 1.5 / 100 #1996
#1997 em diante dobra o percentual

for ano in range(1996, 2026):
    sal_inicial = sal_inicial * (1 + aumento)
    print(f'no ano de {ano} ele ganha {sal_inicial:.2f}')
    aumento  = aumento * 2



