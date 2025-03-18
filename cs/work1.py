year_group = input("Insert your input group: ")
grade = input("Insert your grade: ")
target = input("Insert your target: ")

if year_group == 11 and grade<target:
    print("You are admitted to revision class")
else:
    print("You are not admitted")