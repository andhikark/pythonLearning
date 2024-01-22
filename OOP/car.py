class Car:
    #class variable = outside init inside class, like default value. But can change it
    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make    #instance variable
        self.model = model #instance variable
        self.year = year   #instance variable
        self.color = color  #instance variable

    def drive(self):
        print("This " + self.model + " car is driving")

    def stop(self):
        print("This " + self.model+" car is stopped")