# python-retail-billing-system

Introduction

This project is a Python-based Retail Billing System designed to help users calculate the total cost of grocery purchases. The program allows customers to enter item names, quantities, and unit prices, then automatically calculates the total amount and generates a structured receipt.

Features

- Enter multiple grocery items
- Automatic calculation of total price
- Organized receipt output
- Error handling for invalid inputs
- Simple and user-friendly console interface

Problem Statement

Retail stores require a quick and reliable way to calculate bills for multiple items. This system allows users to input product details and automatically generates an organized bill with accurate calculations.

Requirements

- Python 3.x
- Basic command line interface

How It Works

1. The program displays a welcome message.
2. Users enter item name, quantity, and unit price.
3. The system calculates the total price for each item.
4. Users can continue adding items until they type DONE.
5. The system prints a formatted receipt with the final amount.

Code Structure

- bill_header() – Displays the bill header.
- get_item_name() – Collects and validates item input.
- final_amount() – Displays the final total amount.
- main() – Controls the program workflow.

Example Output

Item Name     Quantity     Price/Unit     Total
------------------------------------------------
Apple            2            3.00         6.00
Milk             1            5.50         5.50
------------------------------------------------
Total Due:                                 11.50

Future Improvements

- Add tax calculation
- Add discount support
- Save bills to files
- Connect to a product database

References

- Python Documentation
- W3Schools Python Guide
- Real Python Tutorials
