def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")



def is_valid(s):
  if  len(s) < 2 or len(s)>6:
    return False
  
  number_started = False
  for i, l in enumerate(s):
    if i < 2 and not l.isalpha:
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
      return False
  return True



if __name__ == "__main__":
    main()
