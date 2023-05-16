num = int(input("Digite um número inteiro: "))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[1;33m", end="")
        total += 1
    else:
        print("\033[1;31m", end="")
    print(c, end=" ")
print(f"\n\033[mO número {num} foi dividido por {total} vezes.")

if total == 2:
    print("Por isso, ele é PRIMO")
else:
    print("Por isso, ele é NÃO É PRIMO")
