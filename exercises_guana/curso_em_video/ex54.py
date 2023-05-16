from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1, 8):
    ano_nasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))

    if ano_atual - ano_nasc >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f"Ao todo tiveram {maioridade} pessoas maior de idade e {menoridade} pessoas menor de idade.")
