# import sys

# print(sys.argv)

# def lines_of_code():
#   try:
#     line_count = 0
#     with open(sys.argv[1], "r") as file: # count_lines.py
#       for line in file:
#         if line.strip() and not line.startswith("#"):
#           line_count += 1
#     return  line_count
#   except FileNotFoundError:
#     sys.exit("File does not exist")



# if len(sys.argv) <= 1:
#   # print("Too few command-line arguments")
#   sys.exit("Too few command-line arguments")
# elif ".py" not in sys.argv[1]:
#   # print("Not a Python file")
#   sys.exit("Not a Python file")
# elif len(sys.argv) == 2:
#   print(lines_of_code())
# else:
#   # print("Too many command-line argumnets")
#   sys.exit("Too many command-line argumnets")


import sys

def lines_of_code(filepath):
    """Cuenta las líneas no vacías y que no sean comentarios en un archivo .py."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return sum(
                1 for line in file
                if line.strip() and not line.lstrip().startswith("#")
            )
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]
    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    print(lines_of_code(file_path))

if __name__ == "__main__":
    main()



