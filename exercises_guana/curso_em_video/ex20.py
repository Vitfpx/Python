from random import shuffle

a1 = input("Primeiro aluno: ")
a2 = input("segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista_alunos = list((a1, a2, a3, a4)) # OU lista_alunos = [a1, a2, a3, a4]
shuffle(lista_alunos)

print(f"A ordem de apresentação será: \n{lista_alunos}.")