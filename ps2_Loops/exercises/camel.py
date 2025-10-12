# text = input("camelCase: ")
# newtext = ""
# for l in text:
#   if l.isupper():
#     newtext += "_" + l.lower()
#   else:
#     newtext += l


# print("snake_case", newtext)


# text = input("camelCase: ")
# snake = []

# for l in text:
#     if l.isupper():
#         snake.append('_')
#         snake.append(l.lower())
#     else:
#         snake.append(l)

# print("snake_case:", ''.join(snake))


text = input("camelCase: ")
snake = ''.join(['_' + c.lower() if c.isupper() else c for c in text])
print("snake_case:", snake)