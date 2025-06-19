"""
Agricultural Plan Module
Author : Hermann KPADONOU
Purpose : Phytosanitary treatment management system

"""

import csv
from datetime import datetime

 
CROP_INDEX = 0
PRODUCT1_NAME_INDEX = 1
PRODUCT1_QTY_INDEX = 2
PRODUCT2_NAME_INDEX = 3
PRODUCT2_QTY_INDEX = 4
CYCLE = 5

def read_products_from_csv(filename="agri_treatments.csv"):
 
# Read the csv file and return compound list


 





                
                

   


 """
 def calculate_area(length, width):
    #Calculate the area en square meters and return in are(1Ha =10000m²)
    L =length
    w = width
    try:
       area = (L*w)/10000
    except ZeroDivisionError:
        print("Error: Length or Width must be different to Zero! Try another data")

    return area

def calculate_product_dose(area, dose_Ha):
    try:
       dose_treatment = area*dose_Ha
    except ZeroDivisionError:
       print("Error: area must be different to Zero!")
    return dose_treatment

    
def write_treatment_to_csv(filename, treatment_data):

def get_user_input(available_products):

#Ask to user to enter the dimensions of space



def display_result(area, product_name, dose, unit, water_volume):


def main():


if __name__ == "__main__":
    main()

   """