from random import randint

tentativa = 0
palpite = 0

print("""Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")

aleatorio = randint(0, 10)

acertou = False

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))
    tentativa += 1
    if palpite == aleatorio:
        acertou = True
    else:
        if palpite < aleatorio:
            print("\033[1;31mMais... Tente mais uma vez.\033[m")
        elif palpite > aleatorio:
            print("\033[1;36mMenos... Tente mais uma vez.\033[m")
print(f"Acertour com {tentativa} tentativas. Parabéns")
