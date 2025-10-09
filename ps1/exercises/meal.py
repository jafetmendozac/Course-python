# def main():
#   time = input("What time is it? ")
#   timeFormatted = convert(time)
#   print(timeFormatted)
#   print("breakfast time" if timeFormatted >= 7 and timeFormatted <= 8 else "lunch time" if timeFormatted >= 12 and timeFormatted <= 13 else "dinner time" if timeFormatted >= 18 and timeFormatted <= 19 else "")


# def convert(time):
#   h, m = time.split(":")
#   m = int(m)/60
#   return int(h)+m

# if __name__ == "__main__":
#     main()




def main():
    time = input("What time is it? ")
    time_in_hours = convert(time)

    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")
    else: ""


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
