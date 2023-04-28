from random import randrange
from time import sleep 

print(
    f'{"-=-" * 20}\n'
    "Vou pensar em um número entre 0 e 5. Tente adivinhar...\n"
    f'{"-=-" * 20}'
)

chute = int(input("Em que número eu pensei? "))

n = randrange(0, 6)
resultado = chute == n

print("PROCESSANDO")
sleep(1)

if resultado:
    print(f"Parabéns! Você conseguiu me vencer, pensei exatamente no número {n}!")
else:
    print(f"GANHEI! Eu pensei no número {n} e não no {chute}")

#%%