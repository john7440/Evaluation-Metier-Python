from typing import Optional, List
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.book import Book

"""Le dao des Livres"""

class BookDao(Dao[Book]):
    def read_all(self) -> List[T]:
        """Afficher tous les livres"""
        return []

    def create(self, obj: T) -> int:
        """Create a new book"""
        return 0

    def read(self, id_entity: int) -> Optional[Book]:  # type: ignore
        """Retourner un livre en fonction de son id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM book WHERE Id_Book=%s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Book(
                        title=row["b_title"], # type: ignore
                        publication_date=row["b_publicationDate"], # type: ignore
                        pages=row["b_pagesNb"], # type: ignore
                        id_book= row["Id_Book"], # type: ignore
                        summary=row["b_summary"], # type: ignore
                        isbn=row["b_isbn"], # type: ignore
                        price=row["b_price"],# type: ignore
                        id_author=row["Id_Author"], # type: ignore
                        id_publisher=row["Id_Publisher"] # type: ignore
                    )
        except pymysql.MySQLError as e:
            print(f"Erreur: {e}")
            return None

    def update(self, obj: T) -> bool:
        """Update an existing book"""
        return True

    def delete(self, obj: T) -> bool:
        """Delete an existing book"""
        return True