def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_append = input("Enter the item to add: ")
            shopping_list.append(item_append)
        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input("Enter the item name to remove: ")
            if item_remove in shopping_list:
                shopping_list.remove(item_remove)
            else:
                print("item doesn't exist in the shopping list")
        elif choice == '3':
            # Display the shopping list
            print("The shopping list is: ", shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()