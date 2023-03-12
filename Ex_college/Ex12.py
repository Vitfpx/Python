'''
12. Given a value in reais and the dollar exchange rate, convert this value to dollars.
'''

real = float(input("Digite um valor em reais: R$"))
cotacao = float(input("Agora a cotação atual do dólar atualmente: "))

dolar = real * cotacao

print(f"O valor digitado em reais equivale a U${dolar}.")
