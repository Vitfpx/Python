# n = número, s = soma, q = quantidade de termos
n = s = q = 0 
while n != 999:
    s += n
    q += 1
    n = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {q-1} número(s) e a soma entre ele(s) foi {s}.")