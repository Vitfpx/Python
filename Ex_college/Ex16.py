'''
16. Write a program that solves the following problem: a “xerox” copy costs R$ 0.25 per sheet, but over 100 sheets this value drops to R$ 0.20 per unit. Given the total number of copies, inform the amount to be paid.
'''

copias = int(input("Informe a quantidade de cópias: "))

xerox = copias * 0.25

if copias > 100: 
    xerox = 0.20 * copias

print(f"O valor a ser pago será de R${(round(xerox, 2))}")
