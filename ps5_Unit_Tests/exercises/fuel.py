def main():
  fraction = input("Fraction: ")
  gauge = convert(fraction)
  return gauge(gauge)


def convert(fraction):
  while True:
    try:
      x, y = fraction.split("/")
      x = int(x)
      y = int(y)
      if y == 0 or x > y:
        continue
      percentage = round((x / y) * 100)
      return percentage
    except (ValueError, ZeroDivisionError):
      continue


def gauge(percentage):
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"


if __name__ == "__main__":
  main()
