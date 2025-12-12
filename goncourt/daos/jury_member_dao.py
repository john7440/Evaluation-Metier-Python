from typing import List, Optional
import pymysql

from goncourt.daos.dao import Dao, T
from goncourt.models.jury_member import JuryMember


class JuryMemberDao(Dao[JuryMember]):
    def create(self, obj: T) -> int:
        """Create a new JuryMember """
        return 0

    def read(self, id_entity: int) -> Optional[JuryMember]:
        """Renvoie un membre du jury en fonction de son id"""
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT Id_JuryMember, j_first_name, j_last_name, j_role
                    FROM jurymember
                    WHERE Id_JuryMember = %s
                    """
                cursor.execute(sql, (id_entity,))
                row = cursor.fetchone()
                if row:
                    return JuryMember(
                        id_jury=row["Id_JuryMember"],
                        first_name=row["j_first_name"],
                        last_name=row["j_last_name"],
                        role=row["j_role"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur: {e}")
            return None

    def read_all(self) -> List[JuryMember]:
        """Renvoie une liste de tous les membres du jury"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT Id_JuryMember, j_first_name, j_last_name,j_role FROM jurymember"
                cursor.execute(sql)
                rows = cursor.fetchall()
                jury_members = []
                for row in rows:
                    jury_members.append(
                        JuryMember(
                            id_jury=row["Id_JuryMember"],
                            first_name=row["j_first_name"],
                            last_name=row["j_last_name"],
                            role=row["j_role"]
                        )
                    )
                return jury_members
        except pymysql.MySQLError as e:
            print(f"Erreur lors du read_all: {e}")
            return []

    def update(self, obj: T) -> bool:
        """Update a JuryMember"""
        return True

    def delete(self, obj: T) -> bool:
        """Delete a JuryMember"""
        return True

    def authenticate(self, login: str, password: str) -> Optional[JuryMember]:
        """Vérifie les identifiants de connexion et retourne le membre du jury si valide """
        try:
            with self.connection.cursor() as cursor:
                sql="""
                    SELECT Id_JuryMember, j_first_name, j_last_name, j_role, j_connection_id, j_password, j_role
                    FROM jurymember
                    WHERE j_connetion_id = %s AND j_password = %s"""
                cursor.execute(sql, (login, password))
                row = cursor.fetchone()

                if row:
                    return JuryMember(
                        id_jury=row["Id_JuryMember"], # type: ignore
                        first_name=row["j_first_name"], # type: ignore
                        last_name=row["j_last_name"], # type: ignore
                        login=row["j_connection_id"], # type: ignore
                        password=row["j_password"], # type: ignore
                        role=row["j_role"]
                    )
                return None
        except pymysql.MySQLError as e:
            print(f"Erreur lors de l'authentification: {e}")
            return None