n = int(input("Digite um número: "))
met =  (n // 2) 

print("Resultado:")

if n % 2 == 0:
    for i in range(1, met+1):
        print("*" * i)
    for i in range(met, 0, -1):
        print("*" * i)
else:
    for i in range(1, met + 2):
        print("*" * i)
    for i in range(met, 0, -1):
        print("*" * i)

# # 1a parte
# for linha in range(1,metade+1):
#     print(linha*'*')

# # Se impar
# if n%2 != 0:
#     print((metade+1)*'*')
    
# # 2a parte
# for linha in range(metade, 0, -1):
#     print(linha*'*')