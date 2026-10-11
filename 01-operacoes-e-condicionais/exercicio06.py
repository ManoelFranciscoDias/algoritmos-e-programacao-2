# 6 - Faça um programa que solicite ao usuário um número. Imprima na tela se o número é par ou impar, positivo, negativo ou simplesmente igual a zero.

try:
    numero = int(input('Informe um número: '))

    if numero == 0:
        print('O número é igual a zero.')
    else:
        if numero % 2 == 0:
            paridade = 'par'
        else:
            paridade = 'ímpar'

        if numero > 0:
            sinal = 'positivo'
        else:
            sinal = 'negativo'

        print(f'O número é {paridade} e {sinal}.')

except ValueError:
    print('Entrada inválida. Digite um número inteiro.')
