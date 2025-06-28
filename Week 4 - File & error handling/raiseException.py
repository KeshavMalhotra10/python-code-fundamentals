#Raising an exception 
'''x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
'''

#raise a TypeError if x is not an integer:

y = 'hello'
if not type(y) is int:
    raise TypeError("Only integers are allowed")