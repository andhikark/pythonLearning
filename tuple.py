# collction which is ordered and unchangeable used to group together related data
student = ("Andhika", 19, "male")

print(student.count("Andhika"))
print(student.index("male"))

for x in student:
    print(x)

if "Andhika" in student:
    print("Andhika is here")