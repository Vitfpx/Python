'''
24. Write a program that calculates the falling velocity of a body as a function of time, starting from zero velocity. Hint: Use acceleration equations from physics.
'''

t = float(input("Digite a velocidade do objeto: "))
a = 10
V = 0

V = a*t

print(f"A velocidade em função do tempo é de {V:.2f}m/s²")