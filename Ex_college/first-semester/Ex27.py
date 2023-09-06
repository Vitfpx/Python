'''
27. Write a program that takes a number and tells it if it is in the range between 100 and 200.
'''

num = float(input("Escreva um número qualquer: "))

if num > 100 and num < 200:
    print(f"{num} está entre 100 e 200.")
else:
    print(f"{num} não está entre 100 e 200.")