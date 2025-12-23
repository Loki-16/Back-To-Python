# print("Hello, AI Developer !")

# name = "Sam"
# age = 21
# height = 5.9
# is_student = True

# print(name,age,height,is_student)

# username = input("Enter your name: ")
# print("welcome,", username)

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print("Sum:", num1 + num2)

# # task 1: 
# print("Lokesh Ijardar", "Age 25","Place Raigarh")

# # task 2:
# num = int(input("Enter a Number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# # task 3:
# C = float(input("Enter Temprature in Celcius: "))
# F = float(C * (9/5) + 32)
# print(F)

# # task 4:
# a =  int(input("Enter a Number: "))
# b =  int(input("Enter another Number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

#  Mini-project: Calculator

print("=== Simple Calculator ===")

num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

print("Choose an operation: + - * / ** %")
op = str(input("Enter operation: "))

if op == "+":
    result = num1 +num2
elif op == "-":
    result = num1-num2
elif op == "*":
    result = num1*num2
elif op == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result = "Error: Cannot divide by zero."
elif op == "**":
    result = num1**num2
elif op == "%":
    result = num1%num2
else:
    result = "Invalid operation."

print("Result: ", result)