class Calculator():
    def __init__(self, num1, operation, num2):
        if operation == '+':
            print(num1+num2)
        elif operation == '-':
            print(num1-num2)
        elif operation == '/':
            print(num1/num2)
        elif operation == '*':
            print(num1*num2)

x = Calculator(14, '/', 2)
print(x)