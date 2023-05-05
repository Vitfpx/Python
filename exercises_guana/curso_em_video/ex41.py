from datetime import date

birth = int(input("Ano de nascimento: "))

age = date.today().year - birth

mirim = age <= 9
infantil = age <= 14
junior = age <= 19
senior = age <= 25

if mirim:
    category = "MIRIM"
elif infantil:
    category = "INFANTIL"
elif junior:
    category = "JUNIOR"
elif senior:
    category = "SENIOR"
else:
    category = "MASTER"

print(f"O atleta tem {age} anos.")
print(f"Classificação: {category}")