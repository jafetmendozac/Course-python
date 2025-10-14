
# def main():
#   gauge = fuel("Fraction: ")
#   if gauge <= 1:
#     print("E")
#   elif gauge >= 99:
#     print("F")
#   else:
#     print(gauge, end="%")


# def fuel(prompt):
#   while True:
#     fraction = input(prompt)
#     x, y = fraction.split("/")
#     try:
#       x = int(x)
#       y = int(y)
#       if x > y:
#         pass
#       else:
#         return int(x/y*100)
      
#     except ValueError:
#       # print("Not integer")
#       pass
#     except ZeroDivisionError:
#       # print("Denominator not be 0")
#       pass

# main()



def main():
    gauge = fuel("Fraction: ")
    if gauge <= 1:
        print("E")
    elif gauge >= 99:
        print("F")
    else:
        print(f"{gauge}%")

def fuel(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                continue
            percentage = round((x / y) * 100)
            return percentage
        except (ValueError, ZeroDivisionError):
            continue  # ask again if input invalid

main()
