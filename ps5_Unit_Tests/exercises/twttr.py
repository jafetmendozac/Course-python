def main():
  word = input("Input: ")
  print(shorten(word))

def shorten(word):
  vowels = "aeiou"
  new_text = [t for t in word if t not in vowels ]
  return "".join(new_text)

if __name__ == "__main__":
  main()