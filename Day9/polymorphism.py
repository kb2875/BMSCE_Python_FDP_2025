#Polymorphism concept

class India:
    def capital(self):
        print("New Delhi")

class USA:
    def capital(self):
        print("Washington DC ")

I=India()
U=USA()
I.capital()
U.capital()