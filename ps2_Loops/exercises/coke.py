# amountDue = 50
# while True:
#   print("Amount Due: ",amountDue)
#   insertCoin = int(input("Insert Coin: "))
#   if insertCoin == 25 or insertCoin == 10 or insertCoin == 5:
#     amountDue -= insertCoin
#   if amountDue == 0:
#     print("Change Owed: ", amountDue)
#     break


amountDue = 50

while amountDue > 0:
    print("Amount Due:", amountDue)
    insertCoin = float(input("Insert Coin: "))
    insertCoin = int(insertCoin)

    if insertCoin in [25, 10, 5]:
        amountDue -= insertCoin

changeOwed = abs(amountDue)
print("Change Owed:", changeOwed)
