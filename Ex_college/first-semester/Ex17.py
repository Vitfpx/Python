'''
17. Write a program that informs the category of a soccer player, considering his age: junior (up to 13 years old), juvenile (up to 17 years old) or senior (above 17 years old).
'''

idade = int(input("Digite a idade: "))

if idade <= 13:
    print("CATEGORIA: Infatil")
elif idade > 13 and idade <= 17:
    print("CATEGORIA: Juvenil")
else:
    print("CATEGORIA: Sênior")