# word = str(input("Enter the word: "))
# print(word[0])
# print(word[-1])
# print(word[::-1])
# print(word[0:3])

# sent = input("Enter the sentence: ")
# print(sent.lower())
# print(sent.upper())
# print(len(sent))
# print(sent.lower().count("a"))

# word = input("Enter the sentence: ")
# print(word.replace(" ","-"))

# nums = [10,67,43,78,99]
# print(nums[0])
# print(nums[-1])
# print(sorted(nums))
# print(nums[::-1])
# nums.append(15)
# print(nums)

# names = ["Lokesh","Ashu","Yash","Neha","Chanchal"]
# length = len(names)
# for i in range(0,length):
#     print(names[i])
# print("Total names: ",length)
# for i,name in enumerate(names):
#     print(i, ":", name)
# for i in range(0,length):  #my solution
#     print(i,":", names[i])

# names = [10,20,30,40,50]
# names.remove(names[2])   #or del names[2]
# names.insert(2, 25)
# names[-1] = 45
# print(names)

# info = {"name": "Lokesh","age":25,"city": "Raigarh","profession":"Student"}
# print(info["name"],"\n",info["age"])
# info["Profession"] = "Student"
# info["city"] = "Pune"
# print(info)

# for key in info:
#     print(key)
# for value in info.values():
#     print(value)
# for key,value in info.items():
#     print(key,":",value)

# info = {"name": "Lokesh","age":25,"city": "Raigarh","profession":"Student"}
# del info["city"]
# if "age" in info:
#     print("Age key found")
# else:
#     print("Age key not found")
# info["country"] = "India"
# print(info)

# # Task 1
# info = {"brand": "Apple", "model": "iPhone 15", "price": 799}
# for value in info.values():
#     print(value)
# # Task 1 done
# # Task 2
# info = {"name": "Lokesh","marks": 98,"subject": "Maths"}
# info["marks"] = 67
# info["passed"] = True
# print(info)
# # Task 2 done
# # Task 3
# info = {"name": "Lokesh","marks": 98,"subject": "Maths"}
# if "name" in info:
#     print("Found")
# else:
#     print("Not found")
# # Task 3 done

# MINI-PROJECT

task_s = []
while True:
    print("\n1. Add task.")
    print("2. View tasks.")
    print("3. Remove task.")
    print("4. Exit.")
    choice = input("\nEnter choice: ").strip()
    if choice == "1":
        task = input("Enter Task: ").strip()
        task_s.append(task)
        print("Task added!")
    elif choice == "2":
        if not task_s:
            print("No tasks available.")
            continue
        for i,task in enumerate(task_s, start=1):
            print(i ,":", task)
    elif choice == "3":
        task = int(input("Enter task number: ").strip())
        if not task_s:
            print("No tasks available.")
            continue
        if 1 <= task <= len(task_s):
            task_s.pop(task-1)
            print("Task number ",task, "removed.")
        else:
            print("Task doesn't exist yet.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("\nInvalid Choice!")
