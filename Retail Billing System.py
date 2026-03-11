# Bill heading
def bill_header():
    print("\n" + "=" * 70)
    print(" {:<25} {:<17} {:<17} {:<17}".format("Item Name", "Quantity", "Price/Unit", "Total"))
    print("-" * 70)  # horizontal dash line

# Ask for item details
def get_item_details():
    item_name = input("\nEnter item name (up to 25 characters including spaces) or type 'DONE' to end the shopping: ").strip()
    if item_name.upper() == 'DONE':
        return None, None, None
    if len(item_name) > 25:
        print("Item name must be 25 characters or less (including spaces). Please try again.")
        return get_item_details()
    
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity should be a positive value. Please try again.")
            return get_item_details()
    except ValueError:
        print("Quantity should be a valid number. Please try again.")
        return get_item_details()
    
    try:
        price = float(input("Enter price per unit: RM"))
        if price <= 0:
            print("Price should be a positive value. Please try again.")
            return get_item_details()
    except ValueError:
        print("Price should be a valid number. Please try again.")
        return get_item_details()
    
    return item_name, quantity, price

# Final Amount
def final_amount(total_due):
    print("-" * 70)
    print(f"{'Total Due: RM':}{total_due:.2f}")
    print("=" * 70)

# Bill friendly welcome
def main():
    print("Welcome to Grocery Billing System! A one-stop shop for every possible grocery desire. Strive to start your buying experience.")

    # Empty shopping cart
    shopping_cart = []
    total_due = 0

    while True:
        item_name, quantity, price = get_item_details()
        if item_name is None:  # Check if done
            break
        total = quantity * price
        shopping_cart.append((item_name, quantity, price, total))
        total_due += total

    # Print the bill if there are items in the cart
    if shopping_cart:
        bill_header()
        for item_name, quantity, price, total in shopping_cart:
            print(f"{item_name:<25}{quantity:^12}{price:^26.2f}{total:^6.2f}")
        final_amount(total_due)
    else:
        print("\nNo items were placed in the cart.")

    print("\nThank you for shopping with us!")
    print("\nWe hope you found joy along the way.")
    print("\nHave a lovely day, bright and true, as we’re grateful for you, our valued crew!")

if __name__ == "__main__":
    main()
