# greet = input("Greeting: ").strip()

# if greet.startswith("Hello"):
#   print("$0")
# elif greet.startswith("H"):
#   print("$20")
# else: 
#   print("$100")

# Optimized and more robust version

greet = input("Greeting: ").strip().lower()

if greet.startswith("hello"):
  print("$0")
elif greet.startswith("h"):
  print("$20")
else: 
  print("$100")
