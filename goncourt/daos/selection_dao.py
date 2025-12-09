from typing import List, Optional
import pymysql
from goncourt.models.selection import Selection
from goncourt.daos.dao import Dao, T


class SelectionDao(Dao[Selection]):
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

    def update(self, obj: T) -> bool:
        """Update une selection"""
        pass

    def delete(self, obj: T) -> bool:
        """Supprimer une selection"""
        pass