#Single level Inheritance
class animal:
    def eat(self):
        print("Eating...")
class Dog(animal):
    def bark(self):
        print("Barking...")
class puppy(Dog):
    def cry(self):
        print("crying...")

A=animal()
D=Dog()
P=puppy()
A.eat()
D.eat()
D.bark()
P.eat()
P.bark()
P.cry()