# lambda function = function written in 1 line using lambda keyword
#                 accepts anyn number of arguments, but only has one expression.
#                 like a short cust, useful if needed for a short period of time

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(double(2))
print(multiply(2,3))
print(add(2,3,4))
print(full_name("andhika", "restu")) 
print(age_check(19))