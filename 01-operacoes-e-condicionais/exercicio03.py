# 3 - Faça um programa que solicite ao usuário digitar a altura e largura de uma determinada área a ser medida. 
# Imprima na tela do valor área total conforme os valores digitados pelo usuário. 

altura = float(input("Digite a altura da área (em metros): "))
largura = float(input("Digite a largura da área (em metros): "))

area = altura * largura

print(f"A área total é de {area:.2f} m².")

