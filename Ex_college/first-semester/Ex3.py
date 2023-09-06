'''
3. Write a program that takes a person's year of birth, calculates their age, and tells them if they are of legal age.
'''

ano = int(input("Digite o ano de seu nascimento: "))
idade = 2023 - ano
if (idade >= 18):
    print(f"Você tem {idade} e é maior de idade!")
else:
    print("Você tem {} e ainda é menor de idade.".format(idade))
