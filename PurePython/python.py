def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


#This section is to test the function of the __init__ ()method
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, 4.5)
print(x.r, x.i)

class Myclass:
    """This is just a simple class too"""
    counter = 1234
    def f(self):
        return("The first real class")
y = Myclass()
y.counter = 1
while y.counter < 10:
    y.counter *= 2
print(y.counter)
del y.counter
