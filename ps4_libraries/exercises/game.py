
from random import randint

while True:
  try:
    level = int(input("Level: "))
    if level < 1:
      continue
    else:
      break
  except ValueError:
    continue

random_number = randint(1, level)

while True:
  guess = int(input("Guess: " ))
  if guess > 0:
    if random_number > guess:
      print("Too small!")
    elif random_number < guess:
      print("Too large!")
    else:
      print("Just right!")
      break



# Optimized version

# from random import randint

# def get_level():
#     while True:
#         try:
#             level = int(input("Level: "))
#             if level >= 1:
#                 return level
#         except ValueError:
#             pass  # ignore invalid input

# def get_guess():
#     while True:
#         try:
#             guess = int(input("Guess: "))
#             if guess > 0:
#                 return guess
#         except ValueError:
#             pass  # ignore invalid input

# def main():
#     level = get_level()
#     random_number = randint(1, level)

#     while True:
#         guess = get_guess()
#         if guess < random_number:
#             print("Too small!")
#         elif guess > random_number:
#             print("Too large!")
#         else:
#             print("Just right!")
#             break

# if __name__ == "__main__":
#     main()
