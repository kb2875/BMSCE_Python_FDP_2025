m1=int(input("Enter the Marks1:"))
m2=int(input("Enter the Marks2:"))
m3=int(input("Enter the Marks3:"))
m4=int(input("Enter the Marks4:"))
totalMax=400

if m1 > 35 and m2 >35 and m3 >35 and m4 > 35:
    Pass=1
    print(Pass)
else:
    Pass=0
    print(Pass)

Percentage = (m1+m2+m3+m4/400)*100

if Percentage >= 75 and Pass==1:
    print("A")
elif Percentage >=50 and Pass==1:
    print("B")
elif Percentage>=30 and Pass==1:
    print("C")
else:
    print("F")
