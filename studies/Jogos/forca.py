def jogar():
    
    print(f'{"*" * 32}\n'
          "   Bem vindo ao jogo da forca   "
          f"\n{'*' * 32}"
    )

    palavra_secreta = "Alexandria"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    

    enforcou = False
    acertou = False

    print(letras_acertadas)
    
    while(not enforcou and not acertou): #Enquanto (True)
    
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1    
        letras_faltando = letras_acertadas.count("_")
        print(letras_acertadas)
        print(f"Ainda faltam {letras_faltando} letras...")

    print("Fim de Jogo")

if __name__ == "__main__":
    jogar() 