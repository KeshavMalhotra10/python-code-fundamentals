#write a function that filters through even numbers

def evenNumber():
    #get user input
    userInput = input("Enter numbers seperated by commas: ")
    #convert input to strList 
    userInputList = userInput.split(",")
    #convert stringlist to intlist
    userInputList = [int(i) for i in userInputList]
    evenList = []
    for i in userInputList:
        if i % 2 == 0:
            evenList.append(i)
    print(evenList)
    
    
evenNumber()