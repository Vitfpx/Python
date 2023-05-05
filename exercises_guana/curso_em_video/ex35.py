print(
    f'{"-=" * 20}\n'
    'Analisando o Triângulo\n'
    f'{"-=" * 20}'
)

n1 = float(input("Primeiro segmento: "))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento: "))

if n3 + n2 > n1 and n2 + n1 > n3 and n1 + n3 > n2:
    print("Os segmentos acima \033[0;36mPODEM FORMAR um triângulo\033[m")
else:
    print("Os semgentos acima \033[0;31mNÃO PODEM FORMAR um triângulo\033[m")
