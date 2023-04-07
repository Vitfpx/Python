# .format comum
print("Tentativa {} de {}".format(3, 10))

# .format com ordens invertidas
print("Tentativa {1} de {0}".format(3, 10))

# .format com diferenças
print("R${}".format(1.59)) # Normal
print("R${:f}".format(1.59)) # O f transoforma a variável em float
print("R${:.2f}".format(1.59)) # Delimitação dos caracteres da variável
print("R${:.2f}".format(1.5)) # 2 caracteres após o ponto independente de ser definido
print("R${:7.2f}".format(1.59)) # Número de espaço que a variável vai ocupar
print("R${:7.2f}".format(4244.23)) # O tópico acima pode ser usado para deixar um padrão de distância
print("R${:07.2f}".format(44.23)) # Colocar algo nos espaços antes da variável até completar o número definido (no caso 7)

# Testando a formatação com inteiros
print("R${:07d}".format(4)) # Número inteiro
print("R${:07d}".format(42)) # Quanto mais números, menos zeros
print('R${:7d}'.format(42)) # Sem os zeros

# Exemplo
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))