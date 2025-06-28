import module
#importing a module using an alias
import module2 as m2

#import a specific function from a module
from math import sqrt

module.greeting("Keshav")


albert = module.person1

print(albert)

#get alberts age

print(albert['age'])


car = m2.car
print(car)
carModel = car['model']
print(carModel)


#using the dir() function to list all attributes and methods of a module
#print(dir(math))
#lets say we found the method 'sqrt' in the math module
#above we imported the sqrt function from math module 
print(sqrt(81))