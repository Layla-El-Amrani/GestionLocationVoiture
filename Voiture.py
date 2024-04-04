class Voiture:
    contour = 0
    voitures = []

    def __init__(self, marque, modele, immatriculation, prix, disponibilite="disponible"):
        Voiture.contour += 1
        self.id_voiture = Voiture.contour
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation
        self.prix = prix
        self.disponibilite = disponibilite
        Voiture.voitures.append(self)

    @staticmethod
    def obtenir_details():
        if not Voiture.voitures:
            print('aucun voiture existe')
        else:
            print('**** list des voiture ****')
            for i, voiture in enumerate(Voiture.voitures, start=1):
                print(f"********* voiture {i} *********")
                print(f"id_voiture : {voiture.id_voiture}")
                print(f"marque : {voiture.marque}")
                print(f"modele : {voiture.modele}")
                print(f"immatriculation : {voiture.immatriculation}")
                print(f"prix par jour: {voiture.prix} € par jour")
                print(f"disponibilite : {voiture.disponibilite}")

    def reserver(self):
        if self.disponibilite == "disponible":
            self.disponibilite = "En cours"
            print("La voiture a été réservée avec succès.")
            return True
        else:
            print("La voiture n'est pas disponible pour la réservation.")
            return False


    @staticmethod
    def annuler_reservation(id_voiture):
        for voiture in Voiture.voitures:
            if voiture.id_voiture == id_voiture and voiture.disponibilite == "En cours":
                print(
                    f"Votre demande de réservation pour la voiture est anneule avec succes")
                voiture.disponibilite = "disponible"
            else:
                print("aucun voiture de ce id est reserve ")
