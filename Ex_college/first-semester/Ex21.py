'''
21. Write a program that reads three numbers from the keyboard and prints them to the screen in reverse order of entry.
'''

num1 = int(input("Digite um número do seu teclado: "))
num2 = int(input("Digite um número novamente: "))
num3 = int(input("Digite o último número: "))

num = num1, num2, num3
reverso = list(reversed(num))

print(f"A ordem inversa seria: {reverso}.")