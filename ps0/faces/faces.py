# text = input()

# text = text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")

# print(text)


'''
optimized for scaling
'''
text = input()

replacements = {
  ":)": "\U0001F642", # 🙂
  ":(": "\U0001F641",  # 🙁
}

for symbol, emoji in replacements.items():
  text = text.replace(symbol, emoji)

print(text)