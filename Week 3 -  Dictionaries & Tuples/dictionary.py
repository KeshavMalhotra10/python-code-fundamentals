#source: https://www.w3schools.com/python/python_dictionaries.asp
#stores data in key-value pairs


carDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(carDict["model"])
#accessing specific key-value pair

#dictionaries cannt have duplicate keys


carDict2 = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964,
    'year': 2020 #this will override the previous 'year' key because no duplicates allowed
     
}

print(carDict2["year"])


#determine length of carDict2
print(len(carDict2))


#using dict constructor

nameDict = dict(name = "John", age = 30, country = "Romania")
print(nameDict)