"""Instance variables are for data unique to 
each instance and class variables 
are for attributes and methods shared by all instances of the class:"""
class Animals:
    kind = 'Canine'   #class variable shared by all instances

    def __init__(self, name, owner):
        self.name = name   # class variable unique to each instance
        self.owner = owner # class variable unique to each instance
        
d = Animals('Dog', 'John')
e = Animals('Cat', 'Doe')

print(d.kind)
print(d.name)
print(e.kind)
print(e.owner)
print(d.owner)
print(e.name)