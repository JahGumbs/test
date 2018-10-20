#!/usr/bin/env python3

def display_menu():
    print("The Wizard Inventory Program")
    print("============================")
    print()
    print("Welcome to the Wizard Inventory!")
    print("You start with 3 basic items and")
    print("can add, edit, or drop any item.")
    print("Can hold up to 4 items at a time.")
    print()
    print("COMMAND MENU")
    print("============")
    print("Type out the command you choose")
    print()
    print("view - View all the items in your inventory")
    print("add -  Add a new item to your inventory")
    print("edit -  Edit an item in your inventory")
    print("drop - Remove an item from your inventory")
    print("exit - Exit program")
    print()    

def list(item_list):
    if len(item_list) == 0:
        print("There are no item in the list.\n")
        return
    else:
        i = 0
        for item in item_list:
            print(str(i+1) + ". " + str(item))
                 
            i += 1
        print()

def add(item_list):
    name = input("Name: ")
    item = []
    if len(item_list) > 3:
        print("You can only hold up to 4 items at a time. Please drop an item first")
    else:
        item.append(name)
        item_list.append(item[0])
        print( item[0] + " was added.\n")

def edit(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.\n")
    else:    
        rename = str(input("New Name: "))
        item = item_list.pop(number-1)
        item_list.insert(number-1, rename)
        print(str(item) + " was renamed to " + str(rename))
     
    print()    
    
def drop(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.\n")
    else:
        item = item_list.pop(number-1)
        print(str(item) + " was deleted.\n")


    
                  
def main():
    item_list =[ "Magic Staff", "Black Spellbook", "Health Potion"]
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "view":
            list(item_list)
        elif command == "add":
            add(item_list)
        elif command == "edit":
            edit(item_list)
        elif command == "drop":
            drop(item_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
