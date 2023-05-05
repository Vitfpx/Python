n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2
reprovado = media < 5
aprovado = media >= 7
recuperacao = media >= 5 and media <= 6.9

print(f"Tirando {n1} e {n2}, a média do aluno é {media}")

if reprovado:
    print("O aluno está \033[4;31mREPROVADO.\033[m")
elif recuperacao:
    print("O aluno está em \033[4;35mRECUPERAÇÃO.\033[m")
elif aprovado:
    print("O aluno está \033[4;32mAPROVADO.\033[m")
