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