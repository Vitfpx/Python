print("Gerador de PA")
print("-=" * 10)

pt = int(input("Primeiro termo: ")) # primeiro termo
r = int(input("Razão da PA: ")) # razão
cont = 1 # contador
qt = 10 # quantidade de termos
t = 1 # termos a mais

while t != 0:
    while cont <= qt:
        print(pt, end=" ▷ " if cont <= qt-1 else " PAUSA\n")
        pt += r
        cont += 1
    t = int(input("Quantos termos você quer mostrar a mais? "))
    qt += t
print(f"Progressão finalizada com {qt} termos mostrados.")
