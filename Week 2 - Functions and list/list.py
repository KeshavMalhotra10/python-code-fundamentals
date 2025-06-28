# a list is a collection which is ordered and changeable. Allows duplicate members.

my_list = ["apple", "banana", "cherry"]
print(my_list)

# To access a list item, we use the index number
print(my_list[1])  # Output: banana


#lists can be of any type
my_list2 = [1, 2, 3, 4, 5] #integers
my_list3 = [1.1, 2.2, 3.3] #floats
my_list4 = ["apple", "banana", "cherry"] #strings
my_list5 = [True, False, True] #Booleans

#lists can also be mixed
my_list6 = [0, "banana", 3.14, True]

#the type of list
print(type(my_list6))  # Output: <class 'list'>


#using the list constructor

newList = list(("Apple", "Orange", "Mango"))
print(newList)