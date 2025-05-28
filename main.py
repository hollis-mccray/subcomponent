from data import *
from item_management import itemManager

def menu():
    options = {
        "I": "Items",
        "S": "Shopping List",
        "E": "Error Report",
        "X": "Exit"
    }
    choice = '?'
    while choice not in options:
        print()
        print("Subcomponent Problem Helper")
        print()
        for key, value in options.items():
            print(f"{key}. {value}")
        print()
        choice = input("Select an Option: ").upper()
    return choice


def main():
    item_data = ItemList()
    option = menu()
    while option != "X":
        match option:
            case "I":
                itemManager(item_data)
            case "S":
                print("\nShopping List...\n")
            case "E":
                print("\nError Report...\n")
        option = menu()

main()