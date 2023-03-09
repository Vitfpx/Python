mes = (input("Escolha um mês do ano: "))

if mes in ["janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"]:
    print(f"O mês de {mes} tem 31 dias.")
elif mes == "fevereiro":
    print(f"O mês de {mes} tem 28 ou 29 dias.")
else:
    print(f"O mês de {mes} tem 30 dias.")
