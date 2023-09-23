amount = 50
while amount > 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount -= coin
print("Change Owed:", amount * -1)
