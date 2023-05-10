print("LEITOR DE NÚMEROS PARES")

s = 0
cont = 0

for cont in range(1, 7):
    num = int(input("Digite um número inteiro qualquer: "))
    cont += 1
    if num % 2 == 0:
        s += num
print(f"A soma dos números pares que você digitou é {s}")