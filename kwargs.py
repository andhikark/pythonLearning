# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Putu", last="kurnia",middle="Andhika", )