"""
Agricultural Plan Module
Author : Hermann KPADONOU
Purpose : Phytosanitary treatment management system
"""


import csv
from datetime import datetime

# --- FONCTIONS DE LOGIQUE ET DE CALCUL ---

def read_products_from_csv(filename="agri_treatments.csv"):
    """
    Lit le fichier des produits et le retourne sous forme de liste de dictionnaires.
    """
    products = []
    try:
        with open(filename, mode='rt') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # On essaie de convertir les valeurs numériques
                try:
                    row['Dose_Ha'] = float(row['Dose_Ha'])
                    row['Water_Volume_L_Ha'] = float(row['Water_Volume_L_Ha']) if row['Water_Volume_L_Ha'] != 'NA' else 0
                    products.append(row)
                except (ValueError, KeyError) as e:
                    print(f"Avertissement : Ligne ignorée dans {filename} à cause d'une erreur de format : {row} ({e})")
    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{filename}' est introuvable. Assurez-vous qu'il est dans le même dossier que le programme.")
    return products

def calculate_area(length, width):
    """
    Calcule la surface d'un champ en hectares (1 hectare = 10 000 m²).
    """
    if length <= 0 or width <= 0:
        return 0
    return (length * width) / 10000

def calculate_product_dose(area, dose_per_hectare):
    """
    Calcule la quantité de produit nécessaire pour une seule application.
    """
    return area * dose_per_hectare

def calculate_water_volume(area, water_per_hectare):
    """
    Calcule le volume d'eau nécessaire pour la bouillie.
    """
    return area * water_per_hectare

def write_treatment_to_csv(filename, treatment_data):
    """
    Ajoute une ligne dans le fichier d'historique des traitements.
    """
    try:
        # 'a' pour "append" (ajouter à la fin)
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            # Définir les noms des colonnes
            fieldnames = ["date", "crop", "product", "area_ha", "dose_used", "unit"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Si le fichier est vide, on écrit l'en-tête
            if file.tell() == 0:
                writer.writeheader()
            
            writer.writerow(treatment_data)
        print(f"Traitement enregistré avec succès dans '{filename}'.")
    except IOError as e:
        print(f"ERREUR : Impossible d'écrire dans le fichier '{filename}'. ({e})")

# --- FONCTIONS D'INTERACTION UTILISATEUR ---

def get_user_input(available_products):
    """
    Demande à l'utilisateur de choisir un produit et de donner les dimensions du champ.
    """
    print("Veuillez choisir un traitement dans la liste :")
    for i, product in enumerate(available_products):
        print(f"  {i+1}. Culture: {product['Crop']}, Produit: {product['Product']}")
    
    # Obtenir le choix du produit
    choice_index = -1
    while choice_index < 0 or choice_index >= len(available_products):
        try:
            choice = int(input(f"Votre choix (1-{len(available_products)}) : "))
            choice_index = choice - 1
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    chosen_product = available_products[choice_index]
    
    # Obtenir les dimensions du champ
    length = float(input("Entrez la longueur du champ (en mètres) : "))
    width = float(input("Entrez la largeur du champ (en mètres) : "))

    return chosen_product, length, width

def display_result(area, product_name, dose, unit, water_volume):
    """
    Affiche le résultat final du calcul à l'utilisateur.
    """
    print("\n--- RÉSULTAT DU CALCUL ---")
    print(f"Surface à traiter : {area:.4f} hectares")
    print("-" * 28)
    print("Pour votre traitement, vous aurez besoin de :")
    print(f"  - Produit : {dose:.3f} {unit} de {product_name}")
    if water_volume > 0:
        print(f"  - Eau : {water_volume:.2f} Litres")
    print("--------------------------\n")

# --- FONCTION PRINCIPALE ---

def main():
    """
    Le point d'entrée et le chef d'orchestre du programme.
    """
    print("--- AgriPlan : Calculateur de Dose Phytosanitaire ---")
    
    # 1. Charger la liste des produits depuis le fichier CSV
    products = read_products_from_csv("agri_treatments.csv")
    if not products:
        return  # Arrêter le programme si aucun produit n'est chargé

    # 2. Demander à l'utilisateur ses choix
    chosen_product, length, width = get_user_input(products)

    # 3. Effectuer les calculs
    area_ha = calculate_area(length, width)
    if area_ha > 0:
        dose = calculate_product_dose(area_ha, chosen_product['Dose_Ha'])
        water = calculate_water_volume(area_ha, chosen_product['Water_Volume_L_Ha'])
        
        # 4. Afficher le résultat
        display_result(area_ha, chosen_product['Product'], dose, chosen_product['Unit'], water)
        
        # 5. Préparer les données pour l'historique
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "crop": chosen_product['Crop'],
            "product": chosen_product['Product'],
            "area_ha": f"{area_ha:.4f}",
            "dose_used": f"{dose:.3f}",
            "unit": chosen_product['Unit']
        }
        
        # 6. Écrire dans le fichier d'historique
        write_treatment_to_csv("historique.csv", record)
    else:
        print("Calcul annulé car la surface est nulle ou les dimensions sont invalides.")

# --- Point d'entrée du script ---
if __name__ == "__main__":
    main()