# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

ano = int(input("digite o ano"))

if ano %4 == 0:
    print("é um ano bissexto")
else:
    print("não é um ano bissexto")

