from datetime import date

birth = int(input("Ano de nascimento: "))

age = date.today().year - birth
missing = 18 - age
enlistment = birth + 18

print(f"Quem nasceu em {birth} tem {age} anos em {date.today().year}.")

if age < 18:
    print(f"Aindal faltam {missing} anos para o alistamento.")
    print(f"Seu alistamento será em {enlistment}.")
elif age > 18:
    print(f"Você já deveria ter se alistado há {abs(missing)} anos.")
    print(f"Seu alistamento foi em {enlistment}")
else:
    print("Você tem que se alistar IMEDIATAMENTO!")
    