#user enters a list
#make a function that takes the sum of the list 

def sum(): 
    #take user input
    userInput = input("enter a list of numbers seperated by commas: ")
    #convert string into a list of numbers
    userInputList = userInput.split(",")
    #add a sum value OUTSIDE LOOP
    sum = 0
    for i in userInputList:
        sum += int(i)
    print("Sum of the list is:", sum)  
        





sum()