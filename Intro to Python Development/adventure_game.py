answer_yes = ["Oui", "O", "oui", "o"]
answer_no = ["Non", "N", "non", "n"]
print(""" BIENVENUE ! COMMENÇONS L'AVENTURE
Vous êtes devant votre maison et vous voyez un homme courir vers vous et vous demander un abri urgent.
Allez-vous lui fournir un abri ? (Oui / Non) """)
ans1 = input(">>")
if ans1.lower() in answer_yes:
    print("\nAprès 2 minutes, la police arrive chez vous et vous demande si le voleur est chez vous ou non.")
    print("Allez-vous dire (Oui / Non)\n")
elif ans1.lower() in answer_no:
    print("\nIl vous attaque. Allez-vous le frapper ou non ? (Oui / Non)\n")
ans2 = input(">>")
if ans2.lower() in answer_yes:
    print("\nVous êtes une personne honnête. C'était un voleur et vous avez gagné le jeu")
elif ans2.lower() in answer_no:
    print("\nVous avez aidé un voleur. Vous allez en prison et vous avez perdu le jeu")
else:
    print("\nRéponse invalide. Veuillez choisir entre Oui ou Non")
ans3 = input(">>")
if ans3.lower() in answer_yes:
  print("\nVous l'avez assommé. Vous avez gagné le jeu")
elif ans3.lower() in answer_no:
  print("\nIl vous tue. Vous avez perdu le jeu")
else:
  print("\nRéponse invalide. Veuillez choisir entre Oui ou Non")
