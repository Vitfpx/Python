menor_peso = 0
maior_peso = 0

for i in range(1, 6):
    peso = float(input(f"O peso da {i}ª pessoa: "))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else: 
        if peso < menor_peso:
            menor_peso = peso
        elif peso > maior_peso:
            maior_peso = peso

print(f"O menor peso foi {menor_peso:.2f}kg e o maior foi {maior_peso:.2f}kg.")
