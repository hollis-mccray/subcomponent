from data import *

def menu():
    options = {
        "B": "Base Item",
        "R": "Recipes",
        "S": "Shopping List",
        "E": "Error Report",
        "X": "Exit"
    }
    choice = '?'
    while choice not in options:
        print("Subcomponent Problem Managers")
        print()
        for key, value in options.items():
            print(f"{key}. {value}")
        print()
        choice = input("Select an Option: ").upper()
    return choice


def main():
    item_data = item_list()
    option = menu()
    while option != "X":
        match option:
            case "B":
                print("\nBase Items..\n")
            case "R":
                print("\nRecipes...\n")
            case "S":
                print("\nShopping List...\n")
            case "E":
                print("\nError Report...\n")
        option = menu()

main()