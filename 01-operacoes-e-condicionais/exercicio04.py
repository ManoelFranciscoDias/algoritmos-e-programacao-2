# 4 - Faça um programa que solicite ao usuário sua idade. 
# Depois Imprima esta idade na tela e informe o ano de nascimento do usuário que digitou a idade.

idade = int(input('Digite sua idade: '))

ano_nascimento = 2026 - idade

print(f'Você tem {idade} anos.')
print(f'Você nasceu em {ano_nascimento}.')

