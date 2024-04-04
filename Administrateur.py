from Manager import Manager


class Administrateur(Manager):
    managers = []

    def __init__(self, id_administrateur, nom, prenom, email, mot_de_passe):
        super().__init__(nom, prenom, email, mot_de_passe)
        self.id_administrateur = id_administrateur

    @staticmethod
    def obtenir_managers():
        if not Administrateur.managers:
            print("Aucun manager n'existe actuellement")
        else:
            print("***   list des managers   ***")
            for i, manager in enumerate(Administrateur.managers, start=1):
                print(f"*****    manager {i}   *****")
                print(f"id : {manager.id_manager}")
                print(f"nom : {manager.nom}")
                print(f"prenom : {manager.prenom}")
                print(f"email : {manager.email}")
                print(f"mot de passe : {manager.mot_de_passe}")
                print("************************")

    @staticmethod
    def ajouter_manager(manager):
        Administrateur.managers.append(manager)
        print("Le manager a été ajouté avec succès")

    @staticmethod
    def modifier_manager(id_manager, nouveau_email, nouveau_mot_de_passe):
        for manager in Administrateur.managers:
            if manager.id_manager == id_manager:
                manager.email = nouveau_email
                manager.mot_de_passe = nouveau_mot_de_passe
                print("Les modifications ont été effectuées avec succès ")
            else:
                print("Aucun manager n'existe avec cet identifiant")

    @staticmethod
    def supprimer_manager(id_manager_supprimer):
        for manager in Administrateur.managers:
            if manager.id_manager == id_manager_supprimer:
                Administrateur.managers.remove(manager)
                print("Le manager a été supprimé avec succès")
            else:
                print("Aucun manager ne correspond à cet id")
