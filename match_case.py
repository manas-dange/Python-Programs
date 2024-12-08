num = int(input("Enter a number"))
match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3 :
        print("Three")
    case _:
        print("Number is not between 1 to 3")
