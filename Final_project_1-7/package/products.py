import json

from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "fridge.json")

def load_products():

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_products(products):

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


def add_product(name, weight, expiry):

    products = load_products()

    product = {
        "name": name,
        "weight": weight,
        "expiry": expiry
    }

    products.append(product)

    save_products(products)

    print("\nProduct added successfully.")


def delete_product(name):

    products = load_products()

    updated_products = []

    found = False

    for product in products:

        if product["name"].lower() != name.lower():

            updated_products.append(product)

        else:

            found = True

    save_products(updated_products)

    if found:
        print("\nProduct deleted successfully.")
    else:
        print("\nProduct not found.")


def edit_product(old_name, new_name, new_weight, new_expiry):

    products = load_products()

    found = False

    for product in products:

        if product["name"].lower() == old_name.lower():

            product["name"] = new_name
            product["weight"] = new_weight
            product["expiry"] = new_expiry

            found = True

            break

    save_products(products)

    if found:
        print("\nProduct updated successfully.")
    else:
        print("\nProduct not found.")


def expired_products():

    products = load_products()

    today = datetime.today().date()

    expired = []

    for product in products:

        expiry_date = datetime.strptime(
            product["expiry"],
            "%Y-%m-%d"
        ).date()

        if expiry_date < today:

            expired.append(product)

    if len(expired) == 0:

        print("\nNo expired products.")

        return

    print("\nExpired products:\n")

    for index, product in enumerate(expired, start=1):

        print(f"{index}. {product['name']}")
        print(f"   Weight: {product['weight']} g")
        print(f"   Expiry: {product['expiry']}")
        print()


def fresh_products():

    from datetime import datetime

    products = load_products()

    today = datetime.today().date()

    fresh = []

    for product in products:

        expiry_date = datetime.strptime(
            product["expiry"],
            "%Y-%m-%d"
        ).date()

        if expiry_date >= today:

            fresh.append(product)

    if len(fresh) == 0:

        print("\nNo fresh products.")

        return

    print("\nFresh products:\n")

    for index, product in enumerate(fresh, start=1):

        print(f"{index}. {product['name']}")
        print(f"   Weight: {product['weight']} g")
        print(f"   Expiry: {product['expiry']}")
        print()



def show_products():

    products = load_products()

    if len(products) == 0:

        print("\nNo products found.")

        return

    print("\nAll products:\n")

    for index, product in enumerate(products, start=1):

        print(f"{index}. {product['name']}")
        print(f"   Weight: {product['weight']} g")
        print(f"   Expiry: {product['expiry']}")
        print()