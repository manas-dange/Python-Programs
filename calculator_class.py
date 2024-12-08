class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def division(self,a,b):
        if b!=0:
            return a/b
        else:
            return "NA"
calc = Calculator()
print(f"Add: {calc.add(10, 5)}")
print(f"Subtract: {calc.sub(10, 5)}")
print(f"Multiply: {calc.multiply(10, 5)}")
print(f"Divide: {calc.division(10, 5)}")
