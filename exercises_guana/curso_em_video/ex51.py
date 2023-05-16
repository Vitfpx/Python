print(
    f"\033[1;31m{'=' * 18}\033[m\n\t"
        "PA\n"
    f"\033[1;31m{'=' * 18}\033[m"
)

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Agora, digite a razão dessa PA: "))

for i in range(termo, termo + razao * 10, razao):
    print(i, end=" → ")

print("Fim")

# ou
# for i in range(termo + razao, termo + razao * 11, razao):
# caso comece no primeiro termo com a razao