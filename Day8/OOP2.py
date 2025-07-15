#class with attributes
#When there are attributes we need to create a constructor
class student:
    def __init__(self, name, USN): #constructor
        self.name=name
        self.USN=USN
    def Display(self):
        print("Name is:",self.name, "USN is:",self.USN)

s1=student("Kiran", 30)
s2=student("Ananth", 19)
s2.Display()
s1.Display()
