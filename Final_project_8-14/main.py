import time
import os

from package.eng_deu_menu import eng_deu_menu
from package.bel_pol_menu import bel_pol_menu

while True:

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("=" * 41)
    print()
    print("Welcome!")
    print()
    print("=" * 41)
    print()
    print("1. English and German")
    print("2. Belarusian and Polish")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        eng_deu_menu()

    elif choice == "2":
        bel_pol_menu()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        input("Press Enter...")
