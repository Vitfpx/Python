print(
    f'{"-=" * 12}\n\t'
    "TABUADA!!\n"
    f'{"-=" * 12}'
)

tabuada = int(input("Qual tabuada você quer consultar? "))

for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} * {i} = {resultado:02}")