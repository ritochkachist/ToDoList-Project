# 7/13/2023
# Margarita Chistiakova
  
toDoList = []
def modifyItem(item): 
    index = toDoList.index(item)
    print(f"Enter the new value for item '{item}':")
    newItem = input()
    toDoList[index] = newItem

choice = 0
while choice != 5:
  print("""\nPlease choose an option from the menu below: 
  1. Add an item to the list
  2. Remove an item from the list
  3. Edit an item in the list 
  4. Print out your list
  5. Quit the program\n""")

  choice = int(input())
  
  if choice == 1:
    print("Please enter an item to be added to the list: ")
    item = input()
    toDoList.append(item)
    with open("ToDo.txt", "a") as f:
        f.write(item + "\n")
      
  elif choice == 2:
    print("Please enter an item to be removed from the list: ")
    item = input()
    if item in toDoList:
        toDoList.remove(item)
        with open("ToDo.txt", "r") as f:
            lines = f.readlines()
        with open("ToDo.txt", "w") as f:
            for line in lines:
                if line.strip() != item:
                    f.write(line)
    else:
        print(f"'{item}' is not in the list.")
      
  elif choice == 3:
    print("What is the item you want to modify?")
    item = input()
    if item in toDoList:
        modifyItem(item)
        with open("ToDo.txt", "w") as f:
            for item in toDoList:
                f.write(item + "\n")
    else:
        print(f"'{item}' is not in the list.")
      
  elif choice == 4:
    f = open("ToDo.txt", "r")
    print(f.read())
    f.close()
    
  elif choice == 5:
    exit()
    
  else:
    print("We don't have such an option in the menu! Please try to choose something different.")
    