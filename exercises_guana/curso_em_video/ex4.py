a = input("Digite algo: ")

print(f"O tipo primitivo desse valor é: {type(a)}")
print(f"É apenas espaço: {a.isspace()}")
print(f"É um número: {a.isnumeric()}")
print(f"É um número alfabético: {a.isalpha()}")
print(f"É um alfanumérico: {a.isalnum()}")
print(f"É maiúscula: {a.isupper()}")
print(f"É minúscula: {a.islower()}")
print(f"É capitalizada: {a.istitle()}")