class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

    def eat(self):
        print("The rabbit is eating")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Eagle(Animal):
    def fly(self):
        print("This eagle is flying")


rabbit = Rabbit()
fish = Fish()
eagle = Eagle()

print(rabbit.alive)
rabbit.eat()
fish.eat()
eagle.sleep()
rabbit.run()
fish.swim()
eagle.fly()
