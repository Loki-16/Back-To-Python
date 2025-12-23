# def greet():
#     print("Hello welcome to Day 4!")

# greet()
# greet()

# def greet_user(name):
#     print("Hello,", name)

# greet_user("Lokesh")

# def add(a,b):
#     return a+b

# result = add(5,11)
# print(result)

# def introduce(name, age, city):
#     print(f"{name} is {age} years old and lives in {city}")

# introduce(name = "Lokesh",age = 25,city = "Raigarh")
# import math
# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime")
# else:
#     print("Not Prime")

# def factorial_iter(n):
#     if n == 0:
#         return 1
#     product = 1
#     for i in range(1,n+1,1):
#         product = product * i
#     return product
# def factorial_rec(n):
#     if n == 0:
#         return 1
#     return n * factorial_rec(n-1)

# print(factorial_iter(5))
# print(factorial_rec(5))


task_s = []
def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    print("Task added!")
def view_tasks(tasks: list) -> None:
    if not tasks:
        print("No tasks available.")
    for i,task in enumerate(tasks, start=1):
        print(i ,":", task)
def remove_task(tasks: list, task: int) -> bool:
    if 1 <= task <= len(tasks):
        tasks.pop(task-1)
        return True
    else:
        return False
def main() -> None:
    while True:
        print("\n1. Add task.")
        print("2. View tasks.")
        print("3. Remove task.")
        print("4. Exit.")
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            task = input("Enter Task: ").strip()
            add_task(task_s,task)
        elif choice == "2":
            view_tasks(task_s)
        elif choice == "3":
            if not task_s:
                print("No tasks available to remove.")
                continue
            task = int(input("Enter task number: ").strip())
            if remove_task(task_s,task):
                print("Task Success!")
            else:
                print("Task Failed")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid Choice!")

if __name__ == "__main__":
    main()