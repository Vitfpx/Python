from time import sleep

opcao = 0

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))


while opcao != 5:
    print(
    "[ 1 ] somar\n"
    "[ 2 ] multiplicar\n"
    "[ 3 ] maior\n"
    "[ 4 ] novos números\n"
    "[ 5 ] sair do programa"
    )

    opcao = int(input(">>>> Qual é sua opção? "))

    if opcao == 1:
        print(f"A soma de {n1} + {n2} = {n1+n2}.")
        print(
            f'{"-=" * 12}'
        )
    elif opcao == 2:
        print(f"O resultado de {n1} * {n2} = {n1 * n2}.")
        print(
            f'{"-=" * 12}'
        )
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"Entre {n1} e {n2} o maior valor é {maior}.")
        elif n2 > n1:
            maior = n2
            print(f"Entre {n1} e {n2} o maior valor é {maior}.")
        else:
            print("Os dois valores são iguais.")

        print(
            f'{"-=" * 12}'
        )
    elif opcao == 4:
        print("Informe os números novamente...")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print(
            f'{"-=" * 12}'
        )
print("Finalizando...")
sleep(1)

print(
    f'{"-=" * 12}'
)
print("Fim do programa! Volte sempre!")