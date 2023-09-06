n = int(input("Digite um número: "))

print("Resultado: ")

for i in range(0, n):
    print(i, " ", "-" * i, "*-" * (n-i-1), "*", sep='')
