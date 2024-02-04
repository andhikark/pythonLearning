# sort() method = used with lists
# sort() function = used with iterables

# students = ["F","H","A","Z","T"]
students = ("F", "H", "A", "Z", "T")

# students.sort(reverse=True)
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)

students2 = [("Zack", "F", 60),
             ("Bob", "B", 85),
             ("Lou", "A", 90),
             ("Kevin", "C", 70)]

grade = lambda grades: grades[1]
students2.sort(key=grade)

for i in students2:
    print(i)

students3 = (("Zack", "F", 40),
             ("Bob", "B", 25),
             ("Lou", "A", 80),
             ("Kevin", "C", 50))

age = lambda ages: ages[2]
sorted_3 = sorted(students3, key=age)

print("__________________________")
for i in sorted_3:
    print(i)
