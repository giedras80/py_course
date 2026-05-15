import os
import csv
from difflib import SequenceMatcher


def similarity(a, b):
    return round(
        SequenceMatcher(None, a.lower(), b.lower()).ratio() * 100
    )


def load_words():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "bel_pol_words.csv"
    )

    words = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            words.append(row)

    return words


def show_word_pairs():

    words = load_words()

    print()

    for item in words:

        belarusian = item["belarusian"]
        polish = item["polish"]
        meaning = item["meaning"]
        

        score = similarity(belarusian, polish)

        print(
            f"{belarusian:<10} - {polish:<10} {meaning} | similarity: {score}%"
        )

def bel_pol_menu():

    while True:

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print("=" * 41)
        print()
        print("Belarusian and Polish")
        print()
        print("=" * 41)
        print()

        print("1. Show word pairs")
        print("2. Back")

        choice = input("\nChoose an option: ")

        if choice == "1":

            if os.name == "nt": 
                os.system("cls")
            else: 
                os.system("clear")

            show_word_pairs()

            input("\nPress Enter to continue...")

        elif choice == "2":
            break

        else:
            print("\nInvalid option.")
            input("\nPress Enter to continue...")


       

