print("=== Warehouse Inventory Tracker ===")

inventory = {
    "Keyboard": 15,
    "Mouse": 30,
    "Monitor": 10
}

while True:
    print("\n===== MENU =====")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Quantity")
    print("4. Remove Product")
    print("5. Search Product")
    print("6. Save Inventory")
    print("7. Exit")

    choice = input("Choose an option: ")

if choice == "1" :
    print("\nCurrent Inventory")

    for product, quantity in investory. items():
        print(product, "-", quantity)

elif choice == "2":
    product = input("Enter product name: ")

    try:
        quantity = int(input("Enter quantity: "))
        inventory[product] = quantity
        print("Product added successfully.") 


    except ValueError:
        print("Please enter a valid number.")


elif choice == "3":
    product = input("Enter product name:")

    if product in inventory:
        try:
            quantity = int(input("Enter new quantity:"))
            investory[product] = quantity
            print("Quantity updated")

        except ValueError:
            print("Please enter a number.")


        else:
            print("Product not found.")


elif choice == "4":
    product = input("Enter product to remove:")

    if product in inventory:
        del inventory[product]
        print("Product removed.")


elif choice == "5":
    product = input("Search product:")

    if product in inventory:
        print(product, "-", inventory[product])

    else:
        print("Product not found.")


elif choice == "6":
    with open("inventory.txt", "w") as file:

        for product, quantity in inventory.items():
            file.write(f"{product},{quantity}\n")

        print("Inventory saved.")


elif choice =="7":
    print("Goodbye!")
    breakpoint

else:
    print("Invaild option.")


