money = float(input("How much money do you have in your wallet? R$"))

dollars = money / 4.93
euro = money / 5.41

print(f"With R${money} you can buy U${dollars:.2f}.")
print(f"With R${money} you can buy U${euro:.2f}.")
