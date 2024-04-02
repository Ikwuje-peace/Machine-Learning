print('\n Input the first number')
first_number = input()
fnum = int(first_number)
oper = input(str('Input the Operator '))
print('\n Input the second number')
second_number = input()
snum = int(second_number)
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

x = Calculator(fnum, oper, snum)
print(x)