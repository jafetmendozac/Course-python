import re
import sys


def main():
  print(validate(input("IPv4 Address: ")))


def validate(ip):
  try:
    parts_ip= ip.split(".")
    for part in parts_ip:
      if len(part) != len(str(int(part))) or int(part) > 255 or int(part) < 0:
        return False
    return True 
  except ValueError:
    return False
    

if __name__ == "__main__":
    main()



# import re
# import sys

# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(ip):
#     # Regular expression for valid IPv4
#     pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
#     if re.match(pattern, ip):
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     main()
