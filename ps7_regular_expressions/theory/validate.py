# email = input ("What's your email? ").strip()

# if "@" in email:
#   print("Valid")
# else: 
#   print("Invalid")

# email = input ("What's your email? ").strip()

# username, domain = email.split("@")

# import re

# email = input ("What's your email? ").strip()

# if re.search(r"^.+@.+\.edu$", email):
#   print("Valid")
# else: 
#   print("Invalid")


# import re

# email = input ("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.(com|edu|org|gov|net)$", email):
#   print("Valid")
# else: 
#   print("Invalid")





import re

email = input ("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else: 
  print("Invalid")