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
        print("\n=== Connexion ===")
        print("1. Utilisateur")
        print("2. Membre du Jury")
        print("3. Président")

        choice = input("Sélectionnez votre rôle : ")

        role_map = {"1": "user", "2": "jury", "3": "president"}

        if choice in role_map:
            return role_map[choice]
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

    def show_votes_submenu(self):
        """Sous-menu pour la consultation des votes"""
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

    def simulate_vote(self, selection_transition: str):
        """Simuler les votes selon la transition de sélection"""
        print("\n--- Simulation de votes ---")

        vote_functions = {
            "1->2": self.vote_dao.simulate_votes_selection_1_to_2,
            "2->3": self.vote_dao.simulate_votes_selection_2_to_3,
            "3->4": self.vote_dao.simulate_votes_selection_3_to_4
        }

        if selection_transition in vote_functions:
            vote_functions[selection_transition]()
        else:
            print("Transition de sélection invalide")

    @staticmethod
    def display_menu_and_get_choice(menu_title: str, options: list) -> str:
        """Afficher un menu générique et récupérer le choix"""
        print(f"\n=== {menu_title} ===")
        for option in options:
            print(option)
        return input("Votre choix : ")

    @staticmethod
    def handle_exit_and_return(choice: str) -> bool:
        """Gérer les options pour quitter (0) et retour
        Retourne True si on doit sortir du menu sinon False"""
        if choice == "0":
            print('\nVous quittez l\'application!')
            exit()
        return False

    #Menu user
    def menu_user(self):
        options = [
            "1. Afficher la sélection en cours",
            "2. Revenir au Menu Principal",
            "0. Quitter"
        ]

        while True:
            choice = self.display_menu_and_get_choice("Menu Utilisateur", options)

            if choice == "1":
                self.display_current_selection()
            elif choice == "2":
                return
            elif self.handle_exit_and_return(choice):
                return
            else:
                print("Option invalide!")


    # Menu Membre du Jury
    def menu_jury(self):
        options = [
            "1. Afficher la sélection",
            "2. Voter pour un livre (sélection 1 -> 2)",
            "3. Voter pour un livre (sélection 2 -> 3)",
            "4. Voter pour un livre (sélection 3 -> 4)",
            "5. Revenir au Menu Principal",
            "0. Quitter"
        ]

        while True:
            choice = self.display_menu_and_get_choice("Menu Membre du Jury", options)

            if choice == "1":
                self.display_current_selection()
            elif choice == "2":
                self.simulate_vote("1->2")
            elif choice == "3":
                self.simulate_vote("2->3")
            elif choice == "4":
                self.simulate_vote("3->4")
            elif choice == "5":
                return
            elif self.handle_exit_and_return(choice):
                return
            else:
                print("Option invalide!")


    # Menu Président
    def menu_president(self):
        options = [
            "1. Afficher la sélection",
            "2. Passer à la sélection suivante",
            "3. Consulter les votes",
            "4. Revenir au Menu Principal",
            "0. Quitter"
        ]

        while True:
            choice = self.display_menu_and_get_choice("Menu Président", options)

            if choice == "1":
                self.display_current_selection()
            elif choice == "2":
                self.selection_dao.go_to_next_selection()
            elif choice == "3":
                self.show_votes_submenu()
            elif choice == "4":
                return
            elif self.handle_exit_and_return(choice):
                return
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
