class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("Driving 🚗 - classes.py:6")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️ - classes.py:10")

class Dog:
    def move(self):
        print("Running 🐕 - classes.py:14")

class Fish:
    def move(self):
        print("Swimming 🐟 - classes.py:18")

vehicles_and_animals = [Car(), Plane(), Dog(), Fish()]

for item in vehicles_and_animals:
    item.move()
