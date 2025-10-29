# code generates 10 random numbers and prints their average:

import random

# radint to have a number betwwen 1 and ten
numbers = []
for _ in range(10):
    num = random.randint(1, 100)
    numbers.append(num)


print("Numbers:", numbers)
average = sum(numbers) / len(numbers)
print("Average:", average)