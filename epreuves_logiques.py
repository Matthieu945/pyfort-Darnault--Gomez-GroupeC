import random

def suiv(joueur):
    if joueur == 0:
        joueur = 1
    else :
        joueur = 0
    return joueur

#création du plateau de jeux
def grille_vide():
   return [[" " for i in range(3)] for j in range(3)]

grille = grille_vide()

#affichage du tableau de jeux
def affiche_grille(grille_joueur, message):
    print(message)
    for i in range (len(grille_joueur)):
        for j in range (len(grille_joueur[i])):
            print("|", end=" ")
            print(grille_joueur[i][j],end=" ")
        print("|")
    print("-"*13)

#position sur la grille
def demande_position():
    while True:
        position = input("Choisissez une position en l'entrant sous la forme (ligne,colonne), entre 1 et 3: ")
        if "," in position:
            ligne, colonne = position.split(',')  # méthode split pour séparer le tuple position là où il y a une virgule
            ligne, colonne = int(ligne), int(colonne)
            if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                return ligne - 1, colonne - 1
        print("Position invalide !")

#Placement bateaux
def init(grille_joueur):
    bateau = 0

    print("Veuillez placer vos deux bateaux sur la grille de jeux.")

    while bateau < 2:
        ligne, colonne = demande_position()

        if grille_joueur[ligne][colonne] == " ":
                grille_joueur[ligne][colonne] = "B"
                bateau = bateau + 1
                print("Votre bateau à bien été placé.")
        else:
                print("La place est déjà prise.")

    affiche_grille(grille_joueur,"Voici la grille de jeux avec vos deux bateaux.")


#changelenet des tours
def tour(joueur, grille_tirs_joueur, grille_adversaire, tirs_maitre) :
    if joueur == 0:
        print("C'est votre tour.")
        affiche_grille(grille_tirs_joueur, "Voici l'historique des tirs.")
        tir1, tir2 = demande_position()
        if grille_adversaire[tir1][tir2] == 'B':
            grille_tirs_joueur[tir1][tir2] = 'x'
            print("Bateau coulé !")
        elif grille_adversaire[tir1][tir2] == ' ':
            grille_tirs_joueur[tir1][tir2] = '.'
            print("Raté...")


    if joueur == 1:
        print("C'est le tour du maître du jeu :")
        while True:  # Boucle pour que chaque tir soit différents
            tir1, tir2 = random.randint(0, 2), random.randint(0, 2)
            if (tir1, tir2) not in tirs_maitre:
                tirs_maitre.add((tir1, tir2))
                break
        print('Le maître du jeu tire en ', tir1+1, ',', tir2+1)
        print('touche: ', grille_adversaire[tir1][tir2])
        if grille_adversaire[tir1][tir2] == 'B':
            grille_tirs_joueur[tir1][tir2] = 'x'
            print("Bateau coulé !")
        elif grille_adversaire[tir1][tir2] == ' ':
            grille_tirs_joueur[tir1][tir2] = '.'
            print("Raté...")

#Choix gagnant
def gagne(grille_tirs_joueur):
    bateaucoule = 0

    for ligne in grille_tirs_joueur:
        for case in ligne:
            if case == 'x':
                bateaucoule += 1
    if bateaucoule == 2:
        return True
    if bateaucoule < 2:
        return False

#jeux final
def jeu_bataille_navale():
    print("Chaque joueur possède 2 bateaux de 1x1 qu'il doit placer sur une grille de 3x3.")
    grille_jouer, grille_maitre = grille_vide(), grille_vide()
    init(grille_jouer)
    tirs_maitre = set()
    while True:
        bateau1 = (random.randint(0, 2), random.randint(0, 2))
        bateau2 = (random.randint(0, 2), random.randint(0, 2))
        if bateau1 != bateau2:
            break
    grille_maitre[bateau1[0]][bateau1[1]] = 'B'
    grille_maitre[bateau2[0]][bateau2[1]] = 'B'

    grille_tirs_jouer, grille_tirs_maitre = grille_vide(), grille_vide()

    joueur = 0
    while True:
        if joueur == 0:
            tour(joueur,grille_tirs_jouer, grille_maitre, tirs_maitre)
            if gagne(grille_tirs_jouer) == True:
                print("Le joueur a gagné !")
                return True
        elif joueur == 1:
            tour(joueur,grille_tirs_maitre, grille_jouer, tirs_maitre)
            if gagne(grille_tirs_maitre) == True:
                print("Le maitre du jeu a gagné !")
                return False

        joueur = suiv(joueur)







