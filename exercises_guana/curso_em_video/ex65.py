s = maior = menor = q = media = 0
pergunta = "s"

while pergunta in "Ss":
    n = int(input("Digite um número: "))
    pergunta = input("Quer continuar? [S/N]: ").strip()[0]

    s += n
    q += 1

    if q == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

media = s / q

print(f"Você digitou {q} números e a média deles foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}.")
