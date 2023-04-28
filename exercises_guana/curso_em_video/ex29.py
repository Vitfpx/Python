v = float(input("Qual a velocidade atual do carro? "))

preco = (v - 80) * 7
multa = v > 80

if  multa:
    print(
        "MULTADO! você excedeu o limite permitido que é 80km/h\n"
        f"Você deve pagar uma multa de R${preco:.2f}\n"
        "Tenha um bom dia! Dirija com segurança!"
    )

    print("Tenha um bom dia! Dirija com segurança!")
