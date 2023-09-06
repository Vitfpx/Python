'''
13. Write a program that draws a Christmas tree using “*”.
'''

tamanho = int(input("Digite o tamanho desejado: "))

for i in range(tamanho):
    print(" " * (tamanho - i - 1) + "*" * (2 * i + 1))
print(" " * (tamanho - 1) + "*")
