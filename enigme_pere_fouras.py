import json
fichier = "data/enigmesPF.json"

def charger_enigmes(fichier):
    with open(fichier, 'r') as f:
        enigmes = json.load(f)
    return enigmes

import random

def enigme_pere_fouras(enigmes) :
    liste_enigme = []
    liste_reponse = []
    for enigme in enigmes :
        if "question" in enigme :
            liste_enigme.append(enigme["question"])
            liste_reponse.append(enigme["reponse"])
    numero_aleatoire = random.randint(0, len(liste_enigme))
    enigme_aleatoire = liste_enigme[numero_aleatoire]
    reponse_attendue = liste_reponse[numero_aleatoire]
    print(enigme_aleatoire)
    essai = 3
    print("Vous avez le droit à trois essais.")
    while essai > 0 :
        resultat_joueur = input("Votre réponse : ")
        if resultat_joueur.lower() == reponse_attendue.lower() :
            print("Bonne réponse ! Vous gagnez une clé.")
            return True
        else :
            print("Mauvaise réponse. Il vous reste encore", essai - 1, "essai(s).")
            essai -= 1
    if essai == 0 :
        print(f"Vous avez perdu. La solution était {reponse_attendue.lower()}. Vous ne gagnez pas de clé.")
    return False

enigmes = charger_enigmes(fichier)
enigme_pere_fouras(enigmes)






