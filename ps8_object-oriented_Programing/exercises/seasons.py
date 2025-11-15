
from datetime import date, datetime
from num2words import num2words
import sys


def main():
  try:
    get_date_birth = input("Date of Birth: ")
    if my_date_object := date.fromisoformat(get_date_birth):
      date_birth = datetime(my_date_object.year, my_date_object.month, my_date_object.day, 0, 0, 0)

      today = date.today()
      date_today = datetime(today.year, today.month, today.day, 0, 0, 0)

      time_elapsed = date_today - date_birth
      minutes_elapsed = time_elapsed.total_seconds() / 60
      print(num2words(minutes_elapsed).capitalize() + " minutes")
  except ValueError as e:
    sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()