
import sys
from tabulate import tabulate

data = []

def getData(file_path):
  try:
    with open(file_path, "r", encoding="utf-8") as file:
      for row in file:
        rows = row.split(",")
        # print(rows)
        data.append(rows)
      return data
  except FileNotFoundError:
    sys.exit("File does not exist")




def main():
  if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments")

  file_path = sys.argv[1]
  if not file_path.endswith(".csv"):
    sys.exit("Not a CSV file")
  
  print(tabulate(getData(file_path), tablefmt="grid"))


if __name__ == "__main__":
  main()