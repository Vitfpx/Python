name = input("Digite seu nome completo: ").strip()

print(f"Seu nome em maiúsculas é {name.upper()}")
print(f"Seu nome em minúsculas é {name.lower()}")
print(f"Seu nome tem ao todo {len(name) - name.count(' ')} letras")
print(f"Seu primeiro nome é {name.split()[0]} e ele tem {len(name.split()[0])} letras")
