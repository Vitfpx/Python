n = int(input("Digite um número: "))
half = n // 2

print("Resultado: ")

for i in range(0, half):
    print(" " * i, "*", sep="")
if n % 2 == 1:
    print(" " * (i+1), "*", sep="")
for i in range(half, 0, -1):
    print(" " * (i-1), "*", sep="")
