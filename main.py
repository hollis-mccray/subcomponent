from sources import options

def menu():
    options = {
        "A": "Add Recipe",
        "E": "Error Report",
        "X": "Exit"
    }
    choice = '?'
    while choice not in options:
        print("Foundry Subcomponent Manager")
        print()
        for key, value in options.items():
            print(f"{key}. {value}")
        print()
        choice = input("Select an Option: ").upper()
    return choice


def main():
    option = menu()
    while option != "X":
        match option:
            case "A":
                print("\nAdding Recipe...\n")
            case "E":
                print("\nPrinting Error Report...\n")
        option = menu()

main()