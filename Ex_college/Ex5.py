'''
5. Write a program that receives the distance in KM traveled by a car and the consumption in liters, then calculates the average consumption.
'''

km = float(input("Qual foi a distância percorrida: "))
litros = float(input("Qual foi o consumo em litros: "))

consumoMedio = km / litros

print(f"O consumo médio do seu carro é de {consumoMedio:.2f}km/l") 

# Definir o número de decimais também pode ser feito com {round(consumoMedio, 2)}