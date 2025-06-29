#inheritance allows us to create a new class that is a modified version of an existing class, inheriting its attributes and methods
#create a child class by creating a class and passing the parent class as an argument


class parent:
    hair_colour = 'brown'
    def __init__(self, name, age):
        self.name = name
        self.age = age



class child(parent):
    pass

print(child.hair_colour)
#will pass 'brown" as it inherited data from parent class


mary = child('mary', 5)
rose = child('rose', 3)

print(mary.name + " is " + str(mary.age) + " years old" + " and has " + mary.hair_colour + " hair!")
print(rose.name + " is " + str(rose.age) + " years old" + " and has " + rose.hair_colour + " hair!")