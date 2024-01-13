#variable = container for a value

#String
fname = "Andhika"
lname = "Restu"
full_name = fname + " " + lname

print(type(fname)) #define var type
print("hello" + full_name) #type cast = manually cast type

# #int
age = 20
age += 1
print(type(age))
print("your age is " + str(age))

# #float
height = 182.5
print(type(height))
print("your high is " + str(height) + "cm")

# #boolean
human = False
print(type(human))
print("are you a human? " + str(human))

#type casting
f = 5.4
s = "11"
i = 2

f = int(f) #if u want permanently change, need to initialize again
print(f)
print(int(s) * 3)
print(int(s) * i)



