# number = 10 
# if number >5:
#     print("Number is greater than 5")

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# age =  int(input("Enter your age: "))
# if age in range(0,13):    #range don't include 13 better to write age<13 for avoiding off-by-one error
#     print("Child")
# elif age in range(13,20):      #range don't include 20
#     print("Teenager")
# elif age in range(20,60):      #range don't include 60
#     print("Adult")
# elif age >= 60:
#     print("Senior")
# else:
#     print("invalid Entry!")

# temp = int(input("Enter the Temperature: "))
# if temp > 30 and temp < 40:          # can chain write 30 < temp < 40
#     print("Warm day!")
# elif temp >= 40:
#     print("Very hot!")
# else :
#     print("Not warm.")

# for i in range(1,11):
#     print(i)

# for i in range(2,21,2):
#     print(i)

# count = 10
# while count > 0:
#     print(count)
#     count -= 1

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1,101):
#     print(i)

# for i in range(1,51):
#     if i % 2 == 1:
#         continue
#     print(i)

# num = int(input("Enter a Number: "))
# for i in range(1,11):
#     print(num ,"x", i ,"=", num*i)

# word = str(input("Enter a Word: "))
# for i in word:
#     print(i)

# total = 0
# while True:
#     i = str(input("Enter a number (or 'stop'): "))
#     if i.lower() == "stop":
#         break
#     total += int(i)
# print("Total sum = ",total)

# MINI- PROJECT

import random

secret = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("Enter your guess: "))
    attempt += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! The number was", secret)
        break
print("You guessed in ",attempt," attempts")