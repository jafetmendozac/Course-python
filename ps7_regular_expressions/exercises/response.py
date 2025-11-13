# import validators

# email = input ("What's your email address? ").strip()

# if validators.email(email):
#   print("Valid")
# else:
#   print("Invalid")




import validators


email = input ("What's your email address? ").strip()

print("Valid" if validators.email(email) else "Invalid")
