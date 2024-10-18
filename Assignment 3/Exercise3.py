items = {
    "123": {"name": "Bread", "price": 1.5},
    "456": {"name": "Milk", "price": 2.0},
    "789": {"name": "Eggs", "price": 3.0}
}

def startNewReceipt():
    receipt = []
    total_amount = 0
    while True:
        barcode = input("Enter the item barcode: ")
        if barcode not in items:
            print("Item not found.")
            continue
        quantity = int(input("Enter the quantity of " + items[barcode]['name'] + ": "))
        item_name = items[barcode]['name']
        item_price = items[barcode]['price']
        total_item_cost = quantity * item_price
        receipt.append({"name": item_name, "quantity": quantity, "total_cost": total_item_cost})
        total_amount += total_item_cost
        add_more = input("Would you like to add another item? (yes/no): ").lower()
        if add_more != "yes":
            break
    printReceipt(receipt, total_amount)

def printReceipt(receipt, total_amount):
    print("\nReceipt:")
    print("-" * 30)
    for item in receipt:
        print(item['name'] + " x " + str(item['quantity']) + " = $" + str(round(item['total_cost'], 2)))
    print("-" * 30)
    print("Total: $" + str(round(total_amount, 2)))
    print("-" * 30)

def posSystem():
    while True:
        new_receipt = input("Would you like to start a new receipt? (yes/no): ").lower()
        if new_receipt == "yes":
            startNewReceipt()
        else:
            print("Exiting the system.")
            break
        
posSystem()
