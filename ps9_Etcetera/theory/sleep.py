"""Generators and Iterators"""
## Prints n sheep

# n = int(input("What's n? "))
# for i in range(n):
#     print("🐑" * i)


## Adds main
# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print("🐑" * i)


# if __name__ == "__main__":
#     main()




## Returns n sheep from helper function
# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print(sheep(i))


# def sheep(n):
#     return "🐑" * n


# if __name__ == "__main__":
#     main()



## Returns a list of sheep
# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)


# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock


# if __name__ == "__main__":
#     main()


## Uses yield
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
