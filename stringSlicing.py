#slicing = create substring by extracting eleemnts from another string
#          indexing[] or slice()
#           [start:stop:step] 

name = "putu andhika restu kurnia"

fname = name[:4]
lname = name[5:12]

funky_name = name[::2] #[0:end:2]
reversed_name = name[::-1] #reverse

print(fname)
print(lname)
print(funky_name)
print(reversed_name)

website = "http://google.com"

slice = slice(7, -4)
print(website[slice])