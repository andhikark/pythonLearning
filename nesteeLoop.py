rows = int(input("How many rows?: "))
column = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(column):
        print(symbol,end="")
    print()

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_num = "123-456-7890"

for i in phone_num:
    if i == "-":
        continue
    print(i,end="")
