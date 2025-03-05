# Importer les modules nécessaires
import sys
import time

# Créer la fonction principale
def main():
# Afficher le message de bienvenue et l'histoire initiale
print("Bienvenue dans le jeu d'aventure!")
print("En tant que voyageur passionné, vous avez décidé de visiter les catacombes de Paris.")
print("Cependant, lors de votre exploration, vous vous retrouvez perdu.")
print("Vous pouvez choisir de marcher dans plusieurs directions pour trouver une sortie.")
print("Commençons par votre nom:")
# Demander au joueur d'entrer son nom
name = input()
# Afficher un message personnalisé avec le nom du joueur
print("Bonne chance, " + name + ".")
# Appeler la fonction introScene avec le nom du joueur comme argument
introScene = (name)

# Créer la fonction introScene qui correspond à la première scène du jeu
def introScene(name):
# Afficher une description de la scène et des choix possibles
print("Vous êtes dans une pièce sombre et humide. Vous voyez trois passages devant vous: un à gauche, un au centre et un à droite.")
print("Que voulez-vous faire?")
print("A) Aller à gauche")
print("B) Aller au centre")
print("C) Aller à droite")
# Demander au joueur d'entrer son choix
choice = input()
# Gérer les choix du joueur avec des instructions if, elif et else
if choice == "A":
# Si le joueur choisit A, appeler la fonction leftScene avec le nom du joueur comme argument
leftScene = (name)
elif choice == "B":
# Si le joueur choisit B, appeler la fonction centerScene avec le nom du joueur comme argument
centerScene = (name)
elif choice == "C":
# Si le joueur choisit C, appeler la fonction rightScene avec le nom du joueur comme argument
rightScene(name)
else:
# Si le joueur entre un choix invalide, afficher un message d'erreur et quitter le jeu
print("Choix invalide. Le jeu est terminé.")
sys.exit()
