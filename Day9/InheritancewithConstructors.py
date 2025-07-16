class parent:
    def __init__(self, name, age):
        #print("This is parent")
        self.name =name
        self.age =age
    def disp(self):
        print(f"name is:{self.name}")
        print(f"Age is:{self.age}")
class child(parent):
    def __init__(self, name, age, USN):
        super().__init__(name,age)
        self.USN=USN
    def disp(self):
        print(f"name is:{self.name}")
        print(f"Age is:{self.age}")
        print(f"USN is:{self.USN}")


c=child("Kiran", 50, 30)
c.disp()
p=parent("Guruprasad", 78)
p.disp()