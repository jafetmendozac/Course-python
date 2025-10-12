def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  if  len(s) < 2 or len(s)>6:
    print("Hola2")
    return False
  
  number_started = False
  for i, l in enumerate(s):
    if i < 2 and not l.isalpha:
      print("Hola")
      return False
    
    if l.isnumeric():
      if not number_started:
        number_started = True
        if l == "0":
          return False
    else:
      if number_started:
        return False

      
    if not(l.isnumeric or l.isalpha()):
      print("Hola4", l, l.isnumeric())
      return False
  return True


main()