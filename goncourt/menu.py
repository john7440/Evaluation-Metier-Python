
class Menu:
    def __init__(self, book_dao, selection_dao, vote_dao):
        self.book_dao = book_dao
        self.selection_dao = selection_dao
        self.vote_dao = vote_dao

        self.roles = {
            "user": "Utilisateur",
            "jury": "Membre du Jury",
            "president": "Président"
        }

    def authenticate(self) -> str:
        print("=== Connexion ===")
        print("1. Utilisateur")
        print("2. Membre du Jury")
        print("3. Président")

        choice = input("Sélectionnez votre rôle : ")

        if choice == "1":
            return "user"
        elif choice == "2":
            return "jury"
        elif choice == "3":
            return "president"
        else:
            print("Choix invalide.")
            return self.authenticate()

    def menu_user(self):
        while True:
            print("\n=== Menu Utilisateur ===")
            print("1. Afficher la sélection en cours")
            print("0. Quitter")

            choice = input("Votre choix: ")

            if choice == "1":
                print("\n--- Sélection en cours ---")
                print(self.book_dao.first_selection())
            elif choice == "0":
                print('\nVous quittez l\'application!')
                return
            else:
                print("Option invalide!")

    # ------------------------------
    # Menu Membre du Jury
    # ------------------------------
    def menu_jury(self):
        while True:
            print("\n=== Menu Membre du Jury ===")
            print("1. Afficher la sélection")
            print("2. Voter pour un livre")
            print("0. Quitter")

            choice = input("Votre choix : ")

            if choice == "1":
                print("\n--- Sélection en cours ---")
                print(self.selection_dao.get_current_selection())

            elif choice == "2":
                book_id = input("ID du livre pour lequel vous votez : ")
                self.vote_dao.vote_for_book(book_id)
                print("Vote enregistré !")

            elif choice == "0":
                print('\nVous quittez l\'application!')
                return
            else:
                print("Option invalide.")

    # ------------------------------
    # Menu Président
    # ------------------------------
    def menu_president(self):
        while True:
            print("\n=== Menu Président ===")
            print("1. Afficher la sélection")
            print("2. Mettre à jour une sélection")
            print("3. Consulter les votes")
            print("0. Quitter")

            choice = input("Votre choix : ")

            if choice == "1":
                print("\n--- Sélection en cours ---")
                print(self.selection_dao.get_current_selection())

            elif choice == "2":
                book_id = input("ID du livre : ")
                selection_id = input("Nouvelle sélection (1, 2, 3...) : ")
                self.selection_dao.update_selection(book_id, selection_id)
                print("Sélection mise à jour.")

            elif choice == "3":
                print("\n--- Votes enregistrés ---")
                print(self.vote_dao.get_votes())

            elif choice == "0":
                print('\nVous quittez l\'application!')
                return
            else:
                print("Option invalide!")

    def run(self):
        role = self.authenticate()

        if role == "user":
            self.menu_user()
        elif role == "jury":
            self.menu_jury()
        elif role == "president":
            self.menu_president()
