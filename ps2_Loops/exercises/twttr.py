

# text = input("Input: ")
# newText=[]
# for t in text:
#   if t.lower() not in ["a","e", "i", "o", "u"]:
#     newText.append(t)

# print("Ouput: ", ".join(newText))


text = input("Input: ")
vowels = "aeiouAEIOU"
new_text = [t for t in text if t not in vowels ]
print("".join(new_text))