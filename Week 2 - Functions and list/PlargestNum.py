#find the largest number in a list


def largestNum(): 
    #get user in put 
    userInput = input("Enter numbers seperated by commas: ")
    #convert string into a list of numbers 
    userInputList = userInput.split(",")
    #convert list of strings into list of integers
    userInputList = [int(i) for i in userInputList]
    #find the largest number using max function
    largestNumber = max(userInputList)
    print(largestNumber)


largestNum()