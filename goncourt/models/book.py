from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date

@dataclass
class Book:
    b_title: str
    b_publicationDate: date
    b_pagesNb: int
    Id_Book: Optional[int] = None
    b_summary: Optional[str] = None
    b_isbn: Optional[str] = None
    b_price: Optional[float] = None

    Id_Author: Optional["Author"] = None # type: ignore
    Id_Publisher: Optional["Publisher"] = None # type: ignore
    selections: List["Selection"] = field(default_factory=list)  # type: ignore
    characters: List["Character"] = field(default_factory=list) # type: ignore
    votes: List["Vote"] = field(default_factory=list) # type: ignore

    def __str__(self):
        return f"{self.b_title}, ({self.b_publicationDate.year})"