from time import sleep
from random import choice

print(f'''    
{"-=" * 10}
      JOKENPO!!
{"-=" * 10}'''
)

print("""
Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA"""
)

jogada = input("Qual é a sua jogada?  ").lower()

jogada_computador = choice(["pedra", "papel", "tesoura"]).lower()

if jogada == "1":
    jogada = "pedra"
elif jogada == "2":
    jogada = "papel"
elif jogada == "3":
    jogada = "tesoura"

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!")
sleep(0.5)

print(
    f'{"-=" * 12}\n'
    f"Computador jogou {jogada_computador}\n"
    f"Jogador jogou {jogada}\n"
    f'{"-=" * 10}'
)

if jogada_computador == "tesoura" and jogada == "papel":
    print("COMPUTADOR VENCE!")
elif jogada_computador == "pedra" and jogada == "tesoura":
    print("COMPUTADOR VENCE!")
elif jogada_computador == "papel" and jogada == "pedra":
    print("COMPUTADOR VENCE!")
elif jogada == "pedra" and jogada_computador == "tesoura":
    print("JOGADOR VENCE!")
elif jogada == "papel" and jogada_computador == "pedra":
    print("JOGADOR VENCE!")
elif jogada == "tesoura" and jogada_computador == "papel":
    print("JOGADOR VENCE!")
else: 
    print("EMPATE")
