while True:
    tab = int(input("Quer ver a tabuada de qual valor? "))
    if tab < 0:
        break
    print("-" * 40)
    for n in range(1, 11):
        print(f"{tab} x {n} = {tab * n}")
    print("-" * 40)
print("-" * 40)
print("PROGRAMA TABUADA ENCERRADA. Volte sempre!")