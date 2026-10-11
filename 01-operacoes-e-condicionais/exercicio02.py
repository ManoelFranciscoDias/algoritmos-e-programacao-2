# 2 - Escreva um programa que peça ao usuário um valor em metros e o exiba convertido em centímetros.

metros = float(input('Digite um valor em metros: ').replace(',','.'))

centimetros = metros * 100

print(f'{metros} metros equivalem a {centimetros} centímetros.')
