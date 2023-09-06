n = int(input("Digite um número: "))

print("Resultado: ")

for i in range(0, n):
    print(" " * i, "*", sep="")
for i in range(n-1, 0, -1):
    print(" " * (i-1), "*", sep="")