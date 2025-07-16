class animal:
    def eat(self):
        print("Eating...")
class Dog(animal):
    def bark(self):
        print("Barking...")
class cat(animal):
    def meow(self):
        print("Mewing...")

A=animal()
D=Dog()
C=cat()
A.eat()
D.eat()
D.bark()
C.eat()
C.meow()
