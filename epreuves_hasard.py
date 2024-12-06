import random
from traceback import print_tb


def bonneteau():

    l = ("A","B","C")
    tentative = 2
    print("Vous devez deviner sous quel bonneteau (A, B ou C) se cache la clé. Vous disposez de deux essais pour le trouver.")
    print(l)

    while tentative >= 1:
        gagnant =random.choice(l)
        print("Il vous reste :",tentative,"tentative.")
        choix = input("Choisir un bonneteau (A, B ou C) : ").upper()
        if choix in l :
            if choix == gagnant :
                print("Bravo, vous avez trouvé la clef!")
                return True
            else:
                print("Vous n'avez pas trouver la clef.")
        else:
            print("Votre choix n'est pas valide.")
        tentative = tentative - 1
    print("Vous avez perdu, la clef se trouve sous le bonneteau", gagnant,".")
    return False


def jeu_lance_des():

    essais = 3
    t1 = ()
    t2 = ()

    while essais > 0 :
        input("Appuyez sur Entrée pour lancer les dés.")
        t1 = (random.randint(1, 6), random.randint(1, 6))
        print(t1)
        if 6 in t1 :
            print ('Bravo, vous avez remporté la partie et la clef.')
            return True
        t2 = (random.randint(1, 6), random.randint(1, 6))
        print(t2)
        if 6 in t2 :
            print('Le maitre du jeux a remporté la partie.')
            return False
        else :
            print("Personne n'a obtenu 6, on passe au prochain essai")
    print("Aucun joueur n'a obtenu un 6 après trois essais, c'est un match nul")
    return False

print(jeu_lance_des())





