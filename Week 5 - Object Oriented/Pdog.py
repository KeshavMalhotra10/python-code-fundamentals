class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    # Create a goldenRetriever class that inherits from the Dog class. Give the sound argument of GoldenRetriever.speak() a default value of "Bark".

class goldenRetriever(Dog):
    def speak(self, sound = 'bark'):
        return super().speak(sound)

john = goldenRetriever("john", 9)
print(john)

#print john.speak()  # Should print "john says bark"

print(john.speak())