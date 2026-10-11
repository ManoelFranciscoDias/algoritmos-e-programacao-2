# 7 - Faça um programa em que o usuário deve digitar um número de 1 a 7. Se digitar 1, deve imprimir "Domingo", 2 - Segunda, 3 - Terça e assim por diante.

try:
    numero = int(input('Informe um número de 1 a 7: '))

    if numero == 1:
        print('Domingo')
    elif numero == 2:
        print('Segunda')
    elif numero == 3:
        print('Terça')
    elif numero == 4:
        print('Quarta')
    elif numero == 5:
        print('Quinta')
    elif numero == 6:
        print('Sexta')
    elif numero == 7:
        print('Sábado')
    else:
        print('Número inválido. Digite um número de 1 a 7.')

except ValueError:
    print('Entrada inválida. Digite um número inteiro.')
