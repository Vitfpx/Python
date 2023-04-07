print('********************************')
print("Bem vindo ao jogo de advinhação!")
print('********************************')

numero_secreto = 42
total_de_tentaivas = 1

while total_de_tentaivas <= 3:
    print(f"Tentativa: {total_de_tentaivas} de 3")

    str_chute = input("Digite o seu número: ")
    print("Você digitou {}".format(str_chute))
    chute = int(str_chute)

    acertou = chute == numero_secreto # Variáveis para deixar as condições mais limpas
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertouu!")
    else:
        if maior:
            print("Você errou! O chute indicado foi maior do que o número secreto...")
        elif menor:
            print("Você errou! O chute indicado foi menor do que o número secreto...")

    total_de_tentaivas = total_de_tentaivas + 1      
      
    print("Fim de jogo.")