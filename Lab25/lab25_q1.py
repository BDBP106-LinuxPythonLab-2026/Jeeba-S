class Car:
    def __init__(self, make, model, year, color, started=False,speed=0,max_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = started
        self.speed = speed
        self.max_speed = max_speed
    showroom="NewAge"
    @classmethod
    def showroom_change(cls,new_name):
        cls.showroom = new_name

    @staticmethod
    def show_intro_message():
        print("this class represents a car")

    #magic method
    def __str__(self):
        return f"{self.make} {self.model} {self.color} {self.year}"

print("PART A")
toyota_camry=Car("Toyota","Camry","2022","Red")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.started)
print(toyota_camry.speed)
print(toyota_camry.max_speed)

print("PART B")
ford_mustang=Car("Ford","Mustang","2022","Black")
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)
print(ford_mustang.started)
print(ford_mustang.speed)
print(ford_mustang.max_speed)

print("PART C")
try:
    print(Car.make)
except AttributeError as error:
    print("ERROR",error)
    print("USE AN OBJECT TO ACCESS THE ATTRIBUTE")
print(toyota_camry.make)

print("PART D")
print(Car.__dict__)

print("PART E")
Car.showroom_change("premium")
print(Car.showroom)
print(Car.__dict__)

print("PART F")
print(toyota_camry.__dict__)

print("PART G")
print(str(toyota_camry))

print("PART H")
Car.show_intro_message()



