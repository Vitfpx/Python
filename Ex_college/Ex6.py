'''
6. Write a program that converts a temperature in Fahrenheit to Celsius.
'''

Fahrenheit = int(input("Digite uma temperatura em Fahrenheit: "))
Celcius = (Fahrenheit - 32) / 1.8

print(f"A temperatura de {Fahrenheit}ºF equivale a {round(Celcius, 2)}ºC")