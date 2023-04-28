import random

def jogar():

    print(
        f"{'*' * 34}\n"
        "Bem vindo ao jogo de adivinhação!\n"
        f"{'*' * 34}"
  )

    numero_secreto = random.randrange(1, 101)
    total_de_tentaivas = 0
    pontos = 500

    print(f"Esse é seu número de pontos: {pontos}")
    print("Qual o nível de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil (4)Impossible")

    nivel = int(input("Defina o nível do jogo: "))

    if nivel == 1:
        total_de_tentaivas = 15
    elif nivel == 2:
        total_de_tentaivas = 10
    elif nivel == 3:
        total_de_tentaivas = 5
    else:
        total_de_tentaivas = 3

    for rodada in range(1, total_de_tentaivas + 1):
        print(f"Tentativa: {rodada} de {total_de_tentaivas}")

        str_chute = input("Digite o seu número entre 1 e 100: ")
        print("Número digitado: {}".format(str_chute))
        chute = int(str_chute)

        if chute < 1 or chute > 100:
            print("ERRO! Digite um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto # Variáveis para deixar as condições mais limpas
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertooou!\n O número era {numero_secreto}\n Com isso você fez {pontos} pontos nesta rodada!")
            print(f"Pontos totais: {pontos}") 
            break
        else:
            if rodada == total_de_tentaivas:
                print(f"Você perdeu. O número secreto era {numero_secreto}\nAlguns pontos foram perdidos :(")
                
            elif maior:
                print("Você errou! O chute indicado foi maior do que o número secreto...\n")
            elif menor:
                print("Você errou! O chute indicado foi menor do que o número secreto...\n")
            pontos_perdidos = abs(numero_secreto - chute) # 40 - 20 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos

    print(f"Pontos totais: {pontos}")

    print("Fim de jogo.")

if __name__ == "__main__":
    jogar()