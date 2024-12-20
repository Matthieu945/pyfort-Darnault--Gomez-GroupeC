import json
fichier = "data/enigmesPF.json"

def charger_enigmes(fichier):
    with open(fichier, 'r') as f:
        enigmes = json.load(f)
    return enigmes

import random

def enigme_pere_fouras(enigmes) :
    liste_enigme = []
    for enigme in enigmes :
        if "question" in enigme :
            liste_enigme.append(enigme["question"])
    enigme_aleatoire = random.choice(liste_enigme)
    print(enigme_aleatoire)
    print("Vous avez le droit à trois essais.")
    essai = 3
    resultat_joueur = input("Votre réponse :")
    while essai > 0 :
        if resultat_joueur.lower() == enigme_aleatoire["reponse"].lower() :
            print("Bonne réponse")
            return True
        else :
            print("Mauvaise réponse")
            essai -=1
    return False

enigmes = charger_enigmes(fichier)
enigme_pere_fouras(enigmes)






