# duck typing = concept where the class of an object is less importhan than the methods/attributes
#               class type is not checked if miniimum methods/attributes are present
#               "If it walks like a duc, and it quaccks like a duck, then it must be duck."

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken  is qwuacking")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

Person.catch(person,chicken)