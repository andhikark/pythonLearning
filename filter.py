# filter() = creates a collection of elemetns from an iterable for which a function returns

# filter(function, iterable)

friends = [("rachel", 19),
            ("monica", 18),
            ("phoebe", 17),
            ("joey", 16),
            ("chandler", 21),
            ("ross", 20)
           ]

age = lambda data: data[1] >=19

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)