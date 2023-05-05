n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

# verificar quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f"O maior valor digitado foi {maior}")

# verificar quem é maior
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f"O menor valor foi {menor}")
