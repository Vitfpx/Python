print("Soma entre números primos!")

s = 0

for i in range(1, 500+1):
    if i % 2 != 0 and i % 3 == 0:
        s += i
        print(f"\033[3;31m{i}\033[m \033[4;36mÍmpar e múltiplo de 3\033[m")
    elif i == 500:
        print(i)
        print(f"A soma de todos os ímpares e múltiplos de 3 é \033[4;36m{s}\033[m")
    else:
        print(i)
