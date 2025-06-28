#Sources: https://www.w3schools.com/python/python_tuples.asp
# Tuples are used to store multiple items in a single variable.
# Tuples are immutable, meaning they cannot be changed once created.
# Tuples are written with round brackets.

food = ('apple', 'banana', 'cherry')
print(food[1])

# tuples can have duplicates

food = ('apple', 'banana', 'cherry', 'apple')
print(food[0])
print(food[3])

#length of tuple

print(len(food))


#tuple with one item needs a comma after the first item

singleItem = ("apple", )
print(singleItem)

#using data consturctor


thisTuple = tuple(('apple', 'bananna', 'cherry'))
print(thisTuple)