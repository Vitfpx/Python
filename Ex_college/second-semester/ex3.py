n = int(input("Digite um número: "))

print("Resultado: ")

for i in range(1, n+1):
    print(i, " ", (n-i) * "-", "*", "-*" * (i-1), sep="")
    # print(i, ' ', (n-i)*'-', '*', (i-1)*'-*', sep='')
