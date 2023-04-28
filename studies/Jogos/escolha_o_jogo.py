import forca
import adivinhacao

def escolher_jogo():

    msg_centralizada = "Choice your game".center(30, " ")

    print(f"{'*' * 32}\n"
          f'{msg_centralizada}\n'
          f"{'*' * 32}"
    )

    print("(1)Forca e (2)Adivinhação")

    jogo = int(input("Escolha qual jogo você quer jogar: "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
    
if __name__ == '__main__':
    escolher_jogo()