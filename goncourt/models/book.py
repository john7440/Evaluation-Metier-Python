from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date

@dataclass
class Book:
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