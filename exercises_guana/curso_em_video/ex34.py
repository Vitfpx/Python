sal = float(input("Qual o salário do funcionário? R$"))

if sal > 1250:
    novo_sal = sal + sal * 0.10
else:
    novo_sal = sal + sal * 0.15

print(f"Quem ganhava \033[1;32;40mR${sal:.2f}\033[m passa a ganhar \033[1;32;40mR${novo_sal:.2f}\033[m agora.")