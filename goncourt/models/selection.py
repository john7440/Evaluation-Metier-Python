from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

from goncourt.models.book import Book

"""Classe qui représente les différente sélection avec leur numéro, date et la liste des livres"""

@dataclass
class Selection:
    date_selection: date
    number_selection: int
    id_selection: Optional[int] = None

    # Une sélection contient plusieurs livres
    books: List[Book] = field(default_factory=list)

    def __str__(self):
        return f"Sélection {self.number_selection} ({self.date_selection})"