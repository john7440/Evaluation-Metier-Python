from typing import List, Optional
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.character import Character

class CharacterDao(Dao[Character]):
    def create(self, obj: T) -> int:
        """Créer un personnage"""
        pass

    def read(self, id_entity: int) -> Optional[Character]:
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT Id_Character, c_name, Id_Book
                    FROM character_table
                    WHERE Id_Character = %s
                """
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Character(
                        id_character=row["Id_Character"],
                        name=row["c_name"],
                        id_book=row["Id_Book"]
                    )
                return None

        except pymysql.MySQLError as e:
            print(f"Erreur lors du read: {e}")
            return None

    def read_all(self) -> List[Character]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Character, c_name, Id_Book FROM character_table"
                cursor.execute(sql)
                rows = cursor.fetchall()
                characters = []
                for row in rows:
                    characters.append(
                        Character(
                            id_character=row["Id_Character"],
                            name=row["c_name"],
                            id_book=row["Id_Book"]
                        )
                    )
                return characters

        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all Character: {e}")
            return []

    def update(self, obj: T) -> bool:
        """Update un personnage"""
        pass

    def delete(self, obj: T) -> bool:
        """Supprimer un personnage"""
        pass