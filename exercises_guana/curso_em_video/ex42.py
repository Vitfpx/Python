n1 = int(input("Primeiro segmento: "))
n2 = int(input("Segundo segmento: "))
n3 = int(input("Terceiro segmento: "))

if n3 + n2 > n1 and n2 + n1 > n3 and n1 + n3 > n2:
    if n1 != n2 and n2 != n3 and n1 != n3:
        print("Os segmentos acima podem formar um \033[4;32mtriângulo ESCALENO!\033[m")
    elif n1 == n2 and n2 == n3:
        print("Os segmentos acima podem formar um \033[4;35mtriângulo EQUILÁTERO\033[m")
    else:
        print("Os segmentos acima podem formar um \033[4;34mtriângulo ISÓSCELES\033[m")
else:
    print("Os semgentos acima \033[0;31mNÃO PODEM FORMAR um triângulo\033[m")
    