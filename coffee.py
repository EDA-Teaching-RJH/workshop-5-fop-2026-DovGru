price = 75
moneyList = [5,10,20,50]

while price > 0:
    print(f"price: {price}p")
    coin = int(input("Insert coin:"))

    if coin in moneyList:
        price -= coin
    else:
        print("Insert valid coin")

print("Thank you dispensing coffee")

change = abs(price)
print(f"Change owed: {change}p")
