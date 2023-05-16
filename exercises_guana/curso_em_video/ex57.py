sexo = input("Informe seu sexo [M/F]: ").upper().strip()

while sexo not in "MmFf":
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip()

print(f"Sexo {sexo} registrado com sucesso!")