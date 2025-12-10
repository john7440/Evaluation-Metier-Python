
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

    def display_current_selection(self):
        sel = self.selection_dao.get_active_selection()

        if not sel:
            print("Aucune sélection disponible")
            return

        print(f"\n>>> Sélection en cours : numéro {sel.number_selection}\n")

        books = self.selection_dao.get_books_from_selection(sel.id_selection)

        if not books:
            print("Aucun livre dans cette sélection")
            return

        for i,b in enumerate(books, start =1):
            print(f"{i}. {b['b_title']} — {b['a_first_name']} {b['a_last_name']} (Éditeur : {b['p_name']})")

    #Menu user
    def menu_user(self):
        while True:
            print("\n=== Menu Utilisateur ===")
            print("1. Afficher la sélection en cours")
            print("2. Revenir au Menu Principal")
            print("0. Quitter")

            choice = input("Votre choix: ")

            if choice == "1":
                self.display_current_selection()
            elif choice == "2":
                return
            elif choice == "0":
                print('\nVous quittez l\'application!')
                exit()
            else:
                print("Option invalide!")

    # ------------------------------
    # Menu Membre du Jury
    # ------------------------------
    def menu_jury(self):
        while True:
            print("\n=== Menu Membre du Jury ===")
            print("1. Afficher la sélection")
            print("2. Voter pour un livre(selection 1 -> 2)")
            print("4. Revenir au Menu Principal")
            print("0. Quitter")

            choice = input("Votre choix : ")

            if choice == "1":
                self.display_current_selection()

            elif choice == "2":
                print("\n--- Simulation de votes ---")
                self.vote_dao.simulate_votes_selection_1_to_2()

            elif choice == "4":
                return

            elif choice == "0":
                print('\nVous quittez l\'application!')
                exit()
            else:
                print("Option invalide!")

    # ------------------------------
    # Menu Président
    # ------------------------------
    def menu_president(self):
        while True:
            print("\n=== Menu Président ===")
            print("1. Afficher la sélection")
            print("2. Passer a la sélection suivante")
            print("3. Consulter les votes")
            print("4. Mettre à jour une sélection")
            print("5. Revenir au Menu Principal")
            print("0. Quitter")

            choice = input("Votre choix : ")

            if choice == "1":
                self.display_current_selection()

            elif choice == "2":
                self.selection_dao.go_to_next_selection()

            elif choice == "3":
                print("\n=== Consultation des Votes ===")
                print("1. Voir tous les votes")
                print("2. Voir les votes de la sélection en cours")
                print("3. Voir le gagnant actuel")

                sub_choice = input("Votre choix : ")

                if sub_choice == "1":
                    print("\n--- Tous les votes ---")
                    print(self.vote_dao.get_votes())

                elif sub_choice == "2":
                    sel = self.selection_dao.get_active_selection()
                    if sel:
                        print(self.vote_dao.get_votes_by_selection(sel.id_selection))
                    else:
                        print("Aucune sélection active")

                elif sub_choice == "3":
                    winner = self.vote_dao.get_winner()
                    if winner:
                        print(f"\nGagnant actuel : {winner['b_title']}")
                        print(f"   Auteur : {winner['a_first_name']} {winner['a_last_name']}")
                        print(f"   Votes : {winner['votes']}")
                    else:
                        print("Aucun vote enregistré")

            elif choice == "4":
                book_id = input("ID du livre : ")
                selection_id = input("Nouvelle sélection (1, 2, 3...) : ")
                self.selection_dao.update_selection(book_id, selection_id)
                print("Sélection mise à jour.")

            elif choice == "5":
                return

            elif choice == "0":
                print('\nVous quittez l\'application!')
                exit()

            else:
                print("Option invalide!")

    #Lancement du menu
    def run(self):
        while True:
            role = self.authenticate()

            if role == "user":
                self.menu_user()
            elif role == "jury":
                self.menu_jury()
            elif role == "president":
                self.menu_president()
