# print("     strip     ".strip())
# print("Maiúsculo".upper())
# print("Minúsculo".lower())
# print("T,exto, c,o,m vá,ria,s v,ír,g,ulas".replace(",", ""))
# print("Texto teste para função count".count("e"))
# print("Texto centralizado".center(50, "*")) #50 seria o número de caracteres total, ou seja, só será preenchido com * o que estiver vazio
# print("Avião?".index('ã'))
# print("Alfanumérico".isnumeric())
print("Teste de quebra de string com split".split(" "))
# print("NOME;CIDADE;IDADE;PAÍS".split(";"))
# print("Este é um título".title())
# print("este é um título".capitalize())
# print("585".zfill(5))
# print("Texto cheio de caracteres".__len__()) # ou print(len("Texto cheio de caracteres"))

# Encadeamento de funções
print("   Te;x;;to   ".strip().replace(";", "").center(25, "*").upper())