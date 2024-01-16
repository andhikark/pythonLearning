#method that gives user more control when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal,item))
print("them {1} jumped over the {0}".format(animal,item)) #positional argument
print(f"The {animal} jumped over the {animal}".format(animal="cow",item="moon")) #Keywords argument

text = "the {} jumped over the {}"
print(text.format(animal,item))

name = "bro"

print("hello, my name is {}".format(name))
print("hello, my name is {0:10}".format(name)) #add pading by 10
print("hello, my name is {:<10}".format(name)) # left align
print("hello, my name is {:>10}".format(name)) # right align
print("hello, my name is {:^10}".format(name)) # justify

number = 10000
num1 = 3.1459

print("THe number pi is {:.3f}".format(num1)) #show decimal point
print("The number is {:,}".format(number)) #add ,
print("The number is {:b}".format(number)) #change to binary
print("The number is {:o}".format(number)) # change to octet
print("The number is {:X}".format(number)) # change to hexadecimal
print("The number is {:E}".format(number)) # change to scientific notation