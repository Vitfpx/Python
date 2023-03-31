'''
25. Write a program that calculates the roots of passing the 2nd degree (ax² + bx + c); the values of a, b, and c are user-supplied (see proposed resolution below).
'''
import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

x1 = (-b+((b**2-4*a*c)**0.5))/(2*a)
x2 = (-b-((b**2-4*a*c)**0.5))/(2*a)

print(f"As raízes da equação serão x1 = {x1:.2f} e x2 = {round(x2, 2)}")
