# text = {}

# while True:
#   try:
#     grocery = input()
#     if grocery in text:
#       text[grocery] = text[grocery] + 1
#     else:
#       text[grocery] = 1
#   except EOFError:
#     print("\n")
#     break

# myKeys = list(text.keys())
# myKeys.sort()

# sd = {i: text[i] for i in myKeys}

# for i in sd:
#   print(sd[i], i.upper())


groceries = {}

while True:
    try:
        item = input().strip().upper()  # normalize to uppercase
        groceries[item] = groceries.get(item, 0) + 1
    except EOFError:
        print()
        break

for item in sorted(groceries):
    print(groceries[item], item)
