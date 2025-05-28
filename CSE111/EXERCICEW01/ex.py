city_name = "Accra"
elevation = 61
population = 4200000
# Ouvrez un fichier texte nommé cities.txt en mode ajout.
with open("cities.txt", "at") as file:
  # Imprimez le nom et les informations d’une ville dans le fichier.
  print(city_name, file=file)
  print(f"{elevation}, {population}", file=file)