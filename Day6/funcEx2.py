def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if(b==0):
        print(" DIV by zero")
        return 0
    else:
        return a/b

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
while(True):
    option=int(input("Enter the operation\n1.add \n2. sub \n3. Mul \n4. Div \n5.Exit\n"))
    match option:
        case 1:
            print(add(num1,num2))

        case 2:
            print(sub(num1, num2))

        case 3:
            print(mul(num1, num2))

        case 4:
            print(div(num1, num2))

        case 5:
            exit(0)
        case _:
            print("Invalid option")

