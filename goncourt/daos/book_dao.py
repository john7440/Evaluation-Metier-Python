from typing import Optional, List
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.book import Book

"""Le dao des Livres"""

class BookDao(Dao[Book]):
    def read_all(self) -> List[T]:
        """Afficher tous les livres"""
        pass

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
                    return Book(
                        title=row["b_title"],
                        publication_date=row["b_publicationDate"],
                        pages=row["b_pagesNb"],
                        id_book= row["Id_Book"],
                        summary=row["b_summary"],
                        isbn=row["b_isbn"],
                        price=row["b_price"],
                        id_author=row["Id_Author"],
                        id_publisher=row["Id_Publisher"]
                    )
        except pymysql.MySQLError as e:
            print(f"Erreur: {e}")
            return None

    def update(self, obj: T) -> bool:
        """Update an existing book"""
        pass

    def delete(self, obj: T) -> bool:
        """Delete an existing book"""
        pass