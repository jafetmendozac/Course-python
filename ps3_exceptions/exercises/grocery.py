text = {}

while True:
  try:
    grocery = input()
    if grocery in text:
      text[grocery] = text[grocery] + 1
    else:
      text[grocery] = 1
  except EOFError:
    print("\n")
    break

myKeys = list(text.keys())
myKeys.sort()

sd = {i: text[i] for i in myKeys}

for i in sd:
  print(sd[i], i.upper())
