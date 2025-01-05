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
def affiche_grille(grille, message):
    print(message)
    for i in range (len(grille)):
        for j in range (len(grille[i])):
            print("|", end=" ")
            print(grille[i][j],end=" ")
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

def init():
    grille = grille_vide()
    bateau = 0

    print("Veuillez placer vos deux bateaux sur la grille de jeux.")

    while bateau < 2:
        ligne, colonne = demande_position()

        if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = "B"
                bateau = bateau + 1
                print("Votre bateau à bien été placé.")
        else:
                print("La place est déjà prise.")

    affiche_grille(grille,"Voici la grille de jeux avec vos deux bateaux.")

def tour(joueur, grille_tirs_joueur, grille_adversaire) :
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
        tir1, tir2 = random.randint(0,2), random.randint(0,2)
        print('Le maître du jeu tire en position', tir1, ',', tir2)
        if grille_adversaire[tir1][tir2] == 'B':
            grille_tirs_joueur[tir1][tir2] = 'x'
            print("Bateau coulé !")
        elif grille_adversaire[tir1][tir2] == ' ':
            grille_tirs_joueur[tir1][tir2] = '.'
            print("Raté...")

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

def jeu_bataille_navale():
    print("Chaque joueur possède 2 bateaux de 1x1 qu'il doit placer sur une grille de 3x3.")
    init()
    grille_jouer, grille_maitre = grille_vide(), grille_vide()

    while True:
        bateau1 = (random.randint(1, 3), random.randint(1, 3))
        bateau2 = (random.randint(1, 3), random.randint(1, 3))
        if bateau1 != bateau2:
            break
    grille_maitre[bateau1[0]][bateau1[1]] = 'B'
    grille_maitre[bateau2[0]][bateau2[1]] = 'B'

    grille_tirs_jouer, grille_tirs_maitre = grille_vide(), grille_vide()

    joueur = 0
    while True:
        if joueur == 0:
            tour(joueur,grille_tirs_jouer, grille_maitre)
        elif joueur == 1:
            tour(joueur,grille_tirs_maitre, grille_jouer)
        if gagne(grille_tirs_jouer) == True:
            print("Le joueur a gagné !")
            return True

        joueur = suiv(joueur)




