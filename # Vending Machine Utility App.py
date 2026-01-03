# Vending Machine Utility App
# CodeLab I – Assessment 2
# Author: [Your Name]

# Dictionary storing vending machine items
# Each item has a name, price, stock, and category
items = {
    "A1": {"name": "Coca Cola", "price": 1.50, "stock": 5, "category": "Drinks"},
    "A2": {"name": "Water", "price": 1.00, "stock": 5, "category": "Drinks"},
    "B1": {"name": "Chocolate Bar", "price": 1.20, "stock": 5, "category": "Snacks"},
    "B2": {"name": "Crisps", "price": 1.30, "stock": 5, "category": "Snacks"},
    "C1": {"name": "Coffee", "price": 2.00, "stock": 5, "category": "Hot Drinks"}
}

def display_menu():
    """Displays all available items grouped by category"""
    print("\n--- VENDING MACHINE MENU ---")
    categories = set(item["category"] for item in items.values())

    for category in categories:
        print(f"\n{category}:")
        for code, item in items.items():
            if item["category"] == category:
                print(f"{code} - {item['name']} (£{item['price']}) | Stock: {item['stock']}")

def get_money():
    """Captures money input from user"""
    while True:
        try:
            money = float(input("\nInsert money (£): "))
            if money <= 0:
                print("Please insert a valid amount.")
            else:
                return money
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_item():
    """Captures item selection"""
    code = input("\nEnter item code: ").upper()
    return code

def vend_item(code, balance):
    """Processes vending logic"""
    if code not in items:
        print("Invalid code.")
        return balance

    item = items[code]

    if item["stock"] <= 0:
        print("Sorry, this item is out of stock.")
        return balance

    if balance < item["price"]:
        print("Insufficient funds.")
        return balance

    # Dispense item
    item["stock"] -= 1
    balance -= item["price"]

    print(f"\nDispensing {item['name']}...")
    print(f"Remaining balance: £{balance:.2f}")

    # Simple intelligence suggestion
    if item["category"] == "Hot Drinks":
        print("Suggestion: Why not add a Chocolate Bar?")

    return balance

def vending_machine():
    """Main program loop"""
    print("Welcome to the Vending Machine!")
    balance = get_money()

    while True:
        display_menu()
        code = select_item()
        balance = vend_item(code, balance)

        if balance <= 0:
            break

        choice = input("\nWould you like to buy another item? (y/n): ").lower()
        if choice != "y":
            break

    print(f"\nChange returned: £{balance:.2f}")
    print("Thank you for using the Vending Machine!")

# Run the vending machine
vending_machine()
