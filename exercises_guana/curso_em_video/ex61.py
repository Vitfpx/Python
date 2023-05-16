print("Gerador de PA")
print(f"{'-=' * 10}")

pt = int(input("primeiro termo: ")) # primeiro termo
r = int(input("Razão da PA: ")) # razão
cont = 1

while cont <= 10:
    print(f"{pt}", end=" → ")
    pt += r
    cont += 1

print("FIM")
