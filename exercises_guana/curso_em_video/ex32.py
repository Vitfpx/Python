from datetime import date

today = date.today()
hoje = f"{today.day:02}/{today.month:02}/{today.year:04}"

ano = int(input("Que ano você quer analisar? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    print(hoje)
elif ano % 100 == 0 and ano % 400 != 0:
    print(f"O ano {ano} NÃO BISSEXTO")
elif ano % 4 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} NÃO É BISSEXTO")