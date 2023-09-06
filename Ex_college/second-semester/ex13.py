n = int(input("Digite um número: "))
met = n // 2
asterisco = 1

print("Resultado: ")
if n % 2 == 0:
    for i in range(met, 0, -1):
        print(" " * (i-1), "*" * asterisco, " " * (i-1), sep="")
        asterisco += 2
    for i in range(0, met):
        asterisco -= 2
        print(" " * i, "*" * asterisco, sep="")
if n % 2 != 0:
    for i in range(met, 0, -1):
        print(" " * (i), "*" * asterisco, " " * (i-1), sep="")
        asterisco += 2
    print("*" * n)
    for i in range(0, met):
        asterisco -= 2
        print(" " * (i+1), "*" * asterisco, sep="")
 