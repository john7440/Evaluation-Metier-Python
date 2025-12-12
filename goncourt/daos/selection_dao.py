from sys import exec_prefix
from typing import List, Optional
import pymysql

from goncourt.models.book import Book
from goncourt.models.selection import Selection
from goncourt.daos.dao import Dao, T

class SelectionDao(Dao[Selection]):
    def update(self, obj: T) -> bool:
        """Update une selection"""
        return True

    def create(self, obj: Selection) -> int:
        """Créer un selection"""
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO selection(s_date, s_number) VALUES (%s, %s)"
                cursor.execute(sql,(obj.date_selection, obj.number_selection))
                self.connection.commit()
                return cursor.lastrowid
        except pymysql.MySQLError as e:
            print(f"Erreur lors de la création de Selection: {e}")
            self.connection.rollback()
            return 0

    def read(self, id_entity: int) -> Optional[Selection]:
        """Retourne la selection en fonction de l'id souhaité"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Selection, s_date, s_number  FROM selection WHERE Id_Selection=%s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Selection(
                        id_selection=row["Id_Selection"], # type: ignore
                        date_selection=row["s_date"], # type: ignore
                        number_selection=row["s_number"] # type: ignore
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read de la Selection: {e}")
            return None

    def read_all(self) -> List[Selection]:
        """Retourne la liste de toutes les sélections"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Selection, s_date, s_number FROM selection"
                cursor.execute(sql)
                rows = cursor.fetchall()
                selections = []
                for row in rows:
                    selections.append(
                        Selection(
                            id_selection=row["Id_Selection"], # type: ignore
                            date_selection=row["s_date"], # type: ignore
                            number_selection=row["s_number"] # type: ignore
                        )
                    )
                return selections
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all de Selection: {e}")
            return []

    def get_current_selection(self):
        """Récupère et affiche la sélection de livres actuellement active"""
        active = self.get_active_selection()
        if not active:
            return "Aucune sélection active."

        selection_id = active.id_selection

        with self.connection.cursor() as cursor:
            sql = """
                SELECT b_title, a_first_name, a_last_name, p_name
                FROM book b
                INNER JOIN publisher p ON b.Id_Publisher = p.Id_Publisher
                INNER JOIN author a ON b.Id_Author = a.Id_Author
                INNER JOIN possess pos ON b.Id_Book = pos.Id_Book
                WHERE pos.Id_Selection = %s;
            """
            cursor.execute(sql, (selection_id,))
            rows = cursor.fetchall()

        if not rows:
            return f"Aucun livre dans la sélection {active.number_selection}."

        lines = []
        for r in rows:
            lines.append(
                f"{r['b_title']} — {r['a_first_name']} {r['a_last_name']} (Éditeur : {r['p_name']})"
            )
        return "\n".join(lines)

    def update_selection(self, book_id: int, selection_number: int) -> bool:
        """
        Met à jour la sélection d'un livre en le déplaçant vers une autre sélection
        - book_id (int) : identifiant du livre à déplacer.
        - selection_number (int) : numéro de la sélection cible.
        Returns:
        - bool : True si la mise à jour a réussi sinon False
        """
        try:
            book_id = int(book_id)
            selection_number = int(selection_number)

            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT Id_Selection FROM selection WHERE s_number = %s",
                    (selection_number,)
                )
                row = cursor.fetchone()

                if not row:
                    print(f"La sélection {selection_number} n'existe pas !")
                    return False

                selection_id = row["Id_Selection"] # type: ignore

                sql = "UPDATE possess SET Id_Selection = %s WHERE Id_Book = %s"
                cursor.execute(sql, (selection_id, book_id))

            self.connection.commit()
            return cursor.rowcount > 0
        except (ValueError, pymysql.MySQLError) as e:
            print(f"Erreur update_selection: {e}")
            self.connection.rollback()
            return False

    def go_to_next_selection(self):
        """
        Passe à la sélection suivante en :
        1. Récupérant les livres qui ont des votes
        2. Créant la nouvelle sélection
        3. Y plaçant ces livres
        4. Vidant les votes
        """
        try:
            current = self.get_active_selection()
            if not current:
                print("Aucune sélection active !")
                return False

            new_number = current.number_selection + 1

            with self.connection.cursor() as cursor:
                # 1. Récupérer les livres qui ont reçu des votes
                cursor.execute("""
                    SELECT DISTINCT Id_Book
                    FROM vote
                    WHERE Id_Selection = %s
                """, (current.id_selection,))

                voted_books = [row['Id_Book'] for row in cursor.fetchall()]

                if not voted_books:
                    print("Aucun livre n'a reçu de vote !")
                    return False

                print(f"{len(voted_books)} livre(s) sélectionné(s) pour la suite !")

                # 2. Créer ou récupérer la nouvelle sélection
                cursor.execute(
                    "SELECT Id_Selection FROM selection WHERE s_number = %s",
                    (new_number,)
                )
                row = cursor.fetchone()

                if row:
                    new_selection_id = row["Id_Selection"]
                else:
                    cursor.execute(
                        "INSERT INTO selection (s_date, s_number) VALUES (NOW(), %s)",
                        (new_number,)
                    )
                    new_selection_id = cursor.lastrowid

                # 3. Déplacer les livres votés vers la nouvelle sélection
                for book_id in voted_books:
                    cursor.execute(
                        "SELECT 1 FROM possess WHERE Id_Book = %s AND Id_Selection = %s",
                        (book_id, new_selection_id)
                    )
                    if not cursor.fetchone():
                        # Insérer dans la nouvelle sélection
                        cursor.execute(
                            "INSERT INTO possess (Id_Book, Id_Selection) VALUES (%s, %s)",
                            (book_id, new_selection_id)
                        )

            self.connection.commit()
            print(f"Passage à la sélection {new_number} effectué !")
            return True

        except pymysql.MySQLError as e:
            print(f"Erreur dans go_to_next_selection : {e}")
            self.connection.rollback()
            return False

    def get_books_from_selection(self, selection_id: int) -> List[Book]:
        """
        Récupère les livres associés à une sélection donnée:
         - selection_id (int) : identifiant de la sélection
         Returns:
         - List[Book] : liste des livres de la sélection
        """
        with self.connection.cursor() as cursor:
            sql = """   SELECT b_title, a_first_name, a_last_name, p_name
                        FROM book b
                        INNER JOIN publisher p ON b.Id_Publisher = p.Id_Publisher
                        INNER JOIN author a ON b.Id_Author = a.Id_Author
                        INNER JOIN possess pos ON b.Id_Book = pos.Id_Book
                        WHERE pos.Id_Selection = %s;
                    """
            cursor.execute(sql, (selection_id,))
            return cursor.fetchall() # type: ignore

    def get_active_selection(self):
        """
           Récupère la sélection active (la plus récente)
           Returns:
           - Selection | None : objet Selection actif ou None si aucune sélection
           """
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT s.Id_Selection, s.s_date, s.s_number
                    FROM selection s
                    INNER JOIN possess p ON s.Id_Selection = p.Id_Selection
                    GROUP BY s.Id_Selection, s.s_date, s.s_number
                    ORDER BY CAST(s.s_number AS UNSIGNED) DESC
                    LIMIT 1;
                """
                cursor.execute(sql)
                row = cursor.fetchone()
                if row:
                    return Selection(
                        id_selection=row["Id_Selection"],
                        date_selection=row["s_date"],
                        number_selection=int(row["s_number"])
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur dans get_active_selection: {e}")
            return None

    def delete(self, obj: T) -> bool:
        """Supprimer une selection"""
        return True