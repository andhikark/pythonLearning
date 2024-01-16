name = "Bro " #global (avail inside & outside functions)

def display_name():
    name = "Code "  #local scope (available only inside this function)
    print(name)


display_name()
print(name)