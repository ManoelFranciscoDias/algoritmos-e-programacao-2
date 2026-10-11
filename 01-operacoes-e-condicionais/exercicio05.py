# 5 - Escreva um programa que peça ao usuário a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.

dias = int(input('Informe a quantidade de dias: '))
horas = int(input('Informe a quantidade de horas: '))
minutos = int(input('Informe a quantidade de minutos: '))
segundos = int(input('Informe a quantidade de segundos: '))

total_em_segundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print(f'O total em segundos é de: {total_em_segundos}s')
