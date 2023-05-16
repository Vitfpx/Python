print(
    f'{"-=" * 12}\n\t'
    "TABUADA!!\n"
    f'{"-=" * 12}'
)

tabuada = int(input("Qual tabuada você quer consultar? "))

for i in range(1, 11):
    print(f"{tabuada} * {i} = {(tabuada * i):02}")
    