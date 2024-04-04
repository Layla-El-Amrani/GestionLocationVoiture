class Manager:
    contour = 0
    voitures = []
    reservations = []




    def __init__(self, nom, prenom, email, mot_de_passe):
        self.id_manager = Manager.contour
        Manager.contour += 1
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe

    @staticmethod
    def obtenir_voiture():
        if not Manager.voitures:
            print('aucun voiture existe')
        else:
            print('**** list des voiture ****')
            for i, voiture in enumerate(Manager.voitures, start=1):
                print(f"********* voiture {i} *********")
                print(f"id_voiture : {voiture.id_voiture}")
                print(f"marque : {voiture.marque}")
                print(f"modele : {voiture.modele}")
                print(f"immatriculation : {voiture.immatriculation}")
                print(f"prix : {voiture.prix}")
                print(f"disponibilite : {voiture.disponibilite}")

    @staticmethod
    def ajouter_voiture(voiture):
        Manager.voitures.append(voiture)
        print("Voiture ajouter avec success")

    @staticmethod
    def modifier_voiture(id_voiture, nouveau_prix):
        for voiture in Manager.voitures:
            if voiture.id_voiture == id_voiture:
                voiture.prix = nouveau_prix
                print(f"la voiture de id {id_voiture} est modifier avec success")

    @staticmethod
    def supprimer_voiture(id_voiture):
        for voiture in Manager.voitures:
            if voiture.id_voiture == id_voiture:
                Manager.voitures.remove(voiture)
                print(f"la voiture de id {id_voiture} est supprimer avec success")

    @staticmethod
    def obtenir_reservations():
        if not Manager.reservations:
            print("aucun reservation ,n'été effectue ")
        else:
            print('liste de tout les reservation ')
            for reservation in Manager.reservations:
                print(reservation)

    @staticmethod
    def accept_reservation(id_voiture):
        for voiture in Manager.voitures:
            if voiture.id_voiture == id_voiture and voiture.disponibilite == "En cours":
                voiture.disponibilite = "Reserve"
                print('la reservation est accepter avec success')
            else:
                print('aucun voiture est reserve ')

    @staticmethod
    def refuse_reservation(id_voiture):
        for voiture in Manager.voitures:
            if voiture.id_voiture == id_voiture and voiture.disponibilite == "En cours":
                voiture.disponibilite = "disponible"
                print('la reservation est refusé avec success')
            else:
                print('aucun voiture est reserve ')
