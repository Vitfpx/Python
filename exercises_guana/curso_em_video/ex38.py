n1 = int(input("\033[4;31mPrimeiro número:\033[m "))
n2 = int(input("\033[4;31mSegundo número:\033[m "))

if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n2 > n1:
    print("O SEGUNDO valor é maior")
else:
    print("Os dois valores são IGUAIS")