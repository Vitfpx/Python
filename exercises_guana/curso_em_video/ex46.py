from time import sleep

print(
    f"{'-=' * 26}\n\t"
    "\033[1;31mCONTAGEM PARA OS FOGOS DE ARTIFÍCIO\n\033[m"
    f"{'-=' * 26}"
)

for cont in range(10, -1, -1):
    sleep(0.7) 
    print(cont)

print("BOOOOOOOOOOM!")
