def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Initialize an empty shopping list
    shopping_list = []
    
    while True:
        # Display the menu options
        display_menu()
        
        # Get user input for the choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nThe shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
