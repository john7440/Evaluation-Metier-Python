from dataclasses import dataclass, field
from typing import List, Optional

from goncourt.models.book import Book

""" Classe représentant un éditeur avec son nom et son adresse """

@dataclass
class Publisher:
    name: str
    address: str
    id_publisher: Optional[int] = None

    books: List["Book"] = field(default_factory=list)

    def __str__(self):
        return f"{self.name}: {self.address}"