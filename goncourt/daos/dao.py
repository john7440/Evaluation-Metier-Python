from abc import ABC, abstractmethod
from typing import Optional, ClassVar, TypeVar, Generic, List
import pymysql  # type: ignore

T = TypeVar("T")

class Dao(ABC, Generic[T]):
    connection: ClassVar[pymysql.Connection] = pymysql.connect(
        host="localhost",
        user="goncourt",
        password="Louvre",
        database="goncourt",
        cursorclass=pymysql.cursors.DictCursor
    )

    @abstractmethod
    def create(self, obj: T) -> int:
        """Crée l'entité en BD correspondant à l'objet obj
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...

    @abstractmethod
    def read(self, id_entity: int) -> Optional[T]:
        """Renvoie l'objet correspondant à l'entité dont l'id est id_entity"""
        ...

    @abstractmethod
    def read_all(self) -> List[T]:
        """Renvoie la liste de toutes les entités de la table"""
        ...

    @abstractmethod
    def update(self, obj: T) -> bool:
        """Met à jour en BD l'entité correspondant à obj"""
        ...

    @abstractmethod
    def delete(self, obj: T) -> bool:
        """Supprime en BD l'entité correspondant à obj"""
        ...

