from typing import List, Optional
import pymysql

from goncourt.daos.dao import T
from goncourt.models.author import Author
from goncourt.daos.dao import Dao

class AuthorDao(Dao[Author]):
    def delete(self, obj: T) -> bool:
        """Supprimer un auteur"""
        return True

    def update(self, obj: T) -> bool:
        """Update un auteur"""
        return True

    def create(self, obj: T) -> int:
        """Créer un auteur"""
        return 0

    def read(self, id_entity: int) -> Optional[Author]:
        """Retourner un auteur en fonction de son id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Author, a_first_name, a_last_name, a_biography FROM author WHERE Id_Author = %s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Author(
                        id_author=row["Id_Author"], # type: ignore
                        first_name=row["a_first_name"], # type: ignore
                        last_name=row["a_last_name"], # type: ignore
                        biography=row["a_biography"] # type: ignore
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read Author: {e}")
            return None

    def read_all(self) -> List[Author]:
        """Retourne la liste de tous les auteurs"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Author, a_first_name, a_last_name, a_biography FROM author"
                cursor.execute(sql)
                rows = cursor.fetchall()
                authors = []
                for row in rows:
                    authors.append(
                        Author(
                            id_author=row["Id_Author"], # type: ignore
                            first_name=row["a_first_name"], # type: ignore
                            last_name=row["a_last_name"], # type: ignore
                            biography=row["a_biography"] # type: ignore
                        )
                    )
                return authors
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all Author: {e}")
            return []