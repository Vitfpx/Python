print(
    f'\033[4;31m{"_" * 12}\033[m\n'
    "\033[4;31mApenas pares\033[m\n"
)

for i in range(2, 51, 2):
    print(i, end=". ")
print("\nAqui estão todos os números pares de 1 a 50.")