
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