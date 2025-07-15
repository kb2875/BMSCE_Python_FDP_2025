m1=int(input("Enter the Marks1:"))
m2=int(input("Enter the Marks2:"))
m3=int(input("Enter the Marks3:"))
m4=int(input("Enter the Marks4:"))
totalMax=400
if m1>0 and m1<100:
    print("M1 valid")
    valid = 1
else:
    print("M1 invalid")
    valid = 0

if m2 > 0 and m2 < 100:
    print("M2 valid")
    valid = 1
else:
    print("M2 invalid")
    valid = 0

if m3 > 0 and m3 < 100:
    print("M3 valid")
    valid =1
else:
    print("M3 invalid")
    valid =0

if m4 > 0 and m4 < 100:
    print("M3 valid")
    valid =1
else:
    print("M3 invalid")
    valid=0

if(valid==0):
    print ("Not valid")
else:
    if m1 > 35 and m2 > 35 and m3 > 35 and m4 > 35:
        Pass=1
        print(Pass)
        Percentage = (m1 + m2 + m3 + m4 / 400) * 100
        if Percentage >= 75 and Pass == 1:
            print("A")
        elif Percentage >= 50 and Pass == 1:
            print("B")
        elif Percentage >= 30 and Pass == 1:
            print("C")
        else:
            print("F")
    else:
        Pass=0
        print(Pass)
