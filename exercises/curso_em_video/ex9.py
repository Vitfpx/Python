num = int(input("Enter a number to see your table: "))

print("-------------------------")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i:02} = {result:02}")

print("-------------------------")