valor_casa = float(input("\033[4;35mQual o valor da casa: R$"))
sal = float(input("\033[4;35mDigite seu salário: R$"))
anos = int(input("\033[4;35mEm quantos anos a casa será paga: "))

prestacao = valor_casa / (anos * 12)
minimo = prestacao > sal * 30 / 100

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.")

if minimo:
    print("\033[1;31mEmpréstimo NEGADO!\033[m")
else:
    print("\033[1;32mEmpréstimo APROVADO!\033[m")
