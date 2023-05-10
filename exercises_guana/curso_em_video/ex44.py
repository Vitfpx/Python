print(
    f'{"=" * 10}' 
    " LOJAS VIT "
    f'{"=" * 10}'
)

preco = float(input("Preço das compras: R$"))

print(
    """\tFORMAS DE PAGAMENTO:
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
    """
)

pagamento = int(input("Qual é a opção desejada? "))

if pagamento == 1:
    desconto = preco * 0.1
    print(
        f"Sua compra de R${preco:.2f} vai custar R${(preco - desconto):.2f} no final.\n"
        f"O desconto será de R${desconto:.2f}."
    )

elif pagamento == 2:
    desconto = preco * 0.05
    print(
        f"Sua compra de R${preco:.2f} vai custar R${(preco - desconto):.2f} no final.\n"
        f"O desconto será de R${desconto:.2f}."
    )

elif pagamento == 3:
    preco_parcelado = preco / 2
    print(f"O preço será de R${preco:.2f}.\nSerão R${preco_parcelado:.2f} cada parcela")
elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))

    juros = preco * 0.2
    preco_parcelado = (preco + juros) / parcelas
    preco_final = preco + juros

    print(
f"""Sua compra será parcelada em {parcelas:.2f}x de R${preco_parcelado:.2f} COM JUROS.
O juros em si terá o valor de R${juros:.2f}.
A compra realizada de R${preco:.2f} vai custar R${preco_final:.2f} no final."""
    )
else:
    print("\033[1;31mOpção inválida de pagamento. Tente novamente.\033[m4")
