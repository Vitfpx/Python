'''
23. Escreva um programa que receba um número inteiro do teclado e diga se ele é par. Dica: Um número é par se o resto da divisão dele por 2 for zero - usar o operador % de resto da divisão.
'''

numInt = int(input("Digite um número inteiro: "))

if numInt % 2 == 0:
    print("Seu número é par!")
else:
    print("Seu número é ímpar!")