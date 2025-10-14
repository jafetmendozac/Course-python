
# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# def main():
#   date = trasformDate("Date: ")
#   print("-".join(date))


# def trasformDate(prompt):
#   while True:
#     try:
#       date = input(prompt)
#       if "/" in date:
#         month, day, year = date.split("/")
#         month = f"{int(month):02}"
#         day = f"{int(day):02}"
#         year = f"{int(year)}"
#         if int(month) > 12 or int(day) > 31:
#           pass
#         else: 
#           return [year, month, day]
#       else: 
#         month, day, year = date.split(" ")
#         for i, m in enumerate(months):
#           if m == month:
#             month = i+1
#         month = f"{int(month):02}"
#         day = f"{int(day[0]):02}"
#         if int(month) > 12 or int(day) > 31:
#           pass
#         else:
#           return [year, month, day]

#     except ValueError:
#       pass
#     except KeyError:
#       pass
#     except EOFError:
#       break



# main()



months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    date = transform_date("Date: ")
    print("-".join(date))

def transform_date(prompt):
    while True:
        try:
            date = input(prompt).strip()

            # Format: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                month = f"{int(month):02}"
                day = f"{int(day):02}"
                year = f"{int(year)}"
                if int(month) > 12 or int(day) > 31:
                    continue
                return [year, month, day]

            # Format: Month D, YYYY
            else:
                month, day, year = date.split(" ")
                day = day.replace(",", "")  # remove comma
                for i, m in enumerate(months):
                    if m == month:
                        month = i + 1
                        break
                month = f"{int(month):02}"
                day = f"{int(day):02}"
                if int(month) > 12 or int(day) > 31:
                    continue
                return [year, month, day]

        except ValueError:
            continue
        except EOFError:
            break

main()
