from dataclasses import dataclass, field
from typing import List

from goncourt.models.book import Book

""" Classe représentant un éditeur avec son nom et son adresse """

@dataclass
class Publisher:
    jury_member: str

@dataclass
class Publisher:
    name: str
    address: str

    books: List["Book"] = field(default_factory=list)