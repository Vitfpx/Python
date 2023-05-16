frase_espacada = input("Digite uma frase para ver se ela é palíndroma: ").strip()
frase = frase_espacada.replace(" ", "")

if frase.capitalize() == frase[::-1].capitalize():
    print("Essa frase é um \033[3;33mpalíndromo!\033[m")
    print(frase_espacada[::-1])
else:
    print('Essa frase não é um \033[3;31mpalíndromo...\033[m')
    print(frase_espacada[::-1])
