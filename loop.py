
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

import time

for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):
    print(i)

for i in "Putu Andhika":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year")