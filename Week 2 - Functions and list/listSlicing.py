a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#get elements from index 1-4 (this does not include index 4 )
print(a[1:4]) #Parameters: start, end, step 


#retreive all elements in a list:
print(a[:])

#retreive all elements starting index 2 
print(a[2:])

#retreive all elements to index 5(exluding index 5)
print(a[:5])

def odd_numbers():
    #returns all odd numbers in a list
    print(a[0::2])

odd_numbers()
 


#negative indexing, returns the last indexes

food = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(food[-1]) #output mango

print(food[-2]) # output kiwi




#Reverse a list using slicing

c = [10,20,30,40,50,60,70,80,90,100]
print(c[::-1])