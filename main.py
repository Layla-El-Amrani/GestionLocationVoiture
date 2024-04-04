from datetime import datetime
from Administrateur import Administrateur
from Voiture import Voiture
from Client import Client
from Manager import Manager

administrateur = Administrateur("1", "el amrani", "layla", "layla@gmail.com", "123")

print("***    Bienvenue dans notre système de réservation de voitures!   ***")
while True:
    print("Choisissez votre catégorie d'accès :")
    print("1.Administrateur")
    print("2.Manager")
    print("3.Client")
    print("taper 4 pour quiter")

    choix = input("Veuillez entrer le numero correspond a votre catégorie d'accès :")
    if choix == "1":
        nom_utilisateur = input("nom de l utilisateur :")
        mot_de_passe = input('mot de passe :')
        while True:
            if administrateur.prenom == nom_utilisateur and administrateur.mot_de_passe == mot_de_passe:
                print("********  Menu   ********")
                print("1.Ajouter un manager")
                print("2.Voir les managers")
                print("3.Modifier les informations d'un manager")
                print("4.Supprimer un manager")
                print("5.Quitter")
                print("**************************")
                choix = input('Veuiller choisir un nombre :')
                if choix == "1":
                    print('Veuillez saisir les information de manager')
                    nom = input("nom: ")
                    prenom = input("prénom: ")
                    email = input("email :")
                    mot_passe = input("mot de passe: ")
                    manager = Manager(nom, prenom, email, mot_passe)
                    administrateur.ajouter_manager(manager)
                elif choix == "2":
                    administrateur.obtenir_managers()
                elif choix == "3":
                    id_manager = int(input('Veuillez entrer id de manager :'))
                    nouveau_email = input('Veuillez entrer le nouveux email de manager :')
                    nouveau_mot_de_passe = input('Veuillez entrer le nouveau mot de passe :')
                    administrateur.modifier_manager(id_manager, nouveau_email, nouveau_mot_de_passe)
                elif choix == "4":
                    id_manager = int(input('Veuillez entrer id de manager :'))
                    administrateur.supprimer_manager(id_manager)
                elif choix == "5":
                    print("Merci d'avoir utilisé notre système de réservation de voitures. Au revoir !")
                    break
                else:
                    print("Veuillez sélectionner un nombre valide.")

            else:
                print(
                    "les informations d'identification sont incorrectes, vous pouvez accéder en tant que manager ou "
                    "client, si vous n'ête pas administrateur")
                break

    elif choix == '2':
        nom_utilisateur = input("nom de l utilisateur :")
        mot_de_passe = input('mot de passe :')
        for manager in administrateur.managers:
            if manager.nom == nom_utilisateur and manager.mot_de_passe == mot_de_passe:
                while True:
                    print("********  Menu   ********")
                    print("1.Gérer les voitures")
                    print("2.Gérer les réservations")
                    print("3.Gérer les clients")
                    print("4.Quiter")
                    print("**************************")
                    choix = input("Veuillez entrer un nombre :")
                    if choix == "1":
                        while True:
                            print("********  Menu   ********")
                            print("1.Ajouter une voiture")
                            print("2.Afficher les voitures")
                            print("3.Modifier une voiture")
                            print("4.Supprimer une voiture")
                            print("5.Quiter")
                            print("**************************")
                            choix = input("Veuillez entrer un nombre :")
                            if choix == '1':
                                print("Veuillez saisir les information des voiture :")
                                marque = input("marque :")
                                immatriculation = input("immatriculation :")
                                modele = input("modele :")
                                prix = input("prix par jour:")
                                voiture = Voiture(marque, immatriculation, modele, prix,
                                                  disponibilite='disponible')
                                manager.ajouter_voiture(voiture)
                            elif choix == '2':
                                manager.obtenir_voiture()
                            elif choix == '3':
                                id_voiture = input('Veuillez saisir id de voiture :')
                                nouveau_prix_voiture = input('Veuillez saisir le nouveaux prix de voiture :')
                                manager.modifier_voiture(id_voiture, nouveau_prix_voiture)
                            elif choix == '4':
                                id_voiture = input('Veuillez saisir id de voiture')
                                manager.supprimer_voiture(id_voiture)
                            elif choix == "5":
                                break
                            else:
                                print("Veuillez sélectionner un nombre valide !")

                    elif choix == "2":
                        while True:
                            print("********  Menu   ********")
                            print("1.Afficher les réservations")
                            print("2.Accepter une réservation")
                            print("3.Refuser une réservation")
                            print("4.Quitter")
                            print("**************************")

                            choix = input("Veuillez entrer un nombre :")
                            if choix == '1':
                                manager.obtenir_reservations()
                            elif choix == '2':
                                id_voiture = input('Veuillez saisir id de voiture de reservation :')
                                manager.accept_reservation(id_voiture)
                            elif choix == '3':
                                id_voiture = input('Veuillez saisir id de voiture de reservation : ')
                                manager.refuse_reservation(id_voiture)
                            elif choix == '4':
                                break
                            else:
                                print("Veuillez sélectionner un nombre valide !")
                    elif choix == "3":
                        while True:
                            print("********  Menu   ********")
                            print("1.ajouter les clients")
                            print("2.Afficher les clients")
                            print("3.Modifier les informations d'un client")
                            print("4.Quiter")
                            choix = input("Veuillez entrer un nombre :")
                            if choix == '1':
                                print('Veuillez saisir les information de client')
                                nom = input('nom :')
                                prenom = input('prenom :')
                                email = input('email :')
                                telephone = input('telephone :')

                                client = Client(nom, prenom, email, telephone)
                                Client.clients.append(client)
                            elif choix == '2':
                                Clients = Client.clients
                                if not Clients:
                                    print("Aucun client existe ")
                                else:
                                    print("****** list des client *********")
                                    for i, client in enumerate(Client.clients, start=1):
                                        print(f"*******  client{i}   *******:")
                                        print(f"id :{client.id_client}")
                                        print(f"nom:{client.id_client}")
                                        print(f"prenom:{client.id_client}")
                                        print(f"email:{client.email}")
                                        print(f"telephone:{client.telephone}")
                                        print(f"****************************:")

                            if choix == '3':
                                id_client = input('Veuillez saisir id client :')
                                numero_telephone = input('Veuillez saisir le nouveaux numero de telephone ')
                                for client in Client.clients:
                                    if client.id_client == id_client:
                                        client.telephone = numero_temlephone
                                        print(f"la client de id {id_client} est modifier avec success")
                            elif choix == "4":
                                break
                            else:
                                print("Veuillez sélectionner un nombre invalide !")

                    elif choix == "4":
                        break
                    else:
                        print("Veuillez choisir un choix invalid !")
                else:
                    print("nom d'utilisateur es incorrecte ")

                break


    elif choix == '3':
        while True:
            print("********  Menu   ********")
            print("1.Rechercher une voiture")
            print("2.Afficher les détails d'une voiture")
            print("3.Réserver une voiture")
            print("4.Annuler une réservation")
            print("5.Quitter")
            print("**************************")
            choix = input('Veuiller choisir un nombre :')
            if choix == "1":
                marque_voiture = input('Veuillez saisir le marque de voiture :')
                for voiture in Voiture.voitures:
                    if voiture.marque == marque_voiture:
                        voiture.obtenir_details()
                    else:
                        print("aucun voiture existe de avex ce marque")
            elif choix == "2":
                for voiture in Voiture.voitures:
                    if voiture.disponibilite == 'disponible':
                        voiture.obtenir_details()
            elif choix == "3":
                id_voiture = input("Veuillez saisir id voiture :")
                date_debut_str = input("Veuillez saisir la date de début (au format YYYY-MM-DD) : ")
                date_fin_str = input("Veuillez saisir la date de fin (au format YYYY-MM-DD) : ")
                date_debut = datetime.strptime(date_debut_str, "%Y-%m-%d")
                date_fin = datetime.strptime(date_fin_str, "%Y-%m-%d")
                if date_debut < date_fin:
                    Client.reserver_voiture(id_voiture, date_debut, date_fin)
                    print("La voiture est reserve pour la période du", date_debut.strftime("%Y-%m-%d"), "au",date_fin.strftime("%Y-%m-%d"))
                    print("Veuillez saisir vos informations pour confirmer la réservation :")
                    nom = input('nom :')
                    prenom = input('prenom :')
                    email = input('email :')
                    telephone = input('telephone :')
                    client = Client(nom, prenom, email, telephone)
                    Client.clients.append(client)
                    for voiture in Voiture.voitures:
                        if str(voiture.id_voiture) == id_voiture:
                            if voiture.reserver():
                                print("La réservation a été effectuée avec succès.")
                            else:
                                print("Impossible de réserver la voiture. Veuillez réessayer.")
                            break
                    print(
                        'Nous vous remercions d\'utiliser notre service. Veuillez patienter pendant que notre équipe de gestion confirme votre réservation.')
                else:
                    print("Erreur : La date de fin doit être postérieure à la date de début.")



            elif choix == "4":
                id_voiture = input("Veuillez saisir id voiture :")
                Voiture.annuler_reservation(id_voiture)
            elif choix == "5":
                break
            else:
                print("Veuillez sélectionner un nombre invalide !")

    elif choix == '4':
        print("Merci d'avoir utilisé notre système de réservation de voitures. Au revoir !")
        break
    else:
        print("Veuillez sélectionner un nombre invalide !")
