#index operator [] = gives access to a swquence's element (str,list,tuples)

name = "Putu Andhika Restu Kurnia!"

if(name[0].isupper()):
    name = name.capitalize()

fname = name[:4].upper()
lname = name[5:].lower()
last_char = name[-1]
print(fname)
print(lname)
