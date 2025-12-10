from typing import List, Optional
import pymysql
from goncourt.models.selection import Selection
from goncourt.daos.dao import Dao, T

class SelectionDao(Dao[Selection]):
    def update(self, obj: T) -> bool:
        pass

    def create(self, obj: T) -> int:
        """Créer un selection"""
        pass

    def read(self, id_entity: int) -> Optional[Selection]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Selection, s_date, s_number  FROM selection WHERE Id_Selection=%s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Selection(
                        id_selection=row["Id_Selection"],
                        date_selection=row["s_date"],
                        number_selection=row["s_number"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read de la Selection: {e}")
            return None

    def read_all(self) -> List[Selection]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Selection, s_date, s_number FROM selection"
                cursor.execute(sql)
                rows = cursor.fetchall()
                selections = []
                for row in rows:
                    selections.append(
                        Selection(
                            id_selection=row["Id_Selection"],
                            date_selection=row["s_date"],
                            number_selection=row["s_number"]
                        )
                    )
                return selections
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all de Selection: {e}")
            return []

    def get_current_selection(self):
        with self.connection.cursor() as cursor:
            sql = """
                SELECT b_title, a_first_name, a_last_name, p_name
                FROM book b
                INNER JOIN publisher p ON b.Id_Publisher = p.Id_Publisher
                INNER JOIN author a ON b.Id_Author = a.Id_Author
                INNER JOIN possess pos ON b.Id_Book = pos.Id_Book
                WHERE pos.Id_Selection = 1;
            """
            cursor.execute(sql)
            rows = cursor.fetchall()

        if not rows:
            return "Aucune sélection."

        lines = []
        for r in rows:
            lines.append(
                f"{r['b_title']} — {r['a_first_name']} {r['a_last_name']} (Éditeur : {r['p_name']})"

            )

        return "\n".join(lines)

    def update_selection(self, book_id, selection_id,):
        with self.connection.cursor() as cursor:
            sql = """UPDATE possess SET Id_Selection = %s WHERE Id_Book = %s"""
            cursor.execute(sql, (selection_id, book_id))
            self.connection.commit()

    def get_highest_selection(self)-> Optional[Selection]:
        """
        Retourne la sélection ayant la valeur s_number la plus élevée
        Exemple : priorité à 1, puis 2, puis 3...
        """
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Selection, s_date, s_number  FROM selection ORDER BY s_number ASC LIMIT 1"
                cursor.execute(sql)
                row = cursor.fetchone()
                if row:
                    return Selection(
                        id_selection=row["Id_Selection"],
                        date_selection=row["s_date"],
                        number_selection=row["s_number"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors de get_highest_selection: {e}")
            return None


    def delete(self, obj: T) -> bool:
        """Supprimer une selection"""
        pass