from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuve_finale import *
from epreuves_hasard import *
from epreuves_mathematiques import *
from fonctions_utiles import *


def jeu():
    introduction()
    equipe = composer_equipe()    #présentation et création des équipes
    clef = 0                    # initialisation du nombre de clés à 0

    while clef < 3:             # On répète tant que l'équipe n'a pas trois clés
        epreuve_choisi = menu_epreuve()
        joueur_choisi = choisir_joueur(equipe)

        if epreuve_choisi == 1:
            epreuve_choisi = epreuve_math()
        if epreuve_choisi == 2:
            epreuve_choisi = jeu_bataille_navale()
        if epreuve_choisi == 3:
            epreuve_choisi = epreuve_hasard()
        if epreuve_choisi == 4:
            epreuve_choisi = enigme_pere_fouras()

        elif epreuve_choisi == True:
            joueur_choisi['clef_gagnees'] += 1
            clef += 1

    print("C'est maintenant le moment de la salle des trésors !")
    final = salle_De_Tresor()  # une fois les 3 clés obtenues -> salle tresor
    if final == True:
        "Vous avez gagné !!!"
    else:
        "Vous avez perdu..."



jeu()






