'''
18. Write a program that says which is the greater of two distinct numbers received from the user.
'''

num1 = float(input("Digite um número qualquer: "))
num2 = float(input("Digite outro número qualquer: "))

if num1 > num2:
    print(f"O primeiro número({num1}) é maior do que o segundo({num2})")
else:
    print(f"O segundo número({num2}) é maior do que o primeiro({num1})")