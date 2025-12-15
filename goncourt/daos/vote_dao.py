from datetime import date
from typing import List, Optional
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.vote import Vote

class VoteDao(Dao[Vote]):
    def create(self, obj: Vote) -> int:
        """Créer un vote"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO vote (Id_Book, Id_JuryMember, Id_selection, v_date) VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (obj.id_book,obj.id_jury_member, obj.id_selection, obj.vote_date))
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.MySQLError as e:
            print(f"Erreur lors de la création du vote: {e}")
            self.connection.rollback()
            return 0

    def read(self, id_entity: int) -> Optional[Vote]:
        """Renvoie un vote en fonction de l'id souhaité"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                     SELECT Id_Vote, Id_Book, Id_JuryMember, v_date, v_value
                     FROM vote
                     WHERE Id_Vote = %s
                     """
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Vote(
                        id_vote=row["Id_Vote"], # type: ignore
                        id_book=row["Id_Book"], # type: ignore
                        id_jury_member=row["Id_JuryMember"], # type: ignore
                        id_selection=row["Id_Selection"], # type: ignore
                        vote_date=row["v_date"] # type: ignore
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read Vote: {e}")
            return None


    def read_all(self) -> List[Vote]:
        """Renvoie une liste de tous les votes"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Vote, Id_Book, Id_JuryMember, Id_Selection, v_date FROM vote"
                cursor.execute(sql)
                rows = cursor.fetchall()
                votes = []
                for row in rows:
                    votes.append(
                        Vote(
                            id_vote=row["Id_Vote"], # type: ignore
                            id_book=row["Id_Book"], # type: ignore
                            id_jury_member=row["Id_JuryMember"], # type: ignore
                            id_selection=row["Id_Selection"], # type: ignore
                            vote_date=row["v_date"] # type: ignore
                        )
                    )
                return votes
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all de Vote: {e}")
            return []

    def update(self, obj: T) -> bool:
        """Update un vote"""
        return True

    def delete(self, obj: Vote) -> bool:
        """Supprimer un vote"""
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM vote WHERE Id_Vote = %s"
                cursor.execute(sql, (obj.id_vote,))
                self.connection.commit()
                return cursor.rowcount > 0
        except pymysql.MySQLError as e:
            print(f"Erreur lors de la suppression du vote: {e}")
            self.connection.rollback()
            return False


    def get_votes(self):
        """
        Récupère et affiche le nombre de votes par livre
        La requête SQL compte le nombre de votes associés à chaque livre,
        puis les classe par ordre décroissant
        """
        with self.connection.cursor() as cursor:
            sql = """
                SELECT b_title, COUNT(*) AS votes
                FROM vote
                INNER JOIN book ON vote.Id_Book = book.Id_Book
                GROUP BY book.Id_Book
                ORDER BY votes DESC;
            """
            cursor.execute(sql)
            rows = cursor.fetchall()

        text = []
        for r in rows:
            text.append(f"{r['b_title']} : {r['votes']} votes")
        return "\n".join(text)

    def get_winner(self) -> Optional[dict]:
        """Récupérer le livre gagnant (celui avec le plus de votes)"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT b.Id_Book, b.b_title, a.a_first_name, a.a_last_name, 
                           COUNT(v.Id_Vote) AS votes
                    FROM vote v
                    INNER JOIN book b ON v.Id_Book = b.Id_Book
                    INNER JOIN author a ON b.Id_Author = a.Id_Author
                    GROUP BY b.Id_Book, b.b_title, a.a_first_name, a.a_last_name
                    ORDER BY votes DESC
                    LIMIT 1
                """
                cursor.execute(sql)
                return cursor.fetchone()  # type: ignore
        except pymysql.MySQLError as e:
            print(f"Erreur get_winner: {e}")
            return None

    def get_votes_by_selection(self, selection_id: int) -> str:
        """Récupérer les votes pour une sélection spécifique"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT b.b_title, COUNT(v.Id_Vote) AS votes
                    FROM vote v
                    INNER JOIN book b ON v.Id_Book = b.Id_Book
                    WHERE v.Id_Selection = %s
                    GROUP BY b.Id_Book, b.b_title
                    ORDER BY votes DESC
                """
                cursor.execute(sql, (selection_id,))
                rows = cursor.fetchall()

                if not rows:
                    return f"Aucun vote pour la sélection {selection_id}"

                text = [f"=== Votes pour la sélection {selection_id} ==="]
                for r in rows:
                    text.append(f"{r['b_title']} : {r['votes']} vote(s)")  # type: ignore
                return "\n".join(text)
        except pymysql.MySQLError as e:
            print(f"Erreur get_votes_by_selection: {e}")
            return "Erreur lors de la récupération des votes"


    def simulate_votes_selection_1_to_2(self):
        """
        Simuler les votes pour passer de la sélection 1 à la sélection 2
        """
        target_selection = 1

        # vérifs
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT Id_Selection FROM selection WHERE s_number = %s", (target_selection,))
                if not cursor.fetchone():
                    print(f"La sélection {target_selection} n'existe pas!")
                    return False

            votes_data = [
                (1, 1, target_selection, date.today()),
                (3, 2, target_selection, date.today()),
                (15, 3, target_selection, date.today()),
                (6, 4, target_selection, date.today()),
                (10, 5, target_selection, date.today()),
                (7, 6, target_selection, date.today()),
                (11, 7, target_selection, date.today()),
                (3, 8, target_selection, date.today()),
                (3, 10, target_selection, date.today()),
                (2, 9, target_selection, date.today())
            ]

            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember, Id_Selection, v_date) VALUES (%s, %s, %s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes comptabilisés avec succès pour la sélection {target_selection}!")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False


    def simulate_votes_selection_2_to_3(self):
        """
        Simuler les votes pour passer de la sélection 2 à la sélection 3
        """
        target_selection = 2

        # vérifs
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT Id_Selection FROM selection WHERE s_number = %s", (target_selection,))
                result = cursor.fetchone()

                if not result:
                    cursor.execute("INSERT INTO selection (s_date, s_number) VALUES (NOW(), %s)", (target_selection,))
                    self.connection.commit()
                    print(f"Sélection {target_selection} créée")

            votes_data = [
                (1, 1, target_selection, date.today()),
                (1, 4, target_selection, date.today()),
                (3, 6, target_selection, date.today()),
                (2, 2, target_selection, date.today()),
                (2, 3, target_selection, date.today()),
                (3, 10, target_selection, date.today()),
                (3, 5, target_selection, date.today()),
                (3, 7, target_selection, date.today()),
                (7, 8, target_selection, date.today()),
                (3, 9, target_selection, date.today())
            ]

            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember, Id_Selection, v_date) VALUES (%s, %s, %s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes enregistrés avec succès pour la sélection {target_selection}!")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False


    def simulate_votes_selection_3_to_4(self):
        """
        Simuler les votes pour passer de la sélection 3 à la sélection 4
        """
        target_selection = 3

        # vérifs
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT Id_Selection FROM selection WHERE s_number = %s", (target_selection,))
                result = cursor.fetchone()

                if not result:
                    cursor.execute("INSERT INTO selection (s_date, s_number) VALUES (NOW(), %s)", (target_selection,))
                    self.connection.commit()
                    print(f"Sélection {target_selection} créée")

            votes_data = [
                (1, 1, target_selection, date.today()),
                (1, 4, target_selection, date.today()),
                (3, 6, target_selection, date.today()),
                (1, 2, target_selection, date.today()),
                (1, 3, target_selection, date.today()),
                (3, 10, target_selection, date.today()),
                (3, 5, target_selection, date.today()),
                (3, 7, target_selection, date.today()),
                (3, 8, target_selection, date.today()),
                (3, 9, target_selection, date.today())
            ]

            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember, Id_Selection, v_date) VALUES (%s, %s, %s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes enregistrés avec succès pour la sélection {target_selection}!")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False
