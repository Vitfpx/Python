sal = float(input("Qual o salário do funcionário? R$"))

novo_sal = sal + (sal * 15 / 100)

print(f"Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber {novo_sal:.2f}")