

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