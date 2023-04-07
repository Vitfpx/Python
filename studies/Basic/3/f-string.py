# f-string comum
print(f"Tentativa {3} de {5}")

# f-string com ordens invertidas
print(f"Tentativa {5} de {3}")

# f-string com diferenças
print(f"R${1.59}") # Normal
print(f"R${1.59:f}") # O f transforma a variável em float
print(f"R${1.59:.2f}") # Delimitação dos caracteres da variável
print(f"R${1.5:.2f}") # 2 caracteres após o ponto independente de ser definido
print(f"R${1.59:7.2f}") # Número de espaço que a variável vai ocupar
print(f"R${4244.23:7.2f}") # O tópico acima pode ser usado para deixar um padrão de distância
print(f"R${44.23:07.2f}") # Colocar algo nos espaços antes da variável até completar o número definido (no caso 7)

# Testando a formatação com inteiros
print(f"R${4:07d}") # Número inteiro
print(f"R${42:07d}") # Quanto mais números, menos zeros
print(f'R${42:7d}') # Sem os zeros

# Exemplo
print(f"Data {9:02d}/{4:02d}")
print(f"Data {19:02d}/{11:02d}")