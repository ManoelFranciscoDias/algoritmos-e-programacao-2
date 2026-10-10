# 1 - Faça um programa que peça dois números decimais ao usuário
# e imprima a adição desses dois números, a multiplicação, a subtração, a exponenciação e a média.

num1 = float(input('Digite o primeiro número: ').replace(',', '.'))
num2 = float(input('Digite o segundo número: ').replace(',', '.'))

adicao = num1 + num2
multiplicacao = num1 * num2
subtracao = num1 - num2
exponenciacao = num1 ** num2
media = (num1 + num2) / 2

print(f'Adição: {num1} + {num2} = {adicao}')
print(f'Multiplicação: {num1} * {num2} = {multiplicacao:.1f}')
print(f'Subtração: {num1} - {num2} = {subtracao}')
print(f'Exponenciação: {num1} ** {num2} = {exponenciacao:.1f}')
print(f'Média: {media:.1f}')
