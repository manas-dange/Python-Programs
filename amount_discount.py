amt = int(input("Enter sale amount"))
if amt>30000:
    discount = amt*0.20
elif amt>=20000:
    discount = amt*0.15
elif amt>=10000:
    discount=amt*0.10
else:
    discount=amt*0.05
