n = int(input("Digite um número \033[1;31minteiro:\033[m "))
print(
    '''Escolha uma das \033[1;31mbases\033[m para \033[1;32mconversão\033[m:\n\t
        \033[0;34m[ 1 ]\033[m converter para \033[1;31mBINÁRIO\033[m\n\t
        \033[0;34m[ 2 ]\033[m converter para \033[1;31mOCTAL\033[m\n\t
        \033[0;34m[ 3 ]\033[m converter para \033[1;31mHEXADECIMAL\033[m
    '''
    )

conv = int(input("Sua opção: "))

if conv == 1:
    print(f"{n} convertido para BINÁRIO é igual a {bin(n)[2:]}")
elif conv == 2:
    print(f"{n} convertido para DECIMAL é igual a {oct(n)[2:]}")
elif conv == 3:
    print(f"{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}")
