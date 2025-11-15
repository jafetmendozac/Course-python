# i = 0
# while i < 3:
#   i += 1
#   print("MEew")



# for _ in range(100):
#   print("emoz")



# print("meow\n" * 3, end="")


# n = int(input("What's n? "))
# if n <0:
#   n = int(input("What's n? "))
#   if n < 0:
#     n=int(input())


# while True:
#   print("Infinite Loop")

# while True:
#   n = int(input("What's n? "))
#   if n < 0:
#     continue
#   else: break


# while True:
#   n = int(input("What's n? "))
#   if n > 0:
#     break


# for i in range(n):
#   print("meow")


def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      break
  return n
      

def meow(n):
  for _ in range(n):
    print("meow")

main()