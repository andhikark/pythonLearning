#collection which is unordered, unindexed. no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()

dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes))
print(utensils.intersection(dishes))
for x in utensils:
    print(x)