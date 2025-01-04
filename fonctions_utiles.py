
def introduction():
    print("Bonjour à vous, chers joueurs et joueuses !\n"
        "Bienvenue sur le fort pour jouer à ce jeu si mythique qu'est Fort Boyard !\n"
        "Lors de cette aventure avec votre équipe, vous devrez réussir plusieurs épreuves\n"
        "afin de récolter un objectif de trois clés pour accéder à la salle du trésor !\n"
        "Vous allez maintenant composer votre équipe.\n"
        "\n")
    input("Appuyer sur 'Entrée' pour composer votre équipe.\n"
          "\n")

def composer_equipe() :
    nombre_joueurs = int(input("Veuillez saisir le nombre de joueurs dans votre équipe : "))
    while nombre_joueurs <= 0 or nombre_joueurs > 3:
        print("Erreur. Votre équipe doit comporter entre 1 et 3 joueurs.")
        nombre_joueurs = int(input("Veuillez saisir le nombre de joueurs dans votre équipe : "))
    equipe = []
    cpt_leader = 0
    for i in range(nombre_joueurs) :
        print("\n")
        print(f"Saisie du joueur {i + 1} :")
        nom = input("Nom du joueur : ")
        profession = input("Profession : ")
        if cpt_leader == 0 :
            leader = input("Ce joueuer doit il être leader ? (oui/non) : ").lower()
            if leader == "oui" :
                cpt_leader = 1
                leader = "Leader"
            else :
                leader = "Membre"
        else :
            leader = "Membre"

        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": leader,
            "cles_gagnees": 0
        }

        equipe.append(joueur)

    if cpt_leader == 0 :
        print("Aucun joueur n'a été sélectionné comme Leader. Le joueur 1 a donc été sélectionné automatiquement comme Leader.")
        equipe[0]["leader"] = "Leader"

    print("\n")
    print("Voici votre équipe :")
    print("\n")
    for i in range(len(equipe)) :
        print(f"Joueur {i + 1} :", end="     ")
        print(f"Nom : {equipe[i]['nom']}")
        print(f"               Profession : {equipe[i]['profession']}")
        print(f"               Rôle : {equipe[i]['leader']}")
        print()

    return equipe


def menu_epreuve() :
    print("Choisissez votre epreuve en saisissant le numéro correspondant.")
    epreuves = {1 : "Épreuve de Mathématiques", 2 : "Épreuve de logique", 3 : "Épreuve de hasard", 4 : "Énigme du Père Fouras"}
    for numero, nom in epreuves.items():
        print(f"{numero}. {nom}")
    choix = 0
    while choix < 1 or choix > 4:
        choix = int(input("Choix : "))
    return choix



def choisir_joueur(equipe):
    print("Sélectionnez un joueur de l'équipe pour participer à cette épreuve.")
    i = 1

    for joueur in equipe:
        print(f"{i}. {joueur['nom']} ({joueur['profession']}) - {joueur['leader']}")
        i += 1

    joueur_choisi = int(input(("Entrez le numéro du joueur : ")))

    return equipe[joueur_choisi - 1]



equipe = composer_equipe()
