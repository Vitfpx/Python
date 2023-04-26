cidade = input("Em que cidade você nasceu? ").strip()

if cidade.upper().split(" ") == "santo".upper().split():
    print("True")
    
else:
    print("False")
    print(cidade.upper().split(" ", 0))