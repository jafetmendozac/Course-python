# import re
# import sys


# def main():
#   print(count(input("Text: ")))

# def count(s):
#   try:
#     pattern = r"\bum\b"
#     matches = re.findall(pattern, s, re.IGNORECASE )
#     return len(matches)
#   except:
#     sys.exit()


# if __name__ == "__main__":
#     main()



import re

def count(text: str) -> int:
    return len(re.findall(r"\bum\b", text, re.IGNORECASE))

def main():
    text = input("Text: ")
    print(count(text))

if __name__ == "__main__":
    main()
