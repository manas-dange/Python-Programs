e = int(input("Enter a year"))
if e%400 == 0 or e%4 == 0 and e%100!=0:
    print("leap year")
else:
    print("not a leap year")
