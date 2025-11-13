import re
import sys


def main():
  print(convert(input("Hours: ")))


def convert(s):
  try: 
    time_pattern = r"\b(1[0-2]|[1-9])(?::([0-5][0-9]))?\s*([AP]M)\b"
    range_pattern = fr"{time_pattern}\s*\bto\b\s*{time_pattern}"

    if matches := re.findall(range_pattern, s, re.IGNORECASE):
      for match in matches:
        print(match)
        if match[2] == "AM":
          return f"{match[0].zfill(2)}:{ match[1] or '00'} to {int(match[3])+12}:{ match[4] or '00'}"
        else:
          return f"{int(match[0])+12}:{ match[1] or '00'} to {match[3].zfill(2)}:{ match[4] or '00'}"
    else:
      raise ValueError("Incorrect Pattern")
  except ValueError as e:
    sys.exit(f"Error: {e}")



if __name__ == "__main__":
    main()