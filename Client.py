from Manager import Manager
from Voiture import Voiture


class Client:
    contour = 0
    clients = []
    reservations = []

    def __init__(self, nom, prenom, email, telephone):
        Client.contour += 1
        self.id_client = Client.contour
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        Client.clients.append(self)

    @staticmethod
    def obtenir_reservations():
        if not Client.reservations:
            print("Aucun reservation existe ")
        else:
            print("****** les reservation *********")
            for i, reservation in enumerate(Client.reservations, start=1):
                print(f"Reservation{i}:")
                print(f"voiture:{reservation['voiture'].id_voiture}")
                print(f"Date de début:{reservation['Date de début']}")
                print(f"Date de fin:{reservation['Date de fin']}")
                print("     ****      ")

    @staticmethod
    def reserver_voiture(id_voiture, date_debut, date_fin):
        reservation = {
            "id voiture": id_voiture,
            "Date de début": date_debut,
            "Date de fin": date_fin
        }
        Client.reservations.append(reservation)
        Manager.reservations.append(reservation)

    @staticmethod
    def annuler_reservation(voiture):
        for reservation in Client.reservations:
            if reservation['voiture'] == voiture:
                Client.reservations.remove(reservation)
                Manager.reservations_en_attente.append(reservation)
                print(f"la reservation de voiture {voiture} est annule avec succes ")

    @staticmethod
    def obtenir_client():
        return Client.clients
