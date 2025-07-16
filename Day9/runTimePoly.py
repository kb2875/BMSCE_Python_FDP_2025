class Mom:
    def cook(self):
        print("Indian cuisine")

class Daughter(Mom):
    def cook(self):
        print("Chinese cuisine")

m=Mom()
d=Daughter()
m.cook()
d.cook()
