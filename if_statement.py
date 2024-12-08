x = 10
if x == 10:
    print("x is equal to 10")
ch1 = input("Enter a single character")
if ch1>='0' and ch1<='9':
    print("You entered a digit")
n1,n2 = map(int, input("Enter two integers").split())
if(n1%n2==0):
    print(f'{n1} is divisible by {n2}')
else :
    print(f'{n1} is not divisible by {n2}')
