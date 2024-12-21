#Épreuve factorielle

def factorielle(n) :
    for i in range (1, n) :
        n *= i
    return n

import random

def epreuve_math_factorielle() :
    n = random.randint(1,10)
    print("Calculer la factorielle de", n, ".")
    a = int(input("Votre réponse :"))
    if a == factorielle(n) :
        print("Bravo ! Vous gagnez une clé.")
        return True
    else :
        print("Raté ! Vous ne gagnez pas de clé.")
        return False

#Épreuve des nombres premiers

def est_premier(n) :
    if n <= 1 :
        return False
    for i in range (2, int((n**0.5)) + 1) :
        if n% i == 0 :
            return False
    return True


def premier_plus_proche(n) :
    while not est_premier(n) :
        n += 1
    return n

def epreuve_math_premier() :
    a = random.randint(10,20)
    print("Quel est le nombre premier le plus proche de ", a, "?")
    b = int(input("Votre réponse :"))
    if b == premier_plus_proche(a):
        print("Bravo ! Vous gagnez une clé.")
        return True
    else :
        print("Raté ! Vous ne gagnez pas de clé.")
        return False


# Épreuve de la roulette

def epreuve_roulette_mathematique() :
    nombres = [random.randint(1, 20) for _ in range(5)]
    print("Nombres sur la roulette :", nombres)
    operation = ['addition', 'soustraction', 'multiplication']
    operation_aleatoire = random.choice(operation)
    print(f"Calculez le résultat en combinant ces nombres avec une {operation_aleatoire}.")
    if operation_aleatoire == 'addition' :
        reponse = 0
        for i in range(len(nombres)) :
            reponse += nombres[i]
    if operation_aleatoire == "soustraction" :
        reponse = 0
        for i in range(len(nombres)) :
            reponse -= nombres[i]
    if operation_aleatoire == "multiplication":
        reponse = 1
        for i in range(len(nombres)) :
            reponse *= nombres[i]
    reponse_joueur = int(input("Votre réponse :"))
    if reponse_joueur == reponse :
        print("Bravo ! Vous gagnez une clé.")
        return True
    else:
        print("Raté ! Vous ne gagnez pas de clé.")
        return False

#Épreuve maths

def epreuve_math() :
    epreuves = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return epreuve()








