'''
Exercício 1: O Sistema de Empréstimo Bancário
Desenvolva um programa para um banco que avalia se um cliente pode ou não receber um empréstimo.
O programa deve pedir as seguintes informações ao usuário:
1. O nome do cliente (string)
2. A idade do cliente (inteiro)
3. O salário mensal do cliente (float)
4. O valor total do empréstimo desejado (float)
5. Em quantos meses ele deseja pagar (inteiro)

**Regras para aprovação:**
O empréstimo só será **APROVADO** se **todas** as condições abaixo forem verdadeiras simultaneamente (uso lógico obrigatório):
* O cliente deve ter 18 anos ou mais.
* O valor da parcela mensal (valor do empréstimo dividido pelos meses) **não pode** comprometer mais de 32% do salário mensal do cliente.

'''
nome = input('Digite o nome do cliente: ')
idade = int(input('Digite o idade do cliente: '))
salario = float(input('digite seu salário: '))
total_emp = float(input('digte o valor total do empréstimo: '))
meses = int(input('Digite quantos meses deseja pagar: '))

parcela = total_emp / meses
limite = salario * 0.32

if idade >= 18 and parcela <= limite:
    print('empréstimo aprovado')
else:
    print('empréstimo negado')
















