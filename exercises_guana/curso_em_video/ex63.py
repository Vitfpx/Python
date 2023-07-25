print(
    f'{"-" * 30}\n'
    "Sequência de Fibonacci\n"
    f'{"-" * 30}'
)

t = int(input("Quantos termos você quer mostrar? "))
n = 0
n1 = 1
n2 = n + n1
cont = 3

print("~" * 30)
print(f"{n} ▷ {n1}", end=" ▷ ")
while cont <= t:
    print(n2, end=" ▷ ")
    n = n1
    n1 = n2
    n2 = n + n1
    cont += 1
print("FIM")
print("~" * 30)