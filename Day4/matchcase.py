fruit= input("enter the fruit")
match fruit:
    case "Apple":
        print("you have an apple")
    case "mango":
        print("you have a mango")
    case "banana":
        print("you have a banana")
    case _:
        print("unknown fruit")

