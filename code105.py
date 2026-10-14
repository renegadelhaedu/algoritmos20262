#questao 1 -  de listas
nums = []
for i in range(5):
    numero = int(input('digite o número: '))
    nums.append(numero)

for num in nums:
    if num % 2 == 0: #mostrar nums pares
        print(num)