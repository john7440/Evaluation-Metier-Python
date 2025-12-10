from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date

@dataclass
class Book:
    """
    Classe représentant un livre dans le système:

    - title (str) : titre du livre
    - publication_date (date) : date de publication du livre
    - pages (int) : nombre de pages
    - id_book (Optional[int]) : identifiant unique du livre (optionnel)
    - summary (Optional[str]) : résumé du livre (optionnel)
    - isbn (Optional[str]) : numéro ISBN du livre (optionnel)
    - price (Optional[float]) : prix du livre (optionnel)

    - id_author (Optional[Author]) : référence vers l'auteur du livre
    - id_publisher (Optional[Publisher]) : référence vers l'éditeur du livre
    - selections (List[Selection]) : liste des sélections auxquelles le livre appartient
    - characters (List[Character]) : liste des personnages associés au livre
    - votes (List[Vote]) : liste des votes liés au livre
    """
    title: str
    publication_date: date
    pages: int
    id_book: Optional[int] = None
    summary: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = None

    id_author: Optional["Author"] = None # type: ignore
    id_publisher: Optional["Publisher"] = None # type: ignore
    selections: List["Selection"] = field(default_factory=list)  # type: ignore
    characters: List["Character"] = field(default_factory=list) # type: ignore
    votes: List["Vote"] = field(default_factory=list) # type: ignore

    def __str__(self):
        return f"{self.title}, ({self.publication_date.year})"