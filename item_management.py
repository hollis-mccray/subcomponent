
def itemManager(item_data):
    options = {
        "N": "New Item",
        "E": "Edit Item",
        "X": "Main Menu"
    }
    choice = '?'
    while choice != "X":
        print()
        print("Item Management")
        print()
        for key, value in options.items():
            print(f"{key}. {value}")
        print()
        choice = input("Select an Option: ").upper()
        match choice:
            case "N":
                addItem(item_data)
            case "E":
                print("\nEdit Item...\n")

def addItem(item_data):
        print()
        print("Create New Item")
        print()
        name = input("Enter new item name: ")
        if item_data.getItem(name) is not None:
            print("Item already exists.")
            choice = input("Edit the existing item (Y/N): ").upper()
            if choice ==  "Y":
                editItem(item_data, name)
        else:
            print("New Item")

def editItem(item_data, name):
    print("Editing " + name)