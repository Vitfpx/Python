n = int(input("Digite um número: "))
half = n // 2
asteriscos = half
espacos = 0

print("Resultado:")

if n % 2 == 0:
    for i in range(half, 0, -1):
        if i == half:
            print("*" * n)    
        else:
            print(" " * espacos, "*", " " * (i-1) * 2, "*", sep="")
        espacos += 1
            
    for i in range(0, half):
        if i != half-1:
            print(" " * (asteriscos-1),"*", " " * i * 2, "*", sep="")
            asteriscos -= 1
        else:
            print("*" * n)
           
else:
    for i in range(half-1, -1, -1):
        if i == half-1:
            print("*" * n) 
        else:
            print(" " * (espacos),"*", " " * (i+half-espacos) , "*", sep="")
        espacos += 1
    print(" " * half, "*", sep="")
    for i in range(1, half+1):
        if i != half:
            print(" " * (asteriscos-1),"*", " " * (i+espacos-half), "*", sep="")
            asteriscos -= 1
            espacos += 1
        else:
            print("*" * n)
