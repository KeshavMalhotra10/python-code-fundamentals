#to-do list with save/load
import json
todo_list = []
completed_list = []

#SAVE
def saveData():

    data = {
        'todo': todo_list,
        'done': completed_list
    }
    with open('todo_data.json', 'w') as f:
        json.dump(data, f)
        print("\n Data saved successfully!")

#LOAD
def loadData():
    global todo_list, completed_list
    try: 
        with open('todo_data.json', 'r') as f:
            data = json.load(f)
            todo_list = data.get('todo', [])
            completed_list = data.get('done', [])
            print("\n Data loaded successfully!")
    except FileNotFoundError:
        print("\n No file saved! Starting anew!")



def todo():
    loadData()
    #take user input to add, tick, or view
    while True:
        print()
        userInput = input("type add, tick, view, or exit: ").lower()
        if userInput == 'add':
            print()
            add = input("Add todo: ").lower()
            todo_list.append(add)
            print()
            print(add + " added!")
        if userInput == 'tick':
            print()
            tick = input("What do you want to tick: ").lower()
            found = False
            for todo in todo_list:
                if todo == tick:
                    todo_list.remove(todo)
                    print()
                    print(todo + " has been accomplished!")
                    completed_list.append(todo)
                    found = True
                    break
            if not found:
                print("todo not found in list!")
                print()
                repeat = input("continue the todoList, y/n: ").lower()
                if repeat == 'y':
                    print('continuing')
                elif repeat == 'n':
                    print("thanks for using this app")
                    break
                else: 
                    print("You entered an invalid input, going back to main options ")
                        
                        
        if userInput == 'view':
            print()
            print("Here is what is on your list: ")
            print()
            for i in todo_list:
                print(i)
            print()
            print("Here is what you have accomplished: ")
            print()
            for x in completed_list:
                print(x)

        if userInput == 'exit':
            print()
            print("Exiting the program!")
            break


todo()




            
