import pyfiglet
import random
import sys


fig = pyfiglet.Figlet()
fonts = fig.getFonts()
font = random.choice(fonts)

if len(sys.argv) == 1:
  text = input("Input: ")
  print("Output:\n", pyfiglet.figlet_format(text, font=font))
elif len(sys.argv) == 3:
  if (sys.argv[1] == "-f" or sys.argv[1] ==  "--font") and sys.argv[2] in fonts:
    text = input("Input: ")
    print("Output:\n", pyfiglet.figlet_format(text, font=sys.argv[2]))
  else:
    sys.exit("Invalid usage")
else: 
  sys.exit("Invalida usage")


  import pyfiglet
import random
import sys

# Optimized

# def main():
#     fig = pyfiglet.Figlet()
#     fonts = fig.getFonts()

#     # Case 1: No arguments → random font
#     if len(sys.argv) == 1:
#         font = random.choice(fonts)
#     # Case 2: Font specified
#     elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
#         font = sys.argv[2]
#         if font not in fonts:
#             sys.exit("Invalid font name")
#     # Invalid usage
#     else:
#         sys.exit("Usage: python script.py [-f FONT_NAME]")

#     # Get user input
#     text = input("Input: ")
#     print("Output:\n", pyfiglet.figlet_format(text, font=font))


# if __name__ == "__main__":
#     main()
