import json
fichier = "data/indicesSalle.json"
import random

def salle_De_Tresor(fichier) :
    jeu_tv = {}
    liste_annees = []
    with open(fichier, "r") as f :
        jeu_tv = json.load(f)
    for annees in jeu_tv["Fort Boyard"].keys() :
        liste_annees.append(annees)
    annee = random.choice(liste_annees)
    jeu_tv = jeu_tv["Fort Boyard"][annee]
    liste_emssions = []
    for emissions in jeu_tv.keys() :
        liste_emssions.append(emissions)
    emission = jeu_tv[random.choice(liste_emssions)]
    liste_indices = []
    for indices in emission["Indices"] :
        liste_indices.append(indices)
        mot_code = emission["MOT-CODE"]
    print("Les quatre premiers indices sont : '{}', '{}', '{}' et '{}'.".format(liste_indices[0].lower(),liste_indices[1].lower(),liste_indices[2].lower(),liste_indices[3].lower()))
    print("Vous avez le droit à trois tentatives pour essayer de trouver le mot-clé.")
    essai = 3
    i = 4
    while essai > 0 :
        print("Vous avez encore", essai, "tentatives.")
        reponse_joueur = input("Votre réponse : ")
        essai -= 1
        if reponse_joueur.lower() == mot_code.lower() :
            print("Félicitations ! Vous avez remporté la parti.")
            return True
        else :
            if essai > 0 :
                print("Raté ! Mais vous avez le droit à un indice supplémentaire.")
                print("Indice supplémentaire : '{}'.".format(liste_indices[i].lower()))
                i += 1
            if essai == 0 :
                print("C'est définitivement perdu ! Le mot-clé était '{}'.".format(mot_code.lower()))
    return False










salle_De_Tresor(fichier)


