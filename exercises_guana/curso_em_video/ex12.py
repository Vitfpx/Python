preco = float(input("Qual o preço do produto? R$"))

promo = preco - (preco * 5 / 100)

print(
    f"O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${promo:.2f}.")
