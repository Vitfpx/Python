'''
28. Write a program that grants a 10% salary increase to employees of a company, who receive up to R$ 1,000.00.
'''

sal = float(input("Digite o valor do seu salário: R$"))

if sal <= 1000:
    novo_sal = sal + sal * 10 / 100
    print(f"Seu novo salário passará de R${sal:.2f} para R${novo_sal:.2f}.")
else:
    print("Seu salário não terá alteração kkkkk")