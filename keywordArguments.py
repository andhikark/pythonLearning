# arguments preceded by an identifies when we pass the to a function
# the order of the arguments doesnt matter, pyhton knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="andhika",first="Kurnia",middle="Putu")