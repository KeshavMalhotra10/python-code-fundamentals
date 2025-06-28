#to-do list with save/load


list = []
tickList = []
def todo():
    #take user input to add, tick, or view
    while True:
        userInput = input("type add, tick, view, or exit: ").lower()
        if userInput == 'add':
            add = input("Add todo: ").lower()
            list.append(add)
            print(add + " added!")
        if userInput == 'tick':
            tick = input("What do you want to tick: ").lower()
            found = False
            for todo in list:
                if todo == tick:
                    list.remove(todo)
                    print(todo + " has been accomplished!")
                    tickList.append(todo)
                    found = True
                    break
            if not found:
                print("todo not found in list!")
                repeat = input("continue the todoList, y/n: ").lower()
                if repeat == 'y':
                    todo()
                elif repeat == 'n':
                    print("thanks for using this app")
                    break
                else: 
                    print("You entered an invalid input, going back to main options ")
                        
                        
        if userInput == 'view':
            print("Here is what is on your list: ")
            print()
            for i in list:
                print(i)
            print("Here is what you have accomplished: ")
            print()
            for x in tickList:
                print(x)

        if userInput == 'exit':
            print()
            print("Exiting the program!")
            break


todo()




            
