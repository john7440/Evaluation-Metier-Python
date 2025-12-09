# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de JuryMember et User
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Person(ABC):
    first_name: str
    last_name: str

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def get_role(self) -> str:
        """Méthode à implémenter dans JuryMember et User"""
        pass