s_idade = 0
homem_velho = 0
f_novas = 0
nome_homem_velho = ""

for i in range(1, 5):

    print(
        f"{'-' * 5}"
        f" {i}ª pessoa "
        f"{'-' * 5}"
    )

    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M] ou [F]: ").capitalize().strip()

    s_idade += idade

    if sexo == "M" and idade > homem_velho: # pode ser feito if sexo in "Mm"
        nome_homem_velho = nome
    elif sexo != "M" and sexo != "F":
        print("Erro! A característica de sexo foi colocada de forma errada...")
        break
    elif sexo == "F" and idade < 20:
        f_novas += 1

media_idade = s_idade / 4

print(f"A média de idade desse grupo é de {media_idade} anos.")
print(f"O nome do homem mais velho do grupo é {nome_homem_velho}.")
print(f"Tem {f_novas} mulheres com menos de 20 anos nesse grupo.")
