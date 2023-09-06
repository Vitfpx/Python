n = int(input("Digite um número: "))
half = n // 2
asteriscos = 0

print("Resultado: ")
if n % 2 == 0:
    for i in range(half-1, -1, -1):
        print(" " * i, "*" * (asteriscos+1)," " * i, sep="")
        asteriscos += 2
    for i in range(0, half):
        print(" " * i, "*" * (asteriscos-1)," " * i, sep="")
        asteriscos -= 2
else:
    for i in range(half-1, -1, -1):
        print(" " * (i+1), "*" * (asteriscos+1)," " * i, sep="")
        asteriscos += 2
    print("*" * n)
    for i in range(0, half):
        print(" " * (i+1), "*" * (asteriscos-1)," " * i, sep="")
        asteriscos -= 2