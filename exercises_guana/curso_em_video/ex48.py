s = 0
n_somados = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s += i
        n_somados += 1
        print(f"\033[3;31m{i}\033[m \033[4;36mÍmpar e múltiplo de 3\033[m")
    elif i == 500:
        print(i)
        print(f"A soma dos {n_somados} números ímpares e múltiplos de 3 é \033[4;36m{s}\033[m")
    else:
        print(i)
