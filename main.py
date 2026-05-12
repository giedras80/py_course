import time
import os

from package.products import add_product, show_products, delete_product, edit_product, expired_products, fresh_products

os.system("cls")

while True:


    if os.name == "nt":
        "cls" 
    
    else: 
        "clear"

    text = "Welcome to Smart Fridge System"

    for char in text:
    
        print(char, end="", flush=True)
        time.sleep(0.03)

    print("\n")

    
    print("1. Add product.")
    print("2. Delete product.")
    print("3. Edit product.")
    print("4. Show expired products.")
    print("5. Show fresh products.")
    print("6. Show all products.")
    print("7. Exit.")

    choice = input("\nChoose an option: ")

    
    if choice == "1":

        name = input("\nEnter product name: ")

        weight = input("Enter product weight in grams: ")

        expiry = input("Enter expiry date (yyyy-mm-dd): ")

        add_product(name, weight, expiry)

        input("\nPress Enter to continue...")


    
    elif choice == "2":

        name = input("\nEnter product name to delete: ")

        delete_product(name)

        input("\nPress Enter to continue...")


    elif choice == "3":

        old_name = input("\nEnter product name to edit: ")

        new_name = input("Enter new product name: ")

        new_weight = input("Enter new weight: ")

        new_expiry = input("Enter new expiry date (yyyy-mm-dd): ")

        edit_product(old_name, new_name, new_weight, new_expiry)

        input("\nPress Enter to continue...")

    
    elif choice == "4":

        expired_products()

        input("\nPress Enter to continue...")


    elif choice == "5":

        fresh_products()

        input("\nPress Enter to continue...")


    elif choice == "6":

        show_products()

        input("\nPress Enter to continue...")


    elif choice == "7":

        print("\nGoodbye.")

        break


    else:

        print("\nOption not available yet.")

        input("\nPress Enter to continue...")
