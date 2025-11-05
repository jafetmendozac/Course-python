import sys
import csv




def main():
  if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")
  try:
    if open(sys.argv[1]):
      rows = getData(sys.argv[1])
      create_csv(rows)
  except FileNotFoundError:
    print("Could not read invalid_file.csv")
  

def getData(file_path):
  with open(file_path, "r") as file:
    ffile = csv.reader(file, delimiter=",")
    rows =[["first", "last", "house"]]
    i =0
    for row in ffile:
      if i > 1:
        first, last = row[0].split(",")
        rows.append([first, last.strip(), row[1]])
      i+=1
    return rows

def create_csv(rows):
  with open(sys.argv[2], 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
if __name__ == "__main__":
  main()