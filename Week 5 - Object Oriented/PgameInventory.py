#make a game inventory using oop:

class gameInventory: 
    def __init__(self, inventoryNumber, inventoryItems ):
        self.inventoryNumber = inventoryNumber
        self.inventoryItems = inventoryItems
    
    def add(self, item):
        self.inventoryItems.append(item) 
        print("You have added " + str(item))
    
    def remove(self, item):
        self.inventoryItems.remove(item)
        print("You have removed  " + str(item))
        
    
    def view(self):
        print(f"Inventory Number: " + str(self.inventoryNumber))
        print(f"Inventory Items: " + str(self.inventoryItems))


john = gameInventory(1, ["apple"])
john.view()
john.add("mango")
john.add("mushrooms")
john.add('sword')
john.view()