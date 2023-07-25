from time import sleep
from random import randrange

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

while True:
    jogador = input("Par ou ímpar? ").capitalize().strip()
    match jogador:
        case "Ímpar":
            COMPUTADOR = "Par"
        case _:
            COMPUTADOR = "Ímpar"

    np = int(input("Digite um número: "))
    sleep(1)
    print("Par ou Ímpar!!!")
    sleep(1)

    nc = randrange(0, 11)

    if (nc + np) % 2 == 0:
        