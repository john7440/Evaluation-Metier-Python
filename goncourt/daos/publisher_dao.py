from typing import List, Optional
import pymysql

from goncourt.daos.dao import T, Dao
from goncourt.models.publisher import Publisher

class PublisherDao(Dao[Publisher]):
    def delete(self, obj: T) -> bool:
        pass

    def update(self, obj: T) -> bool:
        pass

    def create(self, obj: T) -> int:
        pass

    def read(self, id_entity: int) -> Optional[Publisher]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Publisher, name, address FROM publisher WHERE Id_Publisher = %s"
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return Publisher(
                        id_publisher=row["Id_Publisher"],
                        name=row["name"],
                        address=row["address"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read Publisher: {e}")
            return None

    def read_all(self) -> List[Publisher]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_Publisher, p_name, p_address FROM publisher"
                cursor.execute(sql)
                rows = cursor.fetchall()
                publishers = []
                for row in rows:
                    publishers.append(
                        Publisher(
                            id_publisher=row["Id_Publisher"],
                            name=row["p_name"],
                            address=row["p_address"]
                        )
                    )
                return publishers
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all Publisher: {e}")
            return []
