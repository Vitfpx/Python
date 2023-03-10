folha = int(input("Informe a quantidade de folhas: "))

xerox = folha * 0.25

if folha > 100: 
    xerox = 0.20 * folha

print(f"O valor a ser pago será de R${(round(xerox, 2))}")
