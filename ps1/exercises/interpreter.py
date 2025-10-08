# expression = input("Expression: ").split()

# calculate = int(expression[0]) 



# if expression[1] == "+":
#   print(float(int(expression[0]) + int(expression[2])))
# elif expression[1] == "-":
#   print(float(int(expression[0]) - int(expression[2])))
# elif expression[1] == "*":
#   print(float(int(expression[0]) * int(expression[2])))
# else:
#   if expression[2] == "0": print("Error: dividion by zero")
#   else: print(float(int(expression[0]) / int(expression[2])))





expression = input("Expression: ").split()
a, operator, b = expression
a, b = float(a), float(b)

operations = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": a / b if b != 0 else "Error: division by zero"
}

print(operations.get(operator, "Invalid operator"))




# import operator

# ops = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }

# a, op, b = input("Expression: ").split()
# a, b = float(a), float(b)

# if op in ops:
#     try:
#         print(ops[op](a, b))
#     except ZeroDivisionError:
#         print("Error: division by zero")
# else:
#     print("Invalid operator")