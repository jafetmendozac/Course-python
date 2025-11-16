"""List Comprehensions"""

##3 Uses list comprehension
# def main():
#     yell("This", "is", "CS50")


# def yell(*words):
#     uppercased = [arg.upper() for arg in words]
#     print(*uppercased)


# if __name__ == "__main__":
#     main()



## Filters by house using loop
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)



## Filters by house using list comprehension

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)




## Uses filter and key with lambda -- Order a list using a function lambda as key
# students = [
#   {"name": "Hermione", "house": "Gryffindor"},
#   {"name": "Harry", "house": "Gryffindor"},
#   {"name": "Ron", "house": "Gryffindor"},
#   {"name": "Draco", "house": "Slytherin"},
# ]


# def is_gryffindor(s):
#   return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda stu: stu["name"]):
#   print(gryffindor["name"])




## Uses filter with lambda
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]


# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])



"""Dictionary Comprehensions"""
## Creates list of dicts using loop
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)


## Uses dictionary comprehension instead
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)




## Uses dictionary comprehension instead
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)


"""enumerate"""
## Iterates over a list by index
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


# Uses enumerate instead
# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print(i + 1, student)