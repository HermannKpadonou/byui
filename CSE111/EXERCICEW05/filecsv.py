import csv

data = [
    ["Crop", "Product", "Dosage_Ha", "Unit", "Treatments_Per_Cycle"],
    ["Eggplant", "Decis", 1, "L", 200, "25-30"],
    ["Eggplant", "Manebe_80", 3, "kg", 200, "25-30"],
    ["Tomato", "Decis", 1, "L", 200, "10-12"],
    ["Tomato", "Manebe_80", 3, "kg", 200, "10-12"],
    ["Chili Pepper", "Decis", 1, "L", 100, "12-15"],
    ["Chili Pepper", "Manebe_80", 3, "kg", 100, "12-15"],
    ["Bell Pepper", "Decis", 1, "L", 200, "12-15"],
    ["Bell Pepper", "Manebe_80", 3, "kg", 200, "12-15"],
    ["Onion", "Decis", 1, "L", 200, "12-15"],
    ["Onion", "Manebe_80", 3, "kg", 200, "12-15"],
    ["Leek", "Decis", 1, "L", 200, "6-7"],
    ["Leek", "Manebe_80", 3, "kg", 200, "6-7"],
    ["Cabbage", "Decis", 1, "L", 200, "10-12"],
    ["Cabbage", "Manebe_80", 3, "kg", 200, "10-12"],
    ["Radish", "Decis", 1, "L", 200, "1"],
    ["Carrot", "Decis", 1, "L", 200, "5"],
    ["Carrot", "Manebe_80", 3, "kg", 200, "5"],
    ["Lettuce", "Decis", 1, "L", "NA", "4"],
    ["Lettuce", "Manebe_80", 3, "kg", "NA", "4"],
    ["Cucumber", "Decis", 1, "L", 200, "15"],
    ["Cucumber", "Manebe_80", 3, "kg", 200, "15"],
    ["Okra", "Decis", 1, "L", 200, "9"],
    ["Okra", "Manebe_80", 3, "kg", 200, "9"]
]

with open('agri_treatments.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")