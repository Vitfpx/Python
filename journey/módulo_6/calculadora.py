n1 = input("Digite o primero número: ")
n2 = input("Digite o segundo número: ")
print("Operações:\n\t"
        "+ para Adição\n\t"
        "- para Subtração\n\t"
        "* para Multiplicação\n\t"      
        "/ para Divisão"
)

choice = input("Escolha a operação desejada: ")

equation = f"{n1} {choice} {n2}"
result = eval(equation)

print(f"{'*' * 25}\n"
      f"Resultado: {result:.2f}\n"
      f"{'*' * 25}"
)
