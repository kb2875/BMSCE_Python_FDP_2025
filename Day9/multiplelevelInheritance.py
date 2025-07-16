class Mom:
    def cook(self):
        print("cooking...")

class Dad:
    def sleep(self):
        print("sleeping...")

class child(Mom, Dad):
    def study(self):
        print("studying..")

d=Dad()
m=Mom()
c=child()
c.cook()
c.sleep()
c.study()
