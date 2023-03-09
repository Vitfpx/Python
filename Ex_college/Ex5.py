km = float(input("Qual foi a distância percorrida: "))
litros = float(input("Qual foi o consumo em litros: "))

consumoMedio = km / litros

print(f"O consumo médio do seu carro é de {consumoMedio:.2f}km/l") 

# Definir o número de decimais também pode ser feito com {round(consumoMedio, 2)}