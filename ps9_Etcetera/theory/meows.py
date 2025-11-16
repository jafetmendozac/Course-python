## Demonstrates a constant
# MEOWS = 3

# for _ in range(MEOWS):
#   print("meow")


## Demonstrates a class constant
# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow", Cat.MEOWS)


# cat = Cat()
# cat.meow()


# Success --- using mypy in the terminal this could usefull to find the error
# def meow(n: int):
#   for _ in range(n):
#     print("meow")


# number: int = int(input("Number: "))
# meow(number)



## Prints None because mistakes meow as having a return value
# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)


## Annotates return value, ... does not return a value
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)


## Success
# def meow(n: int) -> str:
#     return "meow\n" * n


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")





## Uses Sphinx docstring format
# def meow(n):
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# number = int(input("Number: "))
# meows = meow(number)
# print(meows, end="")






####. argparse ###
# Uses command-line argument

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py [-n NUMBER]")


## Uses command-line argument - Adds description, help
# python3 meows.py --help
# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")



## Adds default, type; removes int()
# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args()

# for _ in range(args.n):
#     print("meow")