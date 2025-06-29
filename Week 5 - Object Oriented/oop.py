#source: https://realpython.com/python3-object-oriented-programming/
#object oriented progrmamming allows us to create classes that can be used to create objects
#the four key concepts of OOP are encapsulation, abstraction, inheritance, and polymorphism
#you create an object by instantiating a class(creating an instance of a class), simply by calling the class name as if it were a function using parentheses 
#class inheritance allows us to create a new class that is a modified version of an existing class, inheriting its attributes and methods
#super() allows us to call the parent class's methods and attributes from the child class, allowing us to extend or modify the behavior of the parent class


#encapsulation: bundle data(attributes) and behaviours(method) into a single unit
#inheritance: create a new class that is a modified version of an existing class, inheriting its attributes and methods
#abstraction: hide the implementation details of a class and expose only the necessary parts to the user
#polymorphism: allow different classes to be treated as instances of the same class through a common interface, enabling code reuse and flexibility

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #note: self is a reference to the current instance of the class, allowing us to access its attributes and methods


#classes allow you to make user-defined data structures
#they define functions call methods that can be used to manipulate the data
#classes are general, they dont have any data, they are simply blueprints
#instances are the actual objects created from the class, they have their own data and can use the methods defined in the class

#in other words, class is an empty form with questions, instances are the filled forms with answers

class dog:
    #class attribute is shared by all instances of the class

    species = "Canis familiaris"  # class attribute, shared by all instances

    #pass, allows compiler to skip the class body, useful when you want to define a class but don't want to add any attributes or methods yet
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance methods
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}."


#instantiate a class(create an object from the class):
hudson = dog("hudson", 5) # create an instance of the dog class
miles = dog('miles', 3)
#print(miles.age)#accessing the instance's attributes
#print(miles.name)
#print(miles.species) #accessing the class attribute, shared by all instances

#however these values are dynamic, meaning you can change them

miles.age = 4
#print(miles.age)
miles.species = "Felis catus"  # changing the class attribute for this instance only
#print(miles.species) 


#try using he instance method functions
#print(miles.description())
#print(miles.speak("Woof!"))


print(miles) #we changed the first instance method to __str__, so it will be called when we print the instance

#learn more about dunder methods such as __str__ and __init_ in https://docs.python.org/3/reference/datamodel.html#object.__init__