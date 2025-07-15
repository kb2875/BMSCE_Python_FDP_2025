#cond=True
while True:
    ans=int(input("1.Say Hello \n2.Say Bye \n3.Say Exit: \n") )
    match ans:
        case 1:
            print("Hello")
        case 2:
            print("Bye")
        case 3:
            print ("ok see you")
            break
        case _:
            print("Invalid option")

