"""
Authors: Hermann KPADONOU
Purpose: This module reads a CSV file and returns its contents as a compound dictionary.
"""


import csv

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
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


def main():
    
    filename = "products.csv"
    key_column_index = 0
    products = read_dictionary(filename, key_column_index)
    print("All Products")
    print(products)

    print(f"Requested Items")
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            product_id = row[0]
            quantity = float(row[1])
            if product_id in products:
                product_data = products[product_id]
                product_name = product_data[1]
                price = float(product_data[2])
                total_price = price * quantity
                print(f"{product_name}: {quantity} @ {total_price:.2f}")
            else:
                print(f"Product '{product_name}' not found in the product list.")
                      
if __name__ == "__main__":
    main()