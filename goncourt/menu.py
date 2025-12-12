class Menu:
    """
      Classe Menu permettant de gérer l'interaction utilisateur
      pour un système de sélection et de votes de livres.

      Attributs :
          book_dao : accès aux données des livres
          selection_dao : accès aux données des sélections
          vote_dao : accès aux données des votes
          roles : dictionnaire des rôles disponibles (user, jury, président)
      """
    def __init__(self, book_dao, selection_dao, vote_dao, jury_dao):
        """
        Initialise le menu avec les DAO nécessaires
        Args :
        - book_dao : DAO pour les livres
        - selection_dao : DAO pour les sélections
        - vote_dao : DAO pour les votes
        """
        self.book_dao = book_dao
        self.selection_dao = selection_dao
        self.vote_dao = vote_dao
        self.jury_dao = jury_dao

        self.roles = {
            "jury": "Membre du Jury",
            "president": "Président"
        }

    def authenticate(self) -> str:
        """
        Permet à l'utilisateur de choisir son rôle
        Returns :
        str : rôle choisi ("jury" ou "president")
        """
        print("\n=== Connexion ===")
        print("1. Membre du Jury")
        print("2. Président")

        choice = input("Sélectionnez votre rôle : ")

        role_map = {"1": "jury", "2": "president"}

        if choice in role_map:
            return role_map[choice]
        else:
            print("Choix invalide.")
            return self.authenticate()

    def menu_login(self):
        """Menu de connexion pour le président"""
        print("\n" + "==== Connexion - Espace Président ====")

        login = input("Identifiant: ").strip()
        password = input("Mot de passe: ").strip()

        if not login or not password:
            print("\nLogin et mot de passe requis!")
            input("Appuyez sur Entrée pour continuer...")
            return None

        #verifs
        jury_member = self.jury_dao.authenticate(login, password)

        if jury_member is None:
            print("\nIdentifiant invalide! Veuillez réessayer!")
            print("Appuyez sur Entré pour continuer")
            return None

        if not self.jury_dao.is_president(jury_member):
            print("Accès réservé au président uniquement!")
            input("Appuyez sur Entrée pour continuer...")
            return None

        print(f"Bienvenue {jury_member.first_name} {jury_member.last_name}!")
        input("Appuyez sur Entrée pour continuer...")
        return jury_member

    def menu_login_jury(self):
        """Menu de connexion pour le jury"""
        print("=== CONNEXION - Espace Membre du Jury ===")

        login = input("Identifiant: ").strip()
        password = input("Mot de passe: ").strip()

        if not login or not password:
            print("\nLogin et mot de passe requis!")
            input("Appuyez sur Entrée pour continuer...")
            return None

        jury_member = self.jury_dao.authenticate(login, password)

        if jury_member is None:
            print("\nIdentifiant invalide! Veuillez réessayer!")
            input("Appuyez sur Entrée pour continuer...")
            return None

        print(f"\nBienvenue {jury_member.first_name} {jury_member.last_name}!")
        input("Appuyez sur Entrée pour continuer...")
        return jury_member



    def display_current_selection(self):
        """
        Affiche la sélection de livres en cours
        """
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


    def menu_jury(self):
        """
        Menu destiné aux membres du jury
        """
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

    def menu_president(self,jury_member):
        """Menu réservé au président après connexion"""
        while True:

            print(f"=== ESPACE PRÉSIDENT - {jury_member.first_name} {jury_member.last_name} ===")
            print("1. Voir la sélection actuelle")
            print("2. Passer à la sélection suivante")
            print("3. Consulter les votes")
            print("4. Voir le gagnant")
            print("0. Déconnexion")

            choix = input("Votre choix: ").strip()

            if choix == "1":
                print("\n" + self.selection_dao.get_current_selection())
                input("\nAppuyez sur Entrée pour continuer...")

            elif choix == "2":
                confirm = input("Confirmer le passage à la sélection suivante? (o/n): ")
                if confirm.lower() == 'o':
                    if self.selection_dao.go_to_next_selection():
                        print("Sélection suivante créée avec succès!")
                    else:
                        print("Erreur lors du passage à la sélection suivante")
                input("\nAppuyez sur Entrée pour continuer...")

            elif choix == "3":
                active = self.selection_dao.get_active_selection()
                if active:
                    print(self.vote_dao.get_votes_by_selection(active.id_selection))
                else:
                    print("Aucune sélection active")
                input("\nAppuyez sur Entrée pour continuer...")

            elif choix == "4":
                winner = self.vote_dao.get_winner()
                if winner:
                    print(f"\nLivre gagnant: {winner['b_title']}")
                    print(f"Auteur: {winner['a_first_name']} {winner['a_last_name']}")
                    print(f"Votes: {winner['votes']}")
                else:
                    print("Aucun vote enregistré")
                input("\nAppuyez sur Entrée pour continuer...")

            elif choix == "0":
                print("Déconnexion...")
                break

            else:
                print("Choix invalide!")
                input("Appuyez sur Entrée pour continuer...")

    def menu_principal(self):
        """
        Menu principal accessible sans authentification
        """
        options = [
            "1. Voir la sélection actuelle",
            "2. S'authentifier (Président)",
            "0. Quitter"
        ]

        while True:
            choice = self.display_menu_and_get_choice("PRIX GONCOURT - Menu Principal", options)

            if choice == "1":
                self.display_current_selection()
            if choice == "2":
                logged_member = self.menu_login()
                if logged_member:
                    self.menu_president(logged_member)
            elif self.handle_exit_and_return(choice):
                return
            else:
                print("Option invalide!")

    def run(self):
        """
        Lance le menu principal
        """
        self.menu_principal()
