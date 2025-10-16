def main():

  text = formatted("Name: ")
  print(text)


def formatted(prompt):
  names=[]
  text = "Adieu, adieu, to "
  while True:
    try:
      name = input(prompt)
      names.append(name)
    except EOFError:
      print("")
      break
  for i, n in enumerate(names):
    if i+1 == 1:
      text += f"{n}"
    elif len(names) == i+1:
      text += f" and {n}"
    else:
      text += f", {n}"
  return text

main()




# Optimized

# def main():
#     names = get_names()
#     print(format_names(names))


# def get_names():
#     names = []
#     while True:
#         try:
#             name = input("Name: ")
#             names.append(name)
#         except EOFError:
#             print()  # print a newline before returning
#             return names


# def format_names(names):
#     text = "Adieu, adieu, to "
#     if len(names) == 1:
#         return text + names[0]
#     elif len(names) == 2:
#         return text + f"{names[0]} and {names[1]}"
#     else:
#         return text + f"{', '.join(names[:-1])}, and {names[-1]}"


# if __name__ == "__main__":
#     main()
