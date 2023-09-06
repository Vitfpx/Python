n = int(input("Digite um número: "))
space = " "

print("Resultado: ")

for i in range(n, 0, -1):
    print(" " * (n-i), "*", " " * (i-1) * 2, "*", sep="")
for i in range(0, n):
    print(" " * (n-1), "*", " " * (i*2), "*", sep="")
    n -= 1
