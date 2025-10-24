

# with open("students.csv") as file:
#   for line in file:
#     row = line.rstrip().split(",")
#     name, house = row
#     print(f"{row[0]} is in {row[1]}")
#     print(f"{name} is in {house}")


# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append(f"{name} is in {house}")


# for student in sorted(students):
#   print(student)


# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     student = {}
#     student['name'] = name
#     student['house'] = house
#     students.append(student)

# for student in students:
#   print(f"{student['name']} is in {student['house']}")



# print(students)


# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     student = {"name": name, "house": house}
#     students.append(student)


# def get_name(student):
#   return student["name"]
  
# def get_house(student):
#   return student["house"]


# for student in sorted(students, key=lambda student: student['house']):
#   print(f"{student['name']} is in {student['house']}")

# import csv

# students = []
# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for name, home in reader:
#     students.append({"name": name, "home": home})


# for student in sorted(students, key=lambda student: student['home']):
#   print(f"{student['name']} is in {student['home']}")


# import csv

# students = []
# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "home": row["home"], "house": row["house"]})


# for student in sorted(students, key=lambda student: student['name']):
#   print(f"{student['name']} is in {student['house']}, from {student['home']}")



#### DATA
# name,house,home
# Yufus,Gryffindor,"teirladf, dfafloorddsf ds"
# Rene,Gryffindor,"fadsc, floord df"
# Kevin,Gryffindor,"jtrewjncv, dfloordfadsf d"
# Ofti,Gryffindor,"kdnf, floord 8"
# Lokri,Slytherin,"adiie, floord 0 "
# Alfhalad,Slytherin,"kant, floord 23"
# Zentu,Asfengard,"kanutdm, floord -"
# Borton,Yutenhaid,"eretc, floord 5"
# Zluturd,Britaheid,"trued, fllorrsdij 4" 






import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=['name', 'home'])
  writer.writerow({"home": home, "name": name})





