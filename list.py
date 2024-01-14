
food = ["pizza", "hamburger", "hotdog", "spaghetti"]

food[0] = "sushi"

food.append("Ice Cream") #add item in the back of the list
food.remove("hotdog") #remove specific item in list
food.pop() #remove item in the back
food.insert(0,"cake")
food.sort()
for x in food:
    print(x)

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food1 = [drinks,dinner, dessert]

print(food1[0][1])
print(food1[1][2])

