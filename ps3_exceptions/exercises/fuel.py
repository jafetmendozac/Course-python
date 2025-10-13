
def main():
  gauge = fuel("Fraction: ")
  if gauge <= 1:
    print("E")
  elif gauge >= 99:
    print("F")
  else:
    print(gauge, end="%")


def fuel(prompt):
  while True:
    fraction = input(prompt)
    x, y = fraction.split("/")
    try:
      x = int(x)
      y = int(y)
      if x > y:
        pass
      else:
        return int(x/y*100)
      
    except ValueError:
      # print("Not integer")
      pass
    except ZeroDivisionError:
      # print("Denominator not be 0")
      pass

main()