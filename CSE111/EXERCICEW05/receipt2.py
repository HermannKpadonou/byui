"""
Authors: Hermann KPADONOU
Purpose: This program reads a CSV file containing product information and another CSV file containing requested items.
It calculates the total price, including sales tax, and prints a receipt with the details of the requested items.
"""

from datetime import datetime
import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary."""
    products_dict = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  
            for row in reader:
                key = row[key_column_index]
                products_dict[key] = row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")  
    return products_dict

def request_items(products):
    try:
        print("Requested Items")
        total_products_count = 0
        subtotal_price = 0.0
        
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            
            for row in reader:
                try:
                    product_id = row[0]
                    quantity = int(row[1])
                    product_data = products[product_id]  
                    product_name = product_data[1]
                    price = float(product_data[2])
                    total_products_count += quantity
                    subtotal_price += quantity * price
                    print(f"{product_name}: {quantity} @ {price:.2f}")
                except KeyError:
                    print(f"Error: unknown product ID in the request.csv file\n'{product_id}'")
            tax = subtotal_price * 0.06
            total_price = subtotal_price + tax
            print(f"Number of Items: {total_products_count}")
            print(f"Subtotal: {subtotal_price:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: {total_price:.2f}")
    except FileNotFoundError as e:
        print("Error: missing file\n[Errno 2] No such file or directory: 'request.csv'")
        
def date_to_receipt(datetime):

    """Convert a datetime object to a formatted receipt date string."""

    current_date_and_time = datetime.now()
    return current_date_and_time.strftime("%a %b %d %H:%M:%S %Y")     

def main():
    
    try:
        print("Aboisso Market")
        products = read_dictionary("products.csv", 0)
        request_items(products)
        print("Thank you for shopping at the Aboisso Market.")
        print(f"{date_to_receipt(datetime)}")
    except (FileNotFoundError, KeyError):
        pass  # Errors already handled in the functions


if __name__ == "__main__":
    main()