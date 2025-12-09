from typing import Optional, List
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.book import Book

"""Le dao des Livres"""

class BookDao(Dao[Book]):
    def create(self, obj: T) -> int:
        """Create a new book"""
        pass

    def read(self, id_entity: int) -> Optional[Book]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM book WHERE Id_Book=%s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Book(**row)
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur: {e}")
            return None

    def read_all(self) -> List[Book]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM book"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [Book(**row) for row in rows]
        except pymysql.MySQLError as e:
            print(f"Erreur: {e}")
            return []

    def update(self, obj: T) -> bool:
        """Update an existing book"""
        pass

    def delete(self, obj: T) -> bool:
        """Delete an existing book"""
        pass