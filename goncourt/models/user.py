from dataclasses import dataclass

from goncourt.models.person import Person

""" Classe représentant une User qui hérite de la classe Person """

@dataclass
class User(Person):

    def get_role(self) -> str:
        return "User"