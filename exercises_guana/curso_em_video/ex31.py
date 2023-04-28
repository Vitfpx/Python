d = float(input("Qual a distância da sua viagem? "))

if d <= 200:
    preco = d * .5
else:
    preco = d * 0.45

print(
    f"Você está prestes a começar uma viagem de {d}km\n"
    f"E o preço da sua viagem será de R${preco:.2f}"
)
