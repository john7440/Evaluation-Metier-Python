from typing import List, Optional
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.vote import Vote

class VoteDao(Dao[Vote]):
    def create(self, obj: T) -> int:
        """Créer un vote"""
        pass

    def read(self, id_entity: int) -> Optional[Vote]:
        try:
            with self.connection.cursor() as cursor:
                sql = """
                            SELECT Id_Vote, number_vote, Id_Book, Id_JuryMember
                            FROM vote
                            WHERE Id_Vote = %s
                        """
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Vote(
                        id_vote=row["Id_Vote"],
                        number_vote=row["number_vote"],
                        id_book=row["Id_Book"],
                        id_jury_member=row["Id_JuryMember"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read Vote: {e}")
            return None


    def read_all(self) -> List[Vote]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Vote, number_vote, Id_Book, Id_JuryMember FROM vote"
                cursor.execute(sql)
                rows = cursor.fetchall()
                votes = []
                for row in rows:
                    votes.append(
                        Vote(
                            id_vote=row["Id_Vote"],
                            number_vote=row["number_vote"],
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

    def vote_for_book(self, book_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO vote (Id_Book) VALUES (%s)"
            cursor.execute(sql, (book_id,))
            self.connection.commit()

    def get_votes(self):
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



