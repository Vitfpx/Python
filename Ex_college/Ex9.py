'''
9. Write a program that takes two numbers and displays the addition, subtraction, multiplication, and division of these numbers.
'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print(f"Valor da adição: {adicao}\nValor da subtração: {subtracao}\nValor da multiplicação: {multiplicacao}\nValor da divisão: {divisao:.2f}")
