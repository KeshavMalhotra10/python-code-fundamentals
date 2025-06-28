#source: https://www.w3schools.com/python/python_sets.asp
# Sets are used to store multiple items in a single variable.
# Sets are unordered, meaning that the items have no index.
# Sets are unchangeable, meaning that you cannot change, add or remove items once the set is created.
# Sets are written with curly brackets.
# Sets cannot have duplicate items.

foodSet = {'banana', 'grape', 'apple'}

print(foodSet)

#true and 1 and  0 and false are same in set 


trueFalse = {True, False, 1, 0}
print(trueFalse)

#check length of set


print(len(foodSet))

#using data constructor
newSet = set(('apple', 'banana', 'cherry'))