from time import sleep

print(
    f"{'-=' * 20}\n"
    "\033[1;31mCONTAGEM PARA OS FOGOS DE ARTIFÍCIO\n\033[m"
    f"{'-=' * 20}"
)

for cont in range(10, -1, -1):
    sleep(0.7)
    print(cont)
    if cont == 0:
        print("BOOOOOOOOOOM!")
