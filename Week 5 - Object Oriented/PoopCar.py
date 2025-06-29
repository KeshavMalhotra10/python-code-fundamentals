'''
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer
Then create two Car objects—a blue car with twenty thousand miles and a red car with thirty thousand miles—and print out their colors and mileage. 

Your output should look like this:
The blue car has 20,000 miles
The red car has 30,000 miles

'''

class car:
    def __init__(self, colour, miles):
        self.colour = colour
        self.miles = miles 
    
    def __str__(self):
        return f"The {self.colour} car has {self.miles} miles"
    

blue = car('blue', '20,000')
red = car('red', "30,000")

print(blue)
print(red)

        
        