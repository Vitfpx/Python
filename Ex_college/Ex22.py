''''
22. Write a program that calculates the area of a circle of radius r, testing whether the radius value is less than zero.
'''

r = int(input("Digite o valor do raio do círculo: "))

pi = 3.1415

area = pi*r**2

if r < 0:
    print("O raio deve ser positivo!")
else:
    print(f"A área do círculo seria {round(area, 2)}cm².")