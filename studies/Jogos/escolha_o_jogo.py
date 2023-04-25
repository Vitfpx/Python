import forca
import adivinhacao

def escolher_jogo():

    print('********************************')
    print("        Choice your game        ")
    print('********************************')

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