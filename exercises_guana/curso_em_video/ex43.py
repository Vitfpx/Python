kg = float(input("Qual é seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))

imc = kg / (altura * altura)

abaixo = imc < 18.5
ideal = imc >= 19.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidade = imc >= 30 and imc < 40
morbido = imc > 40

print(f"O IMC dessa pessoa é de {round(imc, 2)}")

if abaixo:
    print("Você está \033[4;31mABAIXO\033[m do peso")
elif ideal:
    print("PARANBÉNS! Você está no peso \033[4;32mIDEAL\033[m")
elif sobrepeso:
    print("Você está em \033[4;31mSOBREPESO\033[m")
elif obesidade:
    print("Você está em \033[4;31mOBESIDADE\033[m")
elif morbido:
    print("Você está em \033[4;31mOBESIDADE MÓRBIDA\033[m. Cuidado")
