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


"""How to add a list to a class for a specific instance and not all of them at one"""
class Dogs:
    def __init__(self, name): 
        self.name =  name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

j = Dogs('Bruno')
j.add_trick("roll over")
j.add_trick("jump and turn upside down")

k = Dogs('slyvia')
k.add_trick("fly over the wheel")

print(j.name, j.tricks)
print(k.name, k.tricks)



class People:
    def __init__(self, name, character):
        self.name = name
        self.character =  character

h = People('Mary', 'Good')

print(h.name, h.character)