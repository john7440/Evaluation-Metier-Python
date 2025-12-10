from typing import List, Optional
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.vote import Vote

class VoteDao(Dao[Vote]):
    def create(self, obj: T) -> int:
        """Créer un vote"""
        pass

    def read(self, id_entity: int) -> Optional[Vote]:
        """Renvoie un vote en fonction de l'id souhaité"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                            SELECT Id_Vote,Id_Book, Id_JuryMember
                            FROM vote
                            WHERE Id_Vote = %s
                        """
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Vote(
                        id_vote=row["Id_Vote"],
                        id_book=row["Id_Book"],
                        id_jury_member=row["Id_JuryMember"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read Vote: {e}")
            return None


    def read_all(self) -> List[Vote]:
        """Renvoie une liste de tous les votes"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Vote,Id_Book, Id_JuryMember FROM vote"
                cursor.execute(sql)
                rows = cursor.fetchall()
                votes = []
                for row in rows:
                    votes.append(
                        Vote(
                            id_vote=row["Id_Vote"],
                            id_book=row["Id_Book"],
                            id_jury_member=row["Id_JuryMember"]
                        )
                    )
                return votes
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all de Vote: {e}")
            return []

    def update(self, obj: T) -> bool:
        """Update un vote"""
        pass

    def delete(self, obj: T) -> bool:
        """Supprimer un vote"""
        pass

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
                return cursor.fetchone()
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
                    INNER JOIN possess p ON b.Id_Book = p.Id_Book
                    WHERE p.Id_Selection = %s
                    GROUP BY b.Id_Book, b.b_title
                    ORDER BY votes DESC
                """
                cursor.execute(sql, (selection_id,))
                rows = cursor.fetchall()

                if not rows:
                    return f"Aucun vote pour la sélection {selection_id}"

                text = [f"=== Votes pour la sélection {selection_id} ==="]
                for r in rows:
                    text.append(f"{r['b_title']} : {r['votes']} vote(s)")
                return "\n".join(text)
        except pymysql.MySQLError as e:
            print(f"Erreur get_votes_by_selection: {e}")
            return "Erreur lors de la récupération des votes"

    def simulate_votes_selection_1_to_2(self):
        """
        Simuler les votes pour passer de la sélection 1 à la sélection 2
        """
        votes_data = [
            (1, 1),
            (3, 2),
            (15, 3),
            (6, 4),
            (10, 5),
            (7, 6),
            (11, 7),
            (3, 8),
            (3, 10),
            (2, 9)
        ]
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember) VALUES (%s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes comptabilisés avec succès !")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False

    def simulate_votes_selection_2_to_3(self):
        """
        Simuler les votes pour passer de la sélection 2 à la sélection 3
        """
        votes_data = [
            (1, 1),
            (1, 4),
            (3, 6),
            (2, 2),
            (2, 3),
            (3, 10),
            (3, 5),
            (3, 7),
            (7, 8),
            (3, 9)
        ]
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember) VALUES (%s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes enregistrés avec succès !")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False

    def simulate_votes_selection_3_to_4(self):
        """
        Simuler les votes pour passer de la sélection 3 à la sélection 4
        """
        votes_data = [
            (1, 1),
            (1, 4),
            (3, 6),
            (1, 2),
            (1, 3),
            (3, 10),
            (3, 5),
            (3, 7),
            (3, 8),
            (3, 9)
        ]
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO vote (Id_Book, Id_JuryMember) VALUES (%s, %s)"
                cursor.executemany(sql, votes_data)
                self.connection.commit()
                print(f"{len(votes_data)} votes enregistrés avec succès !")
                return True
        except pymysql.MySQLError as e:
            print(f"Erreur simulate_votes: {e}")
            self.connection.rollback()
            return False



