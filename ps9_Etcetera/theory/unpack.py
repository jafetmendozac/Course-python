
"""Unpacking"""

## Unpacks a list
# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")




##  Passes positional arguments as usual
## https://harrypotter.fandom.com/wiki/Wizarding_currency
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# print(total(100, 50, 25), "Knuts")



## 3 Indexes into list
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")



## Unpacks a list
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "Knuts")



## Passes named arguments as usual
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# print(total(galleons=100, sickles=50, knuts=25), "Knuts")



## Indexes into a dict
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")


# Unpacks a dict
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts")



"""args and kwargs"""
## Prints positional arguments
# def f(*args, **kwargs):
#     print("Positional:", args)


# f(100, 50, 25) # Return a list of arguments: (100, 50, 25)


# Prints a word in uppercase
# def f(*args, **kwargs):
#     print("Named:", kwargs)


# f(galleons=100, sickles=50, knuts=25)
