
age = int(input("How old are you? "))

if age == 100:
    print("You are century old")
elif age >= 18:
    print("You are legally to drink beer")
elif age < 0:
    print("Wow how can you have minus age")
else:
    print("please enter correctly ")

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("teh temperature is good today!")
elif (temp < 0 or temp > 30):
    print("the temperature is bad today!")